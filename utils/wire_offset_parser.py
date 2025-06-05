#!/usr/bin/env python
# utils/wire_offset_parser.py
"""
Wire offset Excel file parsing utilities.
Handles parsing of wire correction factor data from Excel (.xlsx) files.
"""

import re
from typing import Any, Dict, List

import openpyxl


def _parse_temperature_cell(cell_value: Any) -> float:
    """
    Given a cell value like '2000.1°F ' (possibly with trailing whitespace),
    strip off the '°F', parentheses if present, and return a float.
    Raises ValueError if the resulting text is not a float.
    """
    if cell_value is None:
        raise ValueError("Temperature cell is empty")
    s = str(cell_value).strip()
    # Remove any parentheses or '°F' markers
    # e.g. "(‐0.1°F)" → "-0.1"
    s = s.replace("(", "").replace(")", "")
    # Remove '°F' or '°f' (case-insensitive)
    s = re.sub(r"°[Ff]", "", s).strip()
    # Now s should look like '2000.1' or '-0.1'
    try:
        return float(s)
    except Exception as e:
        raise ValueError(f"Cannot parse temperature from '{cell_value}'") from e


def parse_wire_offsets_from_excel(path: str) -> List[Dict[str, Any]]:
    """
    Open the given Excel file (assumed .xlsx) and parse the 'CERT, Wire Roll'
    worksheet to extract wire offset correction factors.

    Structure:
    - Temperatures are in rows 21 and 27, columns C:J (up to 8 temperatures)
    - Correction factors are in rows 24 and 30, columns C:J (corresponding to temperatures)
    - Wire traceability number is extracted from filename

    Returns a list of dicts, each dict:
        {
          "TraceabilityNo": <string extracted from filename>,
          "NominalTemp": <float from rows 21/27>,
          "CorrectionFactor": <float from rows 24/30>
        }
    """
    wb = openpyxl.load_workbook(path, data_only=True)
    if "CERT, Wire Roll" not in wb.sheetnames:
        raise ValueError(f"'CERT, Wire Roll' sheet not found in {path}")

    ws = wb["CERT, Wire Roll"]
    results: List[Dict[str, Any]] = []

    # Extract traceability number from filename (e.g., "072513A.xlsx" -> "072513A")
    import os

    filename = os.path.basename(path)
    traceability_no = os.path.splitext(filename)[0]

    # Define temperature and correction factor row/column ranges
    temp_rows = [21, 27]  # Temperatures in rows 21 and 27
    cf_rows = [24, 30]  # Correction factors in rows 24 and 30
    columns = list(range(3, 11))  # Columns C through J (3 through 10)

    # Read temperatures and correction factors from both row sets
    for row_set_idx in range(len(temp_rows)):
        temp_row = temp_rows[row_set_idx]
        cf_row = cf_rows[row_set_idx]

        for col in columns:
            # Read temperature value
            temp_cell = ws.cell(row=temp_row, column=col).value
            if temp_cell is None:
                continue  # Skip empty temperature cells

            # Read corresponding correction factor
            cf_cell = ws.cell(row=cf_row, column=col).value
            if cf_cell is None:
                continue  # Skip if no correction factor

            try:
                # Convert to float values
                nominal_temp = float(temp_cell)
                correction_factor = float(cf_cell)

                results.append(
                    {
                        "TraceabilityNo": traceability_no,
                        "NominalTemp": nominal_temp,
                        "CorrectionFactor": correction_factor,
                    }
                )
            except (ValueError, TypeError):
                # Skip cells that can't be converted to float
                continue

    wb.close()
    return results
