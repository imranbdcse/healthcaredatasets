#!/usr/bin/env python3
"""
CSV File Analyzer for Healthcare Datasets Repository
This script finds and analyzes all CSV files in the repository.
"""

import os
import pandas as pd
import numpy as np
from pathlib import Path
import sys

def find_csv_files(directory):
    """Find all CSV files in the given directory and subdirectories."""
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.csv'):
                csv_files.append(os.path.join(root, file))
    return csv_files

def analyze_csv_file(file_path):
    """Analyze a single CSV file and return basic information."""
    try:
        print(f"\n{'='*60}")
        print(f"Analyzing: {os.path.basename(file_path)}")
        print(f"Full path: {file_path}")
        print(f"{'='*60}")
        
        # Try different encodings if needed
        encodings = ['utf-8', 'unicode_escape', 'latin-1', 'cp1252']
        df = None
        encoding_used = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                encoding_used = encoding
                break
            except UnicodeDecodeError:
                continue
                
        if df is None:
            print("❌ Error: Could not read the file with any standard encoding")
            return
            
        print(f"✅ Successfully loaded with encoding: {encoding_used}")
        
        # Basic file information
        print(f"\n📊 Dataset Information:")
        print(f"   • Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"   • File size: {os.path.getsize(file_path) / 1024 / 1024:.2f} MB")
        
        # Column information
        print(f"\n📋 Columns ({len(df.columns)}):")
        for i, col in enumerate(df.columns, 1):
            dtype = str(df[col].dtype)
            null_count = df[col].isnull().sum()
            null_percent = (null_count / len(df)) * 100
            print(f"   {i:2d}. {col:<25} | Type: {dtype:<10} | Nulls: {null_count:>6} ({null_percent:>5.1f}%)")
        
        # Data preview
        print(f"\n👀 First 5 rows:")
        print(df.head().to_string(index=False))
        
        # Basic statistics for numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print(f"\n📈 Numeric Columns Statistics:")
            print(df[numeric_cols].describe().round(2).to_string())
        
        # Categorical columns summary
        categorical_cols = df.select_dtypes(include=['object']).columns
        if len(categorical_cols) > 0:
            print(f"\n📊 Categorical Columns (unique values):")
            for col in categorical_cols:
                unique_count = df[col].nunique()
                print(f"   • {col:<25}: {unique_count:>6} unique values")
                if unique_count <= 10:
                    values = df[col].value_counts().head().to_dict()
                    print(f"     Top values: {values}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error analyzing {file_path}: {str(e)}")
        return None

def main():
    """Main function to find and analyze all CSV files."""
    # Get the current directory (repository root)
    repo_root = Path(__file__).parent
    
    print("🔍 Healthcare Datasets CSV File Analyzer")
    print("=" * 60)
    print(f"Searching for CSV files in: {repo_root}")
    
    # Find all CSV files
    csv_files = find_csv_files(repo_root)
    
    if not csv_files:
        print("❌ No CSV files found in the repository.")
        return
    
    print(f"\n✅ Found {len(csv_files)} CSV file(s):")
    for i, file_path in enumerate(csv_files, 1):
        rel_path = os.path.relpath(file_path, repo_root)
        print(f"   {i}. {rel_path}")
    
    # Analyze each CSV file
    datasets = {}
    for file_path in csv_files:
        df = analyze_csv_file(file_path)
        if df is not None:
            datasets[os.path.basename(file_path)] = df
    
    # Summary
    print(f"\n{'='*60}")
    print("📋 SUMMARY")
    print(f"{'='*60}")
    print(f"Total CSV files found: {len(csv_files)}")
    print(f"Successfully analyzed: {len(datasets)}")
    
    if datasets:
        total_rows = sum(df.shape[0] for df in datasets.values())
        total_cols = sum(df.shape[1] for df in datasets.values())
        print(f"Total data points: {total_rows:,} rows across all files")
        print(f"Total columns: {total_cols} across all files")

if __name__ == "__main__":
    main()