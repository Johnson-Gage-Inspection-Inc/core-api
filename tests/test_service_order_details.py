import pytest
from service_order_details import get_work_item_details_for_tus

def test_get_work_item_details_for_tus():
    # Test with a valid work item number
    valid_work_item_number = '56561-067667-01'
    result = get_work_item_details_for_tus(valid_work_item_number)
    assert isinstance(result, dict)
    assert result['certificateNumber'] == valid_work_item_number
    assert result['clientCompanyId'] is not None
    assert result['serviceOrderId'] is not None
    assert result['assetId'] is not None
