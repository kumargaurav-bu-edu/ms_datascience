#!/usr/bin/env python3
"""
Comprehensive analysis of all 5 BFSI datasets for Milestone One.
Analyzes data types, missing values, duplicates, and basic statistics.
"""

import pandas as pd
import numpy as np
import os

DATA_DIR = "/Users/gaurav/workspace/datascience/boston_university/ms_datascience/week_10122025/AI_leaders/data"

datasets = [
    {
        "name": "Credit Card Fraud Detection",
        "path": "credit_card_fraud_detection/creditcard.csv",
        "industry": "Banking & Financial Services"
    },
    {
        "name": "Financial Distress Prediction",
        "path": "financial_distress_prediction/Financial Distress.csv",
        "industry": "Financial Services"
    },
    {
        "name": "Insurance Claims",
        "path": "insurance_claims_dataset/car_insurance_claim.csv",
        "industry": "Insurance"
    },
    {
        "name": "Credit Score Classification",
        "path": "credit_score_classification/train.csv",
        "industry": "Banking"
    },
    {
        "name": "Bank Churners",
        "path": "bank_churners/BankChurners.csv",
        "industry": "Banking"
    }
]

print("="*100)
print("COMPREHENSIVE DATASET ANALYSIS FOR MILESTONE ONE")
print("="*100)

for i, dataset_info in enumerate(datasets, 1):
    file_path = os.path.join(DATA_DIR, dataset_info['path'])
    
    print(f"\n{'='*100}")
    print(f"DATASET {i}: {dataset_info['name']}")
    print(f"Industry: {dataset_info['industry']}")
    print(f"{'='*100}")
    
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        
        # Basic info
        print(f"\n📊 BASIC INFORMATION:")
        print(f"   Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"   Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        # Data types
        print(f"\n📋 DATA TYPES:")
        dtype_counts = df.dtypes.value_counts()
        for dtype, count in dtype_counts.items():
            print(f"   {dtype}: {count} columns")
        
        # Sample columns by type
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        string_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        print(f"\n   Numeric columns ({len(numeric_cols)}): {', '.join(numeric_cols[:5])}{'...' if len(numeric_cols) > 5 else ''}")
        print(f"   String/Object columns ({len(string_cols)}): {', '.join(string_cols[:5])}{'...' if len(string_cols) > 5 else ''}")
        
        # Missing values
        print(f"\n❓ MISSING VALUES:")
        missing = df.isnull().sum()
        missing_pct = (missing / len(df)) * 100
        has_missing = missing[missing > 0]
        
        if len(has_missing) > 0:
            print(f"   Total columns with missing values: {len(has_missing)}")
            print(f"   Top 5 columns with missing values:")
            for col in has_missing.head(5).index:
                print(f"      {col}: {missing[col]:,} ({missing_pct[col]:.2f}%)")
        else:
            print(f"   ✅ No missing values found")
        
        # Duplicates
        print(f"\n🔄 DUPLICATE ROWS:")
        duplicates = df.duplicated().sum()
        print(f"   Total duplicate rows: {duplicates:,} ({(duplicates/len(df)*100):.2f}%)")
        
        # Target variable (if identifiable)
        print(f"\n🎯 POTENTIAL TARGET VARIABLES:")
        potential_targets = []
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in ['class', 'label', 'target', 'flag', 'churn', 'fraud', 'distress', 'score', 'claim']):
                potential_targets.append(col)
                unique_vals = df[col].nunique()
                print(f"   {col}: {unique_vals} unique values")
                if unique_vals <= 10:
                    print(f"      Distribution: {df[col].value_counts().to_dict()}")
        
        # Sample data
        print(f"\n📝 SAMPLE COLUMNS (first 5):")
        for col in df.columns[:5]:
            print(f"   {col}: {df[col].dtype}")
            if df[col].dtype == 'object':
                print(f"      Sample values: {df[col].dropna().head(3).tolist()}")
            else:
                print(f"      Range: [{df[col].min():.2f}, {df[col].max():.2f}]")
        
        # Statistical summary for numeric columns
        print(f"\n📈 NUMERIC SUMMARY (first 3 numeric columns):")
        for col in numeric_cols[:3]:
            print(f"   {col}:")
            print(f"      Mean: {df[col].mean():.2f}, Std: {df[col].std():.2f}")
            print(f"      Min: {df[col].min():.2f}, Max: {df[col].max():.2f}")
        
    except Exception as e:
        print(f"   ❌ Error analyzing dataset: {str(e)}")

print(f"\n{'='*100}")
print("ANALYSIS COMPLETE")
print(f"{'='*100}")
