import os
from flask import request, Response
from app import app
import logging

if os.getenv("SKIP_AUTH", "false").lower() == "true":

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
        return {
            "user": "testuser@example.com",
            "sub": "fake-subject"
        }
    
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

        return Response("Not Found", 404)    # /pyro-assets
    def fake_pyro_assets():
        if resp := fake_auth_check():
            return resp
        return [
            {
                "assetId": 123456,
                "name": "Mock Pyro Asset",
                "serialNumber": "SN-FAKE-001",
                "clientCompanyId": 9999,
                "assetPoolId": 620646
            }
        ]
        
    # /asset-service-records/<assetId>
    def fake_asset_service_record(assetId):
        if resp := fake_auth_check():
            return resp
        
        # Return different responses based on the asset ID for testing
        if assetId == "12345":
            return [
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
                    "notes": "Mock service record for testing purposes"
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
                    "notes": "Annual inspection - passed"
                }
            ]
        elif assetId == "67890":
            return [
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
                    "notes": "Failed calibration - requires maintenance"
                }
            ]
        else:
            return Response("Asset service records not found", 404)

    app.view_functions["whoami.Whoami"] = fake_whoami
    app.view_functions["work-item-details.WorkItemDetails"] = fake_work_item_details
    app.view_functions["pyro-assets.PyroAssets"] = fake_pyro_assets
    app.view_functions["asset-service-records.AssetServiceRecord"] = fake_asset_service_record
