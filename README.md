# Healthcare Datasets

## About

Healthcare Datasets is a complete, portfolio-ready data science project built around a synthetic healthcare dataset spanning 2019–2024 with 10,000 patient records. The dataset covers patient demographics, medical conditions, and billing information, providing a realistic environment for learning and experimentation while keeping privacy at the center by using non-identifiable, synthetic records.

This repository is structured to support the full analytics lifecycle: dataset validation, exploratory analysis, visualization, and baseline predictive modeling. Developed using Python, Jupyter Notebook, and libraries including Pandas, NumPy, Seaborn, Matplotlib, and scikit-learn, it helps learners move beyond isolated notebook experiments and practice reproducible, script-driven workflows that reflect real-world data science execution.

The project is designed for multiple experience levels. Beginners can focus on profiling and data cleaning fundamentals, intermediate users can build stronger feature pipelines and model evaluations, and portfolio builders can present a healthcare-focused project with clear documentation and reproducibility.

## GitHub About (Short)

Synthetic healthcare dataset (2019–2024, 10k records) for end-to-end data validation, EDA, visualization, and baseline ML — built with Python, Pandas, NumPy, and Seaborn.

Tagline: From raw healthcare data to validated insights and baseline predictions.

## Project Goal

This repository provides a realistic but privacy-safe dataset and tooling for:

- practicing data cleaning and preprocessing
- performing exploratory data analysis (EDA)
- building visual insights for healthcare trends
- training and evaluating baseline tabular ML models

All records are synthetic and intended for educational, research, and portfolio use where real patient data cannot be shared.

## Repository Contents

- `healthcare_dataset.csv`: Main dataset.
- `healthcare_datasets.ipynb`: Jupyter notebook with EDA and modeling exploration.
- `Healthcare datasets Notes .txt`: Working notes and draft analysis.
- `Healthcare datasets primary ask.txt`: Additional project notes.
- `scripts/validate_dataset.py`: Lightweight dataset quality validator.
- `scripts/eda_summary.py`: Console EDA summary report.
- `scripts/train_baseline.py`: Baseline multi-class classifier for `Test Results`.
- `requirements.txt`: Python dependencies.

## Dataset Columns

The CSV file contains the following fields:

1. `Name`
2. `Age`
3. `Gender`
4. `Blood Type`
5. `Medical Condition`
6. `Date of Admission`
7. `Doctor`
8. `Hospital`
9. `Insurance Provider`
10. `Billing Amount`
11. `Room Number`
12. `Admission Type`
13. `Discharge Date`
14. `Medication`
15. `Test Results`

## Requirements

- Python 3.10+
- `pip` (latest recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Open `healthcare_datasets.ipynb` in VS Code or Jupyter.
4. Update any local file paths in notebook/text notes if needed.
5. Run cells from top to bottom.

## Validate the Dataset (Optional)

Run a quick schema and quality check:

```bash
python scripts/validate_dataset.py
```

The validator checks:

- required columns exist
- key date columns can be parsed
- missing-value summary
- basic categorical value sanity for target columns

Generate an EDA summary report:

```bash
python scripts/eda_summary.py
```

Train a baseline model:

```bash
python scripts/train_baseline.py
```

## Typical Use Cases

- Predict `Test Results` as a 3-class classification task (`Normal`, `Abnormal`, `Inconclusive`)
- Analyze billing trends by condition, hospital, or admission type
- Explore demographic patterns and condition prevalence
- Build feature pipelines for tabular ML

## Notes

- Some working notes currently include Windows-specific local paths. If you run in Linux/macOS, replace those paths with project-relative paths (for example, `healthcare_dataset.csv`).
- Notebook outputs may include previously generated plots; rerun cells in a clean environment for reproducible results.

## License and Data Disclaimer

This project is shared for educational purposes. The dataset is synthetic and does not include real patient-identifiable data.
