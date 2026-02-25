import pandas as pd
import json
import os
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ─── Load JSON with all column names ────────────────────────────────────────
with open('all_info.json', encoding='utf-8') as f:
    info = json.load(f)

# Print exact column names per sheet to confirm mapping
for k, v in info.items():
    print(f"\n[{k}] COLUMNS: {v['columns']}")
    if v['durango']:
        # Show only non-nan values
        non_nan = {col: val for col, val in v['durango'].items() if val not in (None, 'None', 'nan', 'NaN', '')}
        print(f"[{k}] DURANGO (non-null): {non_nan}")
