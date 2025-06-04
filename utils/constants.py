# utils/constants.py
"""
Shared constants for the JGI API.
"""

import re

# DAQbook filename pattern matching J1_*, J2_*, J3_*, K4_*, K5_*, K6_*, N2_*.xlsm
daqbook_filename_regex = r"^(J[123]|K[456]|N2)_(0[1-9]|1[0-2])\d{2}\.xlsm$"
daqbook_filename_pattern = re.compile(daqbook_filename_regex, re.IGNORECASE)

wirecert_filename_regex = r"^\d{6}[A-Z0-9]{0,5}\.xls$"
wirecert_filename_pattern = re.compile(wirecert_filename_regex, re.IGNORECASE)
