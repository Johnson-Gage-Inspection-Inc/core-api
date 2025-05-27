import os
from flask import request, Response
from app import app

if os.getenv("SKIP_AUTH", "false").lower() == "true":

    print(">>> Registered view function keys:")
    for k in sorted(app.view_functions):
        print("   ", k)

    print(">>> Patching app.view_functions for all protected endpoints")

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

    # /work_item_details
    def fake_work_item_details():
        if resp := fake_auth_check():
            return resp
        wid = request.args.get("workItemNumber")

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
                "assetPoolId": 620646
            }
        ]

    app.view_functions["whoami.Whoami"] = fake_whoami
    app.view_functions["work_item_details.WorkItemDetails"] = fake_work_item_details
    app.view_functions["pyro-assets.PyroAssets"] = fake_pyro_assets
