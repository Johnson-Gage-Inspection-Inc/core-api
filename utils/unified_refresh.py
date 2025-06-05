# utils/unified_refresh.py
"""
Unified refresh system for detecting SharePoint file changes and triggering appropriate refresh pipelines.

This module handles:
1. WireSetCerts: Single file Pyro/WireSetCerts.xlsx
2. WireOffsets: Wire certificate .xls files in Pyro_Standards matching regex ^\d{6}[A-Z0-9]{0,5}\.xls$
3. DaqbookOffsets: DAQbook .xlsm files in Pyro_Standards matching ^(J[123]|K[456]|N2)_(0[1-9]|1[0-2])\d{2}\.xlsm$
"""

import logging
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from utils.constants import daqbook_filename_pattern, wirecert_filename_pattern
from utils.daqbook import refresh_daqbook_offsets
from utils.sharepoint_client import SharePointClient
from utils.wire_offset_refresher import refresh_wire_offsets
from utils.wire_set_cert_refresher import refresh_wire_set_certs


def get_file_categories_with_updates(
    last_checked: Optional[datetime] = None,
) -> Dict[str, Any]:
    """
    Check which file categories have updates since last refresh.

    Args:
        last_checked: DateTime to compare against. If None, checks last 24 hours.

    Returns:
        Dict with categories and their update status:
        {
            "wiresetcerts": {"has_updates": bool, "files": [...]},
            "wireoffsets": {"has_updates": bool, "files": [...]},
            "daqbookoffsets": {"has_updates": bool, "files": [...]}
        }
    """
    if last_checked is None:
        last_checked = datetime.utcnow() - timedelta(hours=24)

    logger = logging.getLogger(__name__)
    logger.info(f"Checking for file updates since: {last_checked}")

    result = {
        "wiresetcerts": {"has_updates": False, "files": []},
        "wireoffsets": {"has_updates": False, "files": []},
        "daqbookoffsets": {"has_updates": False, "files": []},
        "last_checked": last_checked.isoformat(),
    }

    try:
        # Get all files from SharePoint
        sharepoint_client = SharePointClient()

        # Check WireSetCerts.xlsx file
        try:
            wiresetcerts_file = sharepoint_client.get_wiresetcerts_file()
            if wiresetcerts_file:
                file_modified = wiresetcerts_file.get("lastModifiedDateTime")
                if file_modified:
                    # Parse ISO format datetime
                    if isinstance(file_modified, str):
                        try:
                            modified_dt = datetime.fromisoformat(
                                file_modified.replace("Z", "+00:00")
                            ).replace(tzinfo=None)
                        except ValueError:
                            # Handle different datetime formats
                            from dateutil import parser

                            modified_dt = parser.parse(file_modified).replace(
                                tzinfo=None
                            )
                    else:
                        modified_dt = file_modified

                    if modified_dt > last_checked:
                        result["wiresetcerts"]["has_updates"] = True
                        result["wiresetcerts"]["files"].append(
                            {
                                "name": wiresetcerts_file.get(
                                    "name", "WireSetCerts.xlsx"
                                ),
                                "lastModifiedDateTime": file_modified,
                                "id": wiresetcerts_file.get("id"),
                            }
                        )
                        logger.info("WireSetCerts.xlsx has updates")
        except Exception as e:
            logger.warning(f"Error checking WireSetCerts.xlsx: {e}")

        # Check files in Pyro_Standards folder for wire offsets and DAQbook files
        try:
            pyro_files = sharepoint_client.list_files_in_pyro_standards_folder()

            for file_info in pyro_files:
                filename = file_info.get("name", "")
                file_modified = file_info.get("lastModifiedDateTime") or file_info.get(
                    "last_modified"
                )

                if not file_modified:
                    continue

                # Parse modification datetime
                try:
                    if isinstance(file_modified, str):
                        try:
                            modified_dt = datetime.fromisoformat(
                                file_modified.replace("Z", "+00:00")
                            ).replace(tzinfo=None)
                        except ValueError:
                            from dateutil import parser

                            modified_dt = parser.parse(file_modified).replace(
                                tzinfo=None
                            )
                    else:
                        modified_dt = file_modified
                except Exception as e:
                    logger.warning(
                        f"Could not parse modification time for {filename}: {e}"
                    )
                    continue

                # Check if file was modified since last check
                if modified_dt <= last_checked:
                    continue

                # Categorize file by pattern
                if daqbook_filename_pattern.match(filename):
                    result["daqbookoffsets"]["has_updates"] = True
                    result["daqbookoffsets"]["files"].append(file_info)
                    logger.info(f"DAQbook file has updates: {filename}")

                elif wirecert_filename_pattern.match(filename):
                    result["wireoffsets"]["has_updates"] = True
                    result["wireoffsets"]["files"].append(file_info)
                    logger.info(f"Wire certificate file has updates: {filename}")

        except Exception as e:
            logger.warning(f"Error checking Pyro_Standards files: {e}")

    except Exception as e:
        logger.error(f"Error in get_file_categories_with_updates: {e}")

    return result


def refresh_all_updated_categories(
    last_checked: Optional[datetime] = None,
) -> Dict[str, Any]:
    """
    Check for file updates and refresh all categories that have changes.

    Args:
        last_checked: DateTime to compare against. If None, checks last 24 hours.

    Returns:
        Dict with refresh results for each category:
        {
            "categories_checked": ["wiresetcerts", "wireoffsets", "daqbookoffsets"],
            "categories_updated": ["wiresetcerts", "daqbookoffsets"],
            "results": {
                "wiresetcerts": {...},
                "wireoffsets": {"skipped": "no updates"},
                "daqbookoffsets": {...}
            },
            "summary": {
                "total_categories": 3,
                "categories_with_updates": 2,
                "total_files_processed": 15
            }
        }
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting unified refresh process")

    # Check which categories have updates
    update_status = get_file_categories_with_updates(last_checked)

    result = {
        "categories_checked": ["wiresetcerts", "wireoffsets", "daqbookoffsets"],
        "categories_updated": [],
        "results": {},
        "summary": {
            "total_categories": 3,
            "categories_with_updates": 0,
            "total_files_processed": 0,
        },
        "last_checked": update_status["last_checked"],
    }

    # Process each category that has updates
    categories_with_updates = []

    # 1. WireSetCerts refresh
    if update_status["wiresetcerts"]["has_updates"]:
        logger.info("Refreshing WireSetCerts due to file updates")
        try:
            wiresetcerts_result = refresh_wire_set_certs()
            result["results"]["wiresetcerts"] = wiresetcerts_result
            result["categories_updated"].append("wiresetcerts")
            categories_with_updates.append("wiresetcerts")

            # Add file count to summary (standardized on files_processed)
            files_processed = wiresetcerts_result.get("files_processed", 1)

            # WireSetCerts is always 1 file
            result["summary"]["total_files_processed"] += files_processed

        except Exception as e:
            logger.error(f"Error refreshing WireSetCerts: {e}")
            result["results"]["wiresetcerts"] = {
                "status": "error",
                "message": f"Refresh failed: {str(e)}",
            }
    else:
        result["results"]["wiresetcerts"] = {"skipped": "no updates"}

    # 2. Wire offsets refresh
    if update_status["wireoffsets"]["has_updates"]:
        logger.info(
            f"Refreshing wire offsets due to {len(update_status['wireoffsets']['files'])} file updates"
        )
        try:
            wireoffsets_result = refresh_wire_offsets(
                updated_files=update_status["wireoffsets"]["files"]
            )
            result["results"]["wireoffsets"] = wireoffsets_result
            result["categories_updated"].append("wireoffsets")
            categories_with_updates.append("wireoffsets")

            # Add file count to summary
            files_processed = wireoffsets_result.get("files_processed", 0)
            result["summary"]["total_files_processed"] += files_processed

        except Exception as e:
            logger.error(f"Error refreshing wire offsets: {e}")
            result["results"]["wireoffsets"] = {
                "status": "error",
                "message": f"Refresh failed: {str(e)}",
            }
    else:
        result["results"]["wireoffsets"] = {"skipped": "no updates"}

    # 3. DAQbook offsets refresh
    if update_status["daqbookoffsets"]["has_updates"]:
        logger.info(
            f"Refreshing DAQbook offsets due to {len(update_status['daqbookoffsets']['files'])} file updates"
        )
        try:
            # DAQbook refresh function handles its own file filtering
            daqbook_result = refresh_daqbook_offsets()
            result["results"]["daqbookoffsets"] = {
                "status": "success",
                "message": "DAQbook offsets refreshed successfully",
                "files_processed": len(update_status["daqbookoffsets"]["files"]),
            }
            result["categories_updated"].append("daqbookoffsets")
            categories_with_updates.append("daqbookoffsets")

            # Add file count to summary
            files_processed = len(update_status["daqbookoffsets"]["files"])
            result["summary"]["total_files_processed"] += files_processed

        except Exception as e:
            logger.error(f"Error refreshing DAQbook offsets: {e}")
            result["results"]["daqbookoffsets"] = {
                "status": "error",
                "message": f"Refresh failed: {str(e)}",
            }
    else:
        result["results"]["daqbookoffsets"] = {"skipped": "no updates"}

    # Update summary
    result["summary"]["categories_with_updates"] = len(categories_with_updates)

    logger.info(
        f"Unified refresh completed: {len(categories_with_updates)} categories updated, "
        f"{result['summary']['total_files_processed']} total files processed"
    )

    return result
