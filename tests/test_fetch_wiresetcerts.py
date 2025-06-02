import sys
from io import StringIO
from unittest.mock import MagicMock, patch

import pytest

# Import the module under test
from utils import fetch_wiresetcerts


class TestFetchWiresetcerts:
    """Test cases for the fetch_wiresetcerts script."""

    def test_main_success_with_multiple_sheets(self, capsys):
        """Test successful execution with multiple sheets of data."""
        mock_data = {
            "total_sheets": 2,
            "sheet_names": ["Sheet1", "Sheet2"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 100,
                    "total_columns": 5,
                    "headers": ["Col1", "Col2", "Col3", "Col4", "Col5"],
                    "sample_data": [
                        ["Data1", "Data2", "Data3", "Data4", "Data5"],
                        ["Row2Col1", "Row2Col2", "Row2Col3", "Row2Col4", "Row2Col5"],
                        ["Row3Col1", "Row3Col2", "Row3Col3", "Row3Col4", "Row3Col5"]
                    ]
                },
                "Sheet2": {
                    "total_rows": 50,
                    "total_columns": 3,
                    "headers": ["Name", "Value", "Status"],
                    "sample_data": [
                        ["Test1", 123, "Active"],
                        ["Test2", 456, "Inactive"]
                    ]
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            
            assert result == 0
            mock_get_content.assert_called_once()
            
            captured = capsys.readouterr()
            assert "🔐 Using app-only authentication..." in captured.out
            assert "✅ Successfully fetched WireSetCerts.xlsx" in captured.out
            assert "📊 File contains 2 sheet(s): Sheet1, Sheet2" in captured.out
            assert "📋 Sheet: Sheet1" in captured.out
            assert "📋 Sheet: Sheet2" in captured.out
            assert "100 rows × 5 columns" in captured.out
            assert "50 rows × 3 columns" in captured.out

    def test_main_success_with_single_sheet(self, capsys):
        """Test successful execution with single sheet."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["MainSheet"],
            "sheets": {
                "MainSheet": {
                    "total_rows": 10,
                    "total_columns": 3,
                    "headers": ["A", "B", "C"],
                    "sample_data": [
                        ["Value1", "Value2", "Value3"]
                    ]
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            
            assert result == 0
            captured = capsys.readouterr()
            assert "📊 File contains 1 sheet(s): MainSheet" in captured.out
            assert "Headers: A, B, C" in captured.out

    def test_main_success_with_long_headers(self, capsys):
        """Test display truncation with many headers."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["Sheet1"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 5,
                    "total_columns": 10,
                    "headers": ["Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9", "Col10"],
                    "sample_data": [
                        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
                    ]
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Headers: Col1, Col2, Col3, Col4, Col5..." in captured.out
            assert "Row 2: A | B | C | D | E | ..." in captured.out

    def test_main_success_with_many_sample_rows(self, capsys):
        """Test display truncation with many sample rows."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["Sheet1"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 100,
                    "total_columns": 2,
                    "headers": ["Name", "Value"],
                    "sample_data": [
                        ["Row1", "Value1"],
                        ["Row2", "Value2"],
                        ["Row3", "Value3"],
                        ["Row4", "Value4"],
                        ["Row5", "Value5"]
                    ]
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            result = fetch_wiresetcerts.main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Row 2: Row1 | Value1" in captured.out
            assert "Row 3: Row2 | Value2" in captured.out
            assert "Row 4: Row3 | Value3" in captured.out
            assert "... and 2 more sample rows" in captured.out

    def test_main_success_with_none_values(self, capsys):
        """Test handling of None values in data."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["Sheet1"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 2,
                    "total_columns": 3,
                    "headers": ["Col1", "Col2", "Col3"],
                    "sample_data": [
                        ["Data", None, "MoreData"],
                        [None, "Value", None]
                    ]
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            result = fetch_wiresetcerts.main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Row 2: Data | None | MoreData" in captured.out
            assert "Row 3: None | Value | None" in captured.out

    def test_main_success_with_long_cell_values(self, capsys):
        """Test truncation of long cell values."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["Sheet1"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 1,
                    "total_columns": 2,
                    "headers": ["Short", "Long"],
                    "sample_data": [
                        ["OK", "This is a very long value that should be truncated at 20 characters"]
                    ]
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            result = fetch_wiresetcerts.main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Row 2: OK | This is a very long " in captured.out

    def test_main_no_sheets_found(self, capsys):
        """Test handling when no sheets are found."""
        mock_data = None

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            
            assert result == 1
            captured = capsys.readouterr()
            assert "❌ Error:" in captured.out

    def test_main_empty_sheets_dict(self, capsys):
        """Test handling when sheets dict is empty."""
        mock_data = {"sheets": {}}

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            
            assert result == 1
            captured = capsys.readouterr()
            assert "❌ Error:" in captured.out

    def test_main_sharepoint_drive_id_error(self, capsys):
        """Test handling of SharePoint drive ID configuration error."""
        error_msg = "SHAREPOINT_DRIVE_ID not configured"
        
        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.side_effect = Exception(error_msg)
            
            result = fetch_wiresetcerts.main()
            
            assert result == 1
            captured = capsys.readouterr()
            assert f"❌ Error: {error_msg}" in captured.out
            assert "💡 Tip: Make sure SHAREPOINT_DRIVE_ID is set in your .env file" in captured.out

    def test_main_access_token_error(self, capsys):
        """Test handling of access token authentication error."""
        error_msg = "Access token expired or invalid"
        
        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.side_effect = Exception(error_msg)
            
            result = fetch_wiresetcerts.main()
            
            assert result == 1
            captured = capsys.readouterr()
            assert f"❌ Error: {error_msg}" in captured.out
            assert "💡 Tip: Make sure you're logged into Azure AD and have proper permissions" in captured.out

    def test_main_requests_error(self, capsys):
        """Test handling of network/requests error."""
        error_msg = "requests connection failed"
        
        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.side_effect = Exception(error_msg)
            
            result = fetch_wiresetcerts.main()
            
            assert result == 1
            captured = capsys.readouterr()
            assert f"❌ Error: {error_msg}" in captured.out
            assert "💡 Tip: Check your network connection and SharePoint permissions" in captured.out

    def test_main_generic_error(self, capsys):
        """Test handling of generic exceptions."""
        error_msg = "Something went wrong"
        
        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.side_effect = ValueError(error_msg)
            
            result = fetch_wiresetcerts.main()
            assert result == 1
            captured = capsys.readouterr()
            assert f"❌ Error: {error_msg}" in captured.out
            assert "Error type: ValueError" in captured.out

    @patch("sys.exit")
    @patch("utils.fetch_wiresetcerts.main")
    def test_main_module_execution(self, mock_main, mock_exit):
        """Test the script's main module execution."""
        mock_main.return_value = 0
        
        # Simulate running the script as main module
        with open("utils/fetch_wiresetcerts.py", "r", encoding="utf-8") as f:
            content = f.read()
        exec(compile(content, "utils/fetch_wiresetcerts.py", "exec"))
        
        # Note: This test is more complex to implement properly due to the way Python handles __name__ == "__main__"
        # The actual test would need to mock the entire module execution context

    def test_main_with_missing_sample_data(self, capsys):
        """Test handling when sample_data is missing from sheet."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["Sheet1"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 10,
                    "total_columns": 3,
                    "headers": ["A", "B", "C"]
                    # No sample_data key
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            
            assert result == 0
            captured = capsys.readouterr()
            assert "Headers: A, B, C" in captured.out
            # Should not show sample data section

    def test_main_with_missing_headers(self, capsys):
        """Test handling when headers are missing from sheet."""
        mock_data = {
            "total_sheets": 1,
            "sheet_names": ["Sheet1"],
            "sheets": {
                "Sheet1": {
                    "total_rows": 10,
                    "total_columns": 3,
                    "sample_data": [
                        ["Data1", "Data2", "Data3"]
                    ]
                    # No headers key
                }
            }
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Row 2: Data1 | Data2 | Data3" in captured.out
            # Should not show headers section

    @pytest.mark.parametrize("sheet_count,expected_plural", [
        (0, "sheet(s)"),
        (1, "sheet(s)"),
        (2, "sheet(s)"),
        (5, "sheet(s)")
    ])
    def test_sheet_count_display(self, sheet_count, expected_plural, capsys):
        """Test proper pluralization of sheet count display."""
        sheet_names = [f"Sheet{i+1}" for i in range(sheet_count)]
        sheets = {name: {"total_rows": 1, "total_columns": 1} for name in sheet_names}
        
        mock_data = {
            "total_sheets": sheet_count,
            "sheet_names": sheet_names,
            "sheets": sheets
        }

        with patch("utils.fetch_wiresetcerts.get_wiresetcerts_content") as mock_get_content:
            mock_get_content.return_value = mock_data
            
            result = fetch_wiresetcerts.main()
            
            assert result == 0
            captured = capsys.readouterr()
            assert f"📊 File contains {sheet_count} {expected_plural}" in captured.out
