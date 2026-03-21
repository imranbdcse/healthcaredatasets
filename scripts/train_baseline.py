from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


TARGET_COLUMN = "Test Results"

# Admission-time friendly feature set.
FEATURE_COLUMNS = [
    "Age",
    "Gender",
    "Blood Type",
    "Medical Condition",
    "Doctor",
    "Hospital",
    "Insurance Provider",
    "Billing Amount",
    "Room Number",
    "Admission Type",
    "Medication",
]


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "healthcare_dataset.csv"

    if not csv_path.exists():
        print(f"[ERROR] Dataset not found: {csv_path}")
        return 1

    df = pd.read_csv(csv_path)

    required = set(FEATURE_COLUMNS + [TARGET_COLUMN])
    missing = [c for c in required if c not in df.columns]
    if missing:
        print("[ERROR] Missing required columns for training:")
        for c in missing:
            print(f"  - {c}")
        return 1

    work_df = df[FEATURE_COLUMNS + [TARGET_COLUMN]].copy()
    work_df = work_df.dropna(subset=[TARGET_COLUMN])

    X = work_df[FEATURE_COLUMNS]
    y = work_df[TARGET_COLUMN]

    categorical_features = [
        "Gender",
        "Blood Type",
        "Medical Condition",
        "Doctor",
        "Hospital",
        "Insurance Provider",
        "Admission Type",
        "Medication",
    ]
    numeric_features = ["Age", "Billing Amount", "Room Number"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", "passthrough", numeric_features),
        ]
    )

    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,
    )

    clf = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("=== Baseline Model: RandomForestClassifier ===")
    print(f"Train rows: {len(X_train):,}")
    print(f"Test rows:  {len(X_test):,}")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, digits=4))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
