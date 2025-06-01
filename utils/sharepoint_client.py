# utils/sharepoint_client.py
"""SharePoint client for Microsoft Graph API integration."""

import os
import requests
from typing import Optional, Dict, List, Any

# For testing purposes, allow mocking of request extraction
try:
    from flask import request, has_request_context
    _flask_available = True
except ImportError:
    _flask_available = False
    request = None
    has_request_context = None


class SharePointClient:
    """Client for accessing SharePoint files via Microsoft Graph API."""

    def __init__(self, access_token: Optional[str] = None):
        """Initialize SharePoint client with access token.

        Args:
            access_token: Bearer token for Microsoft Graph API authentication.
                         If not provided, will attempt to extract from Flask request.

        Raises:
            ValueError: If no access token provided and none found in request.
        """
        if access_token:
            self.access_token = access_token
        else:
            # Try to extract from Flask request context if available
            if _flask_available and has_request_context and has_request_context() and request:
                auth_header = request.headers.get("Authorization", "")
                if auth_header.startswith("Bearer "):
                    self.access_token = auth_header.replace("Bearer ", "")
                else:
                    raise ValueError("Access token is required for SharePoint client")
            else:
                raise ValueError("Access token is required for SharePoint client")

        self.base_url = "https://graph.microsoft.com/v1.0"

        # Load SharePoint configuration from environment
        self.site_id = os.getenv(
            "SHAREPOINT_SITE_ID",
            "jgiquality.sharepoint.com,b8d7ad55-622f-41e1-9140-35b87b4616f9,160cda33-41a0-4b31-8ebf-11196986b3e3",
        )
        self.pyro_drive_id = os.getenv(
            "SHAREPOINT_PYRO_DRIVE_ID",
            "b!34PQK-JF0EmH57ieExSqveCp2B5j30NMsNTGcMEXae_5x8SnfJhdR6JqUh5dD03F",
        )
        self.pyro_standards_drive_id = os.getenv("SHAREPOINT_PYRO_STANDARDS_DRIVE_ID")

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make authenticated request to Microsoft Graph API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint relative to base URL
            **kwargs: Additional request parameters

        Returns:
            Response object from requests library
        """
        url = f"{self.base_url}/{endpoint}"
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"

        return requests.request(method, url, headers=headers, **kwargs)

    def get_site_info(self) -> Dict[str, Any]:
        """Get SharePoint site information.

        Returns:
            Dictionary containing site metadata
        """
        if not self.site_id:
            raise ValueError("SHAREPOINT_SITE_ID not configured")

        response = self._make_request("GET", f"sites/{self.site_id}")
        return response.json()

    def get_drive_items(
        self, drive_id: str, folder_path: str = ""
    ) -> List[Dict[str, Any]]:
        """Get items in a SharePoint drive folder.

        Args:
            drive_id: SharePoint drive identifier
            folder_path: Path to folder within drive (empty for root)

        Returns:
            List of drive items
        """
        if folder_path:
            endpoint = f"drives/{drive_id}/root:/{folder_path}:/children"
        else:
            endpoint = f"drives/{drive_id}/root/children"

        response = self._make_request("GET", endpoint)
        data = response.json()
        return data.get("value", [])

    def get_file_by_path(self, file_path: str, drive_id: str) -> Dict[str, Any]:
        """Get file metadata by path within a drive.

        Args:
            file_path: Path to file within the drive
            drive_id: SharePoint drive identifier

        Returns:
            File metadata dictionary
        """
        endpoint = f"drives/{drive_id}/root:/{file_path}"
        response = self._make_request("GET", endpoint)
        return response.json()

    def get_file_by_id(self, file_id: str, drive_id: str) -> Dict[str, Any]:
        """Get file metadata by file ID.

        Args:
            file_id: SharePoint file identifier
            drive_id: SharePoint drive identifier

        Returns:
            File metadata dictionary
        """
        endpoint = f"drives/{drive_id}/items/{file_id}"
        response = self._make_request("GET", endpoint)
        return response.json()

    def search_files(self, query: str, drive_id: str) -> List[Dict[str, Any]]:
        """Search for files in a SharePoint drive.

        Args:
            query: Search query string
            drive_id: SharePoint drive identifier

        Returns:
            List of matching files
        """
        endpoint = f"drives/{drive_id}/root/search(q='{query}')"
        response = self._make_request("GET", endpoint)
        data = response.json()
        return data.get("value", [])

    def get_file_download_url(self, file_id: str, drive_id: str) -> str:
        """Get temporary download URL for a file.

        Args:
            file_id: SharePoint file identifier
            drive_id: SharePoint drive identifier

        Returns:
            Temporary download URL
        """
        endpoint = f"drives/{drive_id}/items/{file_id}/content"
        response = self._make_request("GET", endpoint, allow_redirects=False)
        return response.headers.get("Location", "")

    def get_file_reference(
        self, file_identifier: str, drive_id: str, by_path: bool = True
    ) -> Dict[str, Any]:
        """Get comprehensive file reference with metadata and download URL.

        Args:
            file_identifier: File path or ID
            drive_id: SharePoint drive identifier
            by_path: Whether file_identifier is a path (True) or ID (False)

        Returns:
            Dictionary with file metadata, download URL, and reference info
        """
        # Get file metadata
        if by_path:
            file_info = self.get_file_by_path(file_identifier, drive_id)
        else:
            file_info = self.get_file_by_id(file_identifier, drive_id)

        # Get download URL
        file_id = file_info.get("id")
        download_url = (
            self.get_file_download_url(file_id, drive_id) if file_id else None
        )

        # Build comprehensive reference
        return {
            "id": file_info.get("id"),
            "name": file_info.get("name"),
            "webUrl": file_info.get("webUrl"),
            "downloadUrl": download_url,
            "size": file_info.get("size"),
            "lastModified": file_info.get("lastModifiedDateTime"),
            "mimeType": file_info.get("file", {}).get("mimeType"),
            "driveId": drive_id,
            "path": (
                file_identifier
                if by_path
                else file_info.get("parentReference", {}).get("path", "")
            ),
        }

    def get_wiresetcerts_file(self) -> Dict[str, Any]:
        """Get WireSetCerts.xlsx file reference from Pyro Drive.

        This is an internal method that uses hardcoded drive ID and file path
        for accessing the specific WireSetCerts.xlsx file.

        Returns:
            Dictionary with WireSetCerts.xlsx file metadata and download URL

        Raises:
            ValueError: If Pyro drive ID is not configured
        """
        if not self.pyro_drive_id:
            raise ValueError(
                "SHAREPOINT_PYRO_DRIVE_ID not configured for WireSetCerts access"
            )

        # Hardcoded path for WireSetCerts.xlsx in the Pyro drive
        wiresetcerts_path = "WireSetCerts.xlsx"

        return self.get_file_reference(
            wiresetcerts_path, self.pyro_drive_id, by_path=True
        )


# Helper functions for common SharePoint operations


def get_pyro_file_reference(file_path: str, access_token: str) -> Dict[str, Any]:
    """Get file reference from Pyro drive.

    Args:
        file_path: Path to file within Pyro drive
        access_token: Bearer token for authentication

    Returns:
        File reference dictionary
    """
    client = SharePointClient(access_token)
    if not client.pyro_drive_id:
        raise ValueError("SHAREPOINT_PYRO_DRIVE_ID not configured")

    return client.get_file_reference(file_path, client.pyro_drive_id, by_path=True)


def get_pyro_standards_file_reference(
    file_path: str, access_token: str
) -> Dict[str, Any]:
    """Get file reference from Pyro Standards drive.

    Args:
        file_path: Path to file within Pyro Standards drive
        access_token: Bearer token for authentication

    Returns:
        File reference dictionary
    """
    client = SharePointClient(access_token)
    if not client.pyro_standards_drive_id:
        raise ValueError("SHAREPOINT_PYRO_STANDARDS_DRIVE_ID not configured")

    return client.get_file_reference(
        file_path, client.pyro_standards_drive_id, by_path=True
    )


def search_pyro_files(query: str, access_token: str) -> List[Dict[str, Any]]:
    """Search for files in Pyro drive.

    Args:
        query: Search query string
        access_token: Bearer token for authentication

    Returns:
        List of matching files
    """
    client = SharePointClient(access_token)
    if not client.pyro_drive_id:
        raise ValueError("SHAREPOINT_PYRO_DRIVE_ID not configured")

    return client.search_files(query, client.pyro_drive_id)


def list_pyro_folder_contents(
    folder_path: str, access_token: str
) -> List[Dict[str, Any]]:
    """List contents of a folder in Pyro drive.

    Args:
        folder_path: Path to folder within Pyro drive
        access_token: Bearer token for authentication

    Returns:
        List of folder contents
    """
    client = SharePointClient(access_token)
    if not client.pyro_drive_id:
        raise ValueError("SHAREPOINT_PYRO_DRIVE_ID not configured")

    return client.get_drive_items(client.pyro_drive_id, folder_path)


def get_wiresetcerts_file_reference(access_token: str) -> Dict[str, Any]:
    """Get WireSetCerts.xlsx file reference from Pyro Drive.

    This is a convenience function that uses the hardcoded internal method
    to fetch the specific WireSetCerts.xlsx file.

    Args:
        access_token: Bearer token for authentication

    Returns:
        Dictionary with WireSetCerts.xlsx file metadata and download URL
    """
    client = SharePointClient(access_token)
    return client.get_wiresetcerts_file()


def make_sharepoint_client(access_token: str) -> SharePointClient:
    """Factory function to create SharePoint client.

    Args:
        access_token: Bearer token for authentication

    Returns:
        Configured SharePointClient instance
    """
    return SharePointClient(access_token)
