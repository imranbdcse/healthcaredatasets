from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "Name",
    "Age",
    "Gender",
    "Blood Type",
    "Medical Condition",
    "Date of Admission",
    "Doctor",
    "Hospital",
    "Insurance Provider",
    "Billing Amount",
    "Room Number",
    "Admission Type",
    "Discharge Date",
    "Medication",
    "Test Results",
]

EXPECTED_TEST_RESULTS = {"Normal", "Abnormal", "Inconclusive"}
EXPECTED_ADMISSION_TYPES = {"Emergency", "Elective", "Urgent"}


def validate_dataset(csv_path: Path) -> int:
    if not csv_path.exists():
        print(f"[ERROR] Dataset not found: {csv_path}")
        return 1

    df = pd.read_csv(csv_path)
    errors = 0

    print(f"[INFO] Loaded rows: {len(df):,}")
    print(f"[INFO] Loaded columns: {len(df.columns)}")

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        print("[ERROR] Missing required columns:")
        for col in missing_columns:
            print(f"  - {col}")
        errors += 1
    else:
        print("[OK] All required columns are present.")

    date_columns = ["Date of Admission", "Discharge Date"]
    for col in date_columns:
        if col in df.columns:
            parsed = pd.to_datetime(df[col], errors="coerce")
            invalid = parsed.isna().sum()
            if invalid > 0:
                print(f"[WARN] {col}: {invalid} unparsable date values")
            else:
                print(f"[OK] {col}: all values parse as dates")

    if "Test Results" in df.columns:
        observed = set(df["Test Results"].dropna().unique())
        unexpected = sorted(observed - EXPECTED_TEST_RESULTS)
        if unexpected:
            print(f"[WARN] Unexpected Test Results values: {unexpected}")
        else:
            print("[OK] Test Results values look valid.")

    if "Admission Type" in df.columns:
        observed = set(df["Admission Type"].dropna().unique())
        unexpected = sorted(observed - EXPECTED_ADMISSION_TYPES)
        if unexpected:
            print(f"[WARN] Unexpected Admission Type values: {unexpected}")
        else:
            print("[OK] Admission Type values look valid.")

    print("\n[INFO] Missing values by column:")
    print(df.isna().sum().to_string())

    return 1 if errors else 0


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    default_csv = project_root / "healthcare_dataset.csv"
    raise SystemExit(validate_dataset(default_csv))
