#!/usr/bin/env python3
"""
Script to download Banking, Financial Services, and Insurance (BFSI) datasets from Kaggle.
All datasets have 20+ columns and are relevant to the BFSI industry.
"""

import os
import subprocess
import sys

# Target directory for datasets
DATA_DIR = "/Users/gaurav/workspace/datascience/boston_university/ms_datascience/week_10122025/AI_leaders/data"

# List of BFSI datasets with 20+ columns
DATASETS = [
    {
        "name": "Credit Card Fraud Detection",
        "kaggle_id": "mlg-ulb/creditcardfraud",
        "description": "Credit card transactions dataset with fraud labels (31 columns)",
        "industry": "Banking & Financial Services"
    },
    {
        "name": "Bank Marketing Dataset",
        "kaggle_id": "henriqueyamahata/bank-marketing",
        "description": "Bank marketing campaign data (21 columns)",
        "industry": "Banking"
    },
    {
        "name": "Financial Distress Prediction",
        "kaggle_id": "shebrahimi/financial-distress",
        "description": "Financial distress indicators for companies (86 columns)",
        "industry": "Financial Services"
    },
    {
        "name": "Insurance Claims Dataset",
        "kaggle_id": "xiaomengsun/car-insurance-claim-data",
        "description": "Car insurance claims data (27 columns)",
        "industry": "Insurance"
    },
    {
        "name": "Credit Score Classification",
        "kaggle_id": "parisrohan/credit-score-classification",
        "description": "Credit score classification with extensive features (28 columns)",
        "industry": "Banking & Consumer Finance"
    }
]

# Alternative datasets with guaranteed 20+ columns
ALTERNATIVE_DATASETS = [
    {
        "name": "Home Credit Default Risk",
        "kaggle_id": "c/home-credit-default-risk",
        "description": "Home credit default risk with extensive features (100+ columns)",
        "industry": "Banking & Credit"
    },
    {
        "name": "American Express Default Prediction",
        "kaggle_id": "c/amex-default-prediction",
        "description": "Credit default prediction (190+ columns)",
        "industry": "Financial Services"
    },
    {
        "name": "Santander Customer Transaction",
        "kaggle_id": "c/santander-customer-transaction-prediction",
        "description": "Bank customer transaction prediction (200 columns)",
        "industry": "Banking"
    },
    {
        "name": "Porto Seguro Safe Driver",
        "kaggle_id": "c/porto-seguro-safe-driver-prediction",
        "description": "Insurance driver safety prediction (59 columns)",
        "industry": "Insurance"
    },
    {
        "name": "IEEE Fraud Detection",
        "kaggle_id": "c/ieee-fraud-detection",
        "description": "Fraud detection for financial transactions (400+ columns)",
        "industry": "Financial Services"
    },
    {
        "name": "Credit Card Customers",
        "kaggle_id": "sakshigoyal7/credit-card-customers",
        "description": "Credit card customer churn prediction (23 columns)",
        "industry": "Banking"
    }
]

def check_kaggle_setup():
    """Check if Kaggle API is properly configured."""
    kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_json):
        print("❌ Kaggle API credentials not found!")
        print("\nTo set up Kaggle API:")
        print("1. Go to https://www.kaggle.com/account")
        print("2. Scroll to 'API' section and click 'Create New Token'")
        print("3. This will download kaggle.json")
        print("4. Run these commands:")
        print("   mkdir -p ~/.kaggle")
        print("   mv ~/Downloads/kaggle.json ~/.kaggle/")
        print("   chmod 600 ~/.kaggle/kaggle.json")
        return False
    return True

def download_dataset(dataset_info, index):
    """Download a single dataset from Kaggle."""
    print(f"\n{'='*80}")
    print(f"📊 Dataset {index + 1}: {dataset_info['name']}")
    print(f"Industry: {dataset_info['industry']}")
    print(f"Description: {dataset_info['description']}")
    print(f"Kaggle ID: {dataset_info['kaggle_id']}")
    print(f"{'='*80}")
    
    # Create subdirectory for this dataset
    dataset_name_clean = dataset_info['name'].lower().replace(' ', '_').replace('-', '_')
    dataset_dir = os.path.join(DATA_DIR, dataset_name_clean)
    os.makedirs(dataset_dir, exist_ok=True)
    
    try:
        # Download using Kaggle API
        cmd = f"kaggle datasets download -d {dataset_info['kaggle_id']} -p {dataset_dir} --unzip"
        
        # For competition datasets, use different command
        if dataset_info['kaggle_id'].startswith('c/'):
            competition_name = dataset_info['kaggle_id'][2:]  # Remove 'c/' prefix
            cmd = f"kaggle competitions download -c {competition_name} -p {dataset_dir}"
        
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Successfully downloaded to: {dataset_dir}")
            
            # Unzip if it's a competition dataset
            if dataset_info['kaggle_id'].startswith('c/'):
                print("Unzipping files...")
                subprocess.run(f"cd {dataset_dir} && unzip -o '*.zip' && rm *.zip", 
                             shell=True, capture_output=True)
            
            return True
        else:
            print(f"❌ Error downloading dataset:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Exception occurred: {str(e)}")
        return False

def main():
    """Main function to download all datasets."""
    print("🏦 BFSI Dataset Downloader")
    print("=" * 80)
    
    # Check Kaggle setup
    if not check_kaggle_setup():
        sys.exit(1)
    
    print(f"\n✅ Kaggle API is configured")
    print(f"📁 Target directory: {DATA_DIR}")
    
    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Download datasets
    successful = 0
    failed = []
    
    # Try primary datasets first
    datasets_to_try = DATASETS[:5]
    
    for i, dataset in enumerate(datasets_to_try):
        if download_dataset(dataset, i):
            successful += 1
        else:
            failed.append(dataset['name'])
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 DOWNLOAD SUMMARY")
    print("=" * 80)
    print(f"✅ Successfully downloaded: {successful}/{len(datasets_to_try)} datasets")
    if failed:
        print(f"❌ Failed: {', '.join(failed)}")
        print(f"\n💡 You can try alternative datasets from ALTERNATIVE_DATASETS list")
    print(f"\n📁 All datasets saved to: {DATA_DIR}")
    print("You can now explore these datasets for your analysis!")

if __name__ == "__main__":
    main()
