import pandas as pd
from pathlib import Path
from utils.excel_parser import parse_daqbook_offsets_from_excel

def test_excel_parser_outputs_match_expected_csv():
    base_path = Path(__file__).parent / "data"
    excel_path = base_path / "J1_0325.xlsm"
    csv_path = base_path / "J10325_offsets.csv"

    # Read expected data
    expected = pd.read_csv(csv_path).sort_values(["Temp", "Point"]).reset_index(drop=True)

    # Parse actual Excel data
    actual = pd.DataFrame(parse_daqbook_offsets_from_excel(str(excel_path), "J10325"))
    actual = actual.sort_values(["Temp", "Point"]).reset_index(drop=True)

    # Ensure column match
    assert list(actual.columns) == list(expected.columns) + ["Delta"]

    # Compare core values
    pd.testing.assert_frame_equal(
        actual[["Temp", "Point", "Reading"]],
        expected[["Temp", "Point", "Reading"]],
        check_dtype=False,
        check_exact=False,
        atol=0.01
    )

    print(f"\u2705 {len(expected)} rows validated against expected output")

def test_csv_structure_and_point_range():
    csv_path = Path(__file__).parent / "data" / "J10325_offsets.csv"
    df = pd.read_csv(csv_path)
    assert set(df.columns) == {"Temp", "Point", "Reading"}

    expected_temps = [-100, -50, 0, 250, 500, 1000]
    for temp in expected_temps:
        points = df[df.Temp == temp].Point.tolist()
        assert sorted(points) == list(range(1, 41)), f"Unexpected points for Temp {temp}"

    print("\u2705 CSV structure and point ranges validated")
