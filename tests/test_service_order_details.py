import pytest
from deepdiff import DeepDiff

SUCCESS_CASES = [
    (
        "56561-067667-01",
        {
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
        },
    ),
    (
        "56561-074481-01",
        {
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
        },
    ),
]

IDS = [number for number, _ in SUCCESS_CASES]

@pytest.mark.parametrize(
    "work_item_number,expected",
    SUCCESS_CASES,
    ids=IDS
)
def test_work_item_details_route_with_auth(client, auth_token, work_item_number, expected):
    resp = client.get(
        f"/work_item_details?workItemNumber={work_item_number}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert resp.status_code == 200
    data = resp.get_json()
    diff = DeepDiff(expected, data, ignore_order=True, report_repetition=True)
    assert diff == {}, f"Differences found:\n{diff}"


def test_work_item_details_route_without_auth(client):
    resp = client.get("/work_item_details?workItemNumber=56561-067667-01")
    assert resp.status_code == 401
    assert resp.text == "Unauthorized"
