#!/usr/bin/env python3
"""
Generate dataset samples for Milestone One Appendix.
Creates formatted output showing key columns and sample data.
"""

import pandas as pd
import os

DATA_DIR = "/Users/gaurav/workspace/datascience/boston_university/ms_datascience/week_10122025/AI_leaders/data"

print("="*100)
print("DATASET SAMPLES FOR APPENDIX")
print("="*100)

# Dataset 1: Credit Card Fraud
print("\n" + "="*100)
print("DATASET 1: CREDIT CARD FRAUD DETECTION")
print("="*100)
df1 = pd.read_csv(f"{DATA_DIR}/credit_card_fraud_detection/creditcard.csv")
print(f"\nShape: {df1.shape[0]:,} rows × {df1.shape[1]} columns")
print(f"\nKey Columns Sample (first 5 rows, selected columns):")
print(df1[['Time', 'V1', 'V2', 'V3', 'Amount', 'Class']].head())
print(f"\nTarget Distribution:")
print(df1['Class'].value_counts())
print(f"Fraud Rate: {(df1['Class'].sum() / len(df1) * 100):.3f}%")

# Dataset 2: Financial Distress
print("\n" + "="*100)
print("DATASET 2: FINANCIAL DISTRESS PREDICTION")
print("="*100)
df2 = pd.read_csv(f"{DATA_DIR}/financial_distress_prediction/Financial Distress.csv")
print(f"\nShape: {df2.shape[0]:,} rows × {df2.shape[1]} columns")
print(f"\nKey Columns Sample (first 5 rows, selected columns):")
print(df2[['Company', 'Time', 'Financial Distress', 'x1', 'x2', 'x3']].head())
print(f"\nFinancial Distress Statistics:")
print(df2['Financial Distress'].describe())

# Dataset 3: Insurance Claims
print("\n" + "="*100)
print("DATASET 3: INSURANCE CLAIMS")
print("="*100)
df3 = pd.read_csv(f"{DATA_DIR}/insurance_claims_dataset/car_insurance_claim.csv")
print(f"\nShape: {df3.shape[0]:,} rows × {df3.shape[1]} columns")
print(f"\nKey Columns Sample (first 5 rows, selected columns):")
print(df3[['AGE', 'INCOME', 'EDUCATION', 'OCCUPATION', 'CAR_TYPE', 'CLAIM_FLAG', 'CLM_AMT']].head())
print(f"\n⚠️ Missing Values in Sample Columns:")
missing = df3[['AGE', 'INCOME', 'OCCUPATION']].isnull().sum()
print(missing[missing > 0])
print(f"\nTarget Distribution (CLAIM_FLAG):")
print(df3['CLAIM_FLAG'].value_counts())

# Dataset 4: Credit Score Classification
print("\n" + "="*100)
print("DATASET 4: CREDIT SCORE CLASSIFICATION")
print("="*100)
df4 = pd.read_csv(f"{DATA_DIR}/credit_score_classification/train.csv", low_memory=False)
print(f"\nShape: {df4.shape[0]:,} rows × {df4.shape[1]} columns")
print(f"\nKey Columns Sample (first 5 rows, selected columns):")
print(df4[['Age', 'Occupation', 'Annual_Income', 'Monthly_Inhand_Salary', 
           'Num_Bank_Accounts', 'Num_Credit_Card', 'Credit_Score']].head())
print(f"\n⚠️ Missing Values in Sample Columns:")
missing = df4[['Monthly_Inhand_Salary', 'Num_of_Delayed_Payment', 'Type_of_Loan']].isnull().sum()
print(missing[missing > 0])
print(f"\n⚠️ Data Quality Issue - Age Column:")
print(f"Sample Age values: {df4['Age'].head(10).tolist()}")
print(f"Note: Age contains string values and errors (e.g., negative numbers)")
print(f"\nTarget Distribution (Credit_Score):")
print(df4['Credit_Score'].value_counts())

# Dataset 5: Bank Churners
print("\n" + "="*100)
print("DATASET 5: BANK CHURNERS")
print("="*100)
df5 = pd.read_csv(f"{DATA_DIR}/bank_churners/BankChurners.csv")
print(f"\nShape: {df5.shape[0]:,} rows × {df5.shape[1]} columns")
print(f"\nKey Columns Sample (first 5 rows, selected columns):")
print(df5[['Customer_Age', 'Gender', 'Education_Level', 'Marital_Status', 
           'Income_Category', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Attrition_Flag']].head())
print(f"\nTarget Distribution (Attrition_Flag):")
print(df5['Attrition_Flag'].value_counts())
print(f"Churn Rate: {(df5['Attrition_Flag'] == 'Attrited Customer').sum() / len(df5) * 100:.2f}%")

print("\n" + "="*100)
print("APPENDIX SAMPLES COMPLETE")
print("="*100)
print("\nNote: Use these samples in your appendix (max 1 page)")
print("Format as tables in Word document with proper captions")
