import logging
import os

from flask import Response, jsonify, request
from flask_smorest import abort

if os.getenv("SKIP_AUTH", "false").lower() == "true":
    from app import app

    logging.info("Registered view function keys:")
    for k in sorted(app.view_functions):
        print("   ", k)

    logging.info("Patching app.view_functions for all protected endpoints")

    def fake_auth_check():
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return Response("Unauthorized", 401)

    # /whoami
    def fake_whoami():
        if resp := fake_auth_check():
            return resp
        return {"user": "testuser@example.com", "sub": "fake-subject"}

    # /work-item-details
    def fake_work_item_details():
        if resp := fake_auth_check():
            return resp
        wid = request.args.get("workItemNumber")

        # Handle missing workItemNumber parameter
        if not wid:
            return Response("Missing workItemNumber", 400)

        # Handle invalid workItemNumber format
        import re

        pattern = r"^(56561-)?\d{6}(\.\d{2})?(-\d{2})(R\d{1,2})?$"
        if not re.match(pattern, wid):
            return Response("Invalid work item number format.", 500)

        if wid == "56561-067667-01":
            return {
                "assetAttributes": {},
                "assetId": 1270490,
                "assetMaker": "COL-MET",
                "assetName": "Chrome Plus, Oven No. 13, W-CPI-4143, TUS",
                "assetTag": "W-CPI-4143, TUS",
                "categoryName": "Thermometer",
                "certificateNumber": "56561-067667-01",
                "clientCompanyId": 57283,
                "manufacturerPartNumber": "GENERIC 2354",
                "productManufacturer": "Unidentified",
                "productName": "Thermometers",
                "purchaseOrderNumber": "CHR001150",
                "rootCategoryName": "Thermometers",
                "serialNumber": "OVEN NO. 13",
                "serviceOrderId": 1171585,
            }

        if wid == "56561-074481-01":
            return {
                "assetAttributes": {},
                "assetId": 1270335,
                "assetMaker": "GEHNRICH",
                "assetName": "Capps, Age Oven No. 3, TUS",
                "assetTag": "AGE OVEN NO. 3",
                "categoryName": "Thermometer",
                "certificateNumber": "56561-074481-01",
                "clientCompanyId": 57206,
                "manufacturerPartNumber": "GENERIC 2354",
                "productManufacturer": "Unidentified",
                "productName": "Thermometers",
                "purchaseOrderNumber": "53865",
                "rootCategoryName": "Thermometers",
                "serialNumber": "11108",
                "serviceOrderId": 1259027,
            }

        return Response("Not Found", 404)

    # /pyro-assets
    def fake_pyro_assets():
        if resp := fake_auth_check():
            return resp
        return [
            {
                "assetId": 123456,
                "name": "Mock Pyro Asset",
                "serialNumber": "SN-FAKE-001",
                "clientCompanyId": 9999,
                "assetPoolId": 620646,
            }
        ]  # /asset-service-records/<assetId>

    def fake_asset_service_record(assetId=None):
        from flask import request

        # For Flask-Smorest MethodView, the URL parameter is passed as a named argument
        # If not found in kwargs, try to get from request view_args
        if assetId is None:
            assetId = request.view_args.get("assetId") if request.view_args else None

        # Enforce 401 for missing/invalid Authorization
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            abort(401, message="Unauthorized")

        # Return two mock records for assetId '12345' to match test expectations
        if assetId == "12345":
            return jsonify(
                [
                    {
                        "asset_service_record_id": 1001,
                        "asset_id": 12345,
                        "service_date": "2023-01-01T00:00:00Z",
                        "result_status": "Pass",
                        "serial_number": "SN123456",
                        "asset_name": "Mock Test Asset",
                        "service_type": "Calibration",
                        "technician_name": "Mock Technician",
                        "created_date_utc": "2023-01-01T00:00:00Z",
                        "modified_date_utc": "2023-01-01T00:00:00Z",
                        "notes": "Mock service record for testing purposes",
                    },
                    {
                        "asset_service_record_id": 1002,
                        "asset_id": 12345,
                        "service_date": "2023-06-15T09:30:00Z",
                        "result_status": "Pass",
                        "serial_number": "SN123456",
                        "asset_name": "Mock Test Asset",
                        "service_type": "Inspection",
                        "technician_name": "Mock Inspector",
                        "created_date_utc": "2023-06-15T09:30:00Z",
                        "modified_date_utc": "2023-06-15T09:30:00Z",
                        "notes": "Annual inspection - passed",
                    },
                ]
            )
        elif assetId == "67890":
            return jsonify(
                [
                    {
                        "asset_service_record_id": 2001,
                        "asset_id": 67890,
                        "service_date": "2023-03-15T14:30:00Z",
                        "result_status": "Fail",
                        "serial_number": "SN789012",
                        "asset_name": "Another Mock Asset",
                        "service_type": "Calibration",
                        "technician_name": "Mock Technician",
                        "created_date_utc": "2023-03-15T14:30:00Z",
                        "modified_date_utc": "2023-03-15T14:30:00Z",
                        "notes": "Failed calibration - requires maintenance",
                    }
                ]
            )
        else:
            abort(404, message="Asset service records not found")

    # /daqbook-offsets
    def mock_get_daqbook_offsets():
        # In mock mode, bypass auth for these endpoints since the tests expect it
        # Return empty list for consistent mock behavior
        return []  # /daqbook-offsets/<tn>

    def mock_get_daqbook_offsets_by_tn(tn):
        # In mock mode, bypass auth for these endpoints since the tests expect it
        # Return empty list for consistent mock behavior
        return []

    app.view_functions["whoami.Whoami"] = fake_whoami
    app.view_functions["work-item-details.WorkItemDetails"] = fake_work_item_details
    app.view_functions["pyro-assets.PyroAssets"] = fake_pyro_assets
    app.view_functions["asset-service-records.AssetServiceRecord"] = (
        fake_asset_service_record
    )
    app.view_functions["daqbook_offsets.DaqbookOffsets"] = mock_get_daqbook_offsets
    app.view_functions["daqbook_offsets.DaqbookOffsetsByTN"] = (
        mock_get_daqbook_offsets_by_tn
    )

    print("Mock view bindings applied successfully!")
    print("Updated view functions:")
    for key in sorted(app.view_functions.keys()):
        if any(
            endpoint in key
            for endpoint in ["whoami", "work-item", "pyro", "asset-service", "daqbook"]
        ):
            print(f"  {key}: {app.view_functions[key]}")

    # SharePoint mock functions
    def mock_get_pyro_file_reference():
        """Mock SharePoint Pyro file reference endpoint."""
        if resp := fake_auth_check():
            return resp

        file_path = request.args.get("filePath")
        if not file_path:
            abort(400, message="Missing filePath parameter")

        return {
            "id": "mock-file-id-123",
            "name": file_path.split("/")[-1] if "/" in file_path else file_path,
            "webUrl": f"https://jgiquality.sharepoint.com/sites/mock/Shared%20Documents/{file_path}",
            "downloadUrl": f"https://download.sharepoint.com/temp/{file_path}",
            "size": 2048,
            "lastModified": "2025-06-01T10:00:00Z",
            "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "driveId": "mock-pyro-drive-id",
            "path": file_path,
        }

    def mock_search_pyro_files():
        """Mock SharePoint Pyro file search endpoint."""
        if resp := fake_auth_check():
            return resp

        query = request.args.get("query")
        if not query:
            abort(400, message="Missing query parameter")

        # Return mock search results
        return [
            {
                "id": "search-result-1",
                "name": f"{query}-document-1.xlsx",
                "webUrl": f"https://jgiquality.sharepoint.com/sites/mock/Shared%20Documents/{query}-document-1.xlsx",
                "size": 1024,
                "lastModified": "2025-06-01T09:00:00Z",
                "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            },
            {
                "id": "search-result-2",
                "name": f"{query}-report-2.pdf",
                "webUrl": f"https://jgiquality.sharepoint.com/sites/mock/Shared%20Documents/{query}-report-2.pdf",
                "size": 3072,
                "lastModified": "2025-05-31T15:30:00Z",
                "mimeType": "application/pdf",
            },
        ]

    def mock_list_pyro_folder_contents():
        """Mock SharePoint Pyro folder contents endpoint."""
        if resp := fake_auth_check():
            return resp

        folder_path = request.args.get("folderPath", "")

        # Return mock folder contents
        return [
            {
                "id": "folder-item-1",
                "name": "calibration-data.xlsx",
                "webUrl": f"https://jgiquality.sharepoint.com/sites/mock/Shared%20Documents/{folder_path}/calibration-data.xlsx",
                "size": 4096,
                "lastModified": "2025-06-01T08:00:00Z",
                "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            },
            {
                "id": "folder-item-2",
                "name": "test-results",
                "webUrl": f"https://jgiquality.sharepoint.com/sites/mock/Shared%20Documents/{folder_path}/test-results",
                "size": None,  # Folder has no size
                "lastModified": "2025-05-30T12:00:00Z",
                "mimeType": None,  # Folder has no MIME type
            },
        ]    # Register SharePoint mock endpoints (if they exist)
    sharepoint_endpoints = [
        "sharepoint.PyroFileReference",
        "sharepoint.PyroFileSearch",
        "sharepoint.PyroFolderContents",
    ]
    
    for endpoint in sharepoint_endpoints:
        if endpoint in app.view_functions:
            if "FileReference" in endpoint:
                app.view_functions[endpoint] = mock_get_pyro_file_reference
            elif "FileSearch" in endpoint:
                app.view_functions[endpoint] = mock_search_pyro_files
            elif "FolderContents" in endpoint:
                app.view_functions[endpoint] = mock_list_pyro_folder_contents

    # Wire Offsets mock endpoints
    def fake_wire_offsets():
        if resp := fake_auth_check():
            return resp
        # Return empty list since no data exists yet
        return []

    def fake_wire_offsets_by_wirelot(traceability_no):
        if resp := fake_auth_check():
            return resp
        # Return empty list since no data exists yet
        return []

    def fake_wire_set_certs():
        if resp := fake_auth_check():
            return resp
        # Return empty list since no data exists yet in mock mode
        return []

    def fake_wire_set_cert_by_serial(serial_number):
        if resp := fake_auth_check():
            return resp
        # Mock single wire set cert lookup
        # Return 404 for any serial number in mock mode
        from flask_smorest import abort
        abort(404, message="Wire set certificate not found")

    def fake_refresh_wire_set_certs():
        if resp := fake_auth_check():
            return resp
        # Mock successful refresh
        return {
            "message": "Wire set certificates refreshed successfully",
            "status": "success",
        }

    def fake_unified_refresh():
        """Mock unified refresh endpoint."""
        if resp := fake_auth_check():
            return resp
        # Mock successful unified refresh
        return {
            "status": "success",
            "message": "All categories refreshed successfully",
            "summary": "Refreshed 0 files across 3 categories",
            "categories": {
                "WireSetCerts": {
                    "status": "success",
                    "files_processed": 0,
                    "records_processed": 0,
                    "errors": [],
                },
                "WireOffsets": {
                    "status": "success",
                    "files_processed": 0,
                    "records_processed": 0,
                    "errors": [],
                },
                "DaqbookOffsets": {
                    "status": "success",
                    "files_processed": 0,
                    "records_processed": 0,
                    "errors": [],
                },
            },
        }

    # Register wire offsets mock endpoints
    wire_offset_endpoints = [
        "wire_offsets.WireOffsets",
        "wire_offsets.WireOffsetsByTraceabilityNo",
        "wire_offsets.WireSetCerts",
        "wire_offsets.WireSetCertBySerial",
    ]

    for endpoint in wire_offset_endpoints:
        if endpoint in app.view_functions:
            if (
                "WireOffsets" in endpoint
                and "WireOffsetsByTraceabilityNo" not in endpoint
            ):
                app.view_functions[endpoint] = fake_wire_offsets
            elif "WireOffsetsByTraceabilityNo" in endpoint:
                app.view_functions[endpoint] = fake_wire_offsets_by_wirelot            elif "WireSetCerts" in endpoint and "WireSetCertBySerial" not in endpoint:
                app.view_functions[endpoint] = fake_wire_set_certs
            elif "WireSetCertBySerial" in endpoint:
                # Mock for individual wire set cert lookup
                app.view_functions[endpoint] = fake_wire_set_cert_by_serial

    # Register unified refresh endpoint mock
    if "refresh_excel_data.ExcelRefresh" in app.view_functions:
        app.view_functions["refresh_excel_data.ExcelRefresh"] = fake_unified_refresh
