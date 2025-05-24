def test_work_item_details_route_with_auth(client, auth_token):
    """Test the work item details route with authentication."""
    response = client.get(
        "/work_item_details?workItemNumber=56561-067667-01",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["certificateNumber"] == "56561-067667-01"
    assert data['clientCompanyId'] == 57283
    assert data['serviceOrderId'] == 1171585
    assert data['assetId'] == 1270490

def test_work_item_details_route_without_auth(client):
    response = client.get("/work_item_details?workItemNumber=56561-067667-01")
    assert response.status_code == 401
    assert response.text == 'Unauthorized'

