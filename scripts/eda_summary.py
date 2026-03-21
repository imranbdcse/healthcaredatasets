from __future__ import annotations

from pathlib import Path

import pandas as pd


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "healthcare_dataset.csv"

    if not csv_path.exists():
        print(f"[ERROR] Dataset not found: {csv_path}")
        return 1

    df = pd.read_csv(csv_path)

    print("=== Healthcare Dataset EDA Summary ===")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn dtypes:")
    print(df.dtypes.to_string())

    print("\nMissing values:")
    print(df.isna().sum().to_string())

    if "Test Results" in df.columns:
        print("\nTest Results distribution (%):")
        distribution = (df["Test Results"].value_counts(normalize=True) * 100).round(2)
        print(distribution.to_string())

    if "Age" in df.columns:
        print("\nAge summary:")
        print(df["Age"].describe().to_string())

    if "Billing Amount" in df.columns:
        print("\nBilling Amount summary:")
        print(df["Billing Amount"].describe().to_string())

    for col in ["Medical Condition", "Hospital", "Insurance Provider", "Admission Type"]:
        if col in df.columns:
            print(f"\nTop 10 values for {col}:")
            print(df[col].value_counts().head(10).to_string())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
