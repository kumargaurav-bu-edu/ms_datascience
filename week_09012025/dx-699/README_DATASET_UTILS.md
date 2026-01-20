# Dataset Utility Functions

This module provides utilities for loading and caching **ANY** UCI ML Repository dataset, solving SSL issues and avoiding repeated API calls.

## Features

- **Works with ANY Dataset**: Not limited to Mushroom - works with all UCI ML Repository datasets
- **Automatic Caching**: Downloads dataset once and caches it locally
- **SSL Issue Handling**: Automatically handles SSL certificate issues in office networks
- **Offline Support**: Works offline once dataset is cached
- **Reusable**: Can be imported in any notebook

## Quick Start

### Primary Function: Load Any Dataset

```python
from dataset_utils import load_uci_dataset

# Load ANY UCI dataset by ID
# Mushroom dataset (ID: 73)
dataset = load_uci_dataset(73)

# Iris dataset (ID: 53)
iris = load_uci_dataset(53)

# Wine dataset (ID: 109)
wine = load_uci_dataset(109)

# Extract features and targets
X = dataset['data']['features']
y = dataset['data']['targets']
metadata = dataset['metadata']
variables = dataset['variables']
```

### Convenience Function: Mushroom Dataset

```python
from dataset_utils import load_mushroom_dataset

# Convenience function for Mushroom dataset (ID: 73)
# Equivalent to: load_uci_dataset(73)
dataset = load_mushroom_dataset()

# Extract features and targets
X = dataset['data']['features']
y = dataset['data']['targets']
metadata = dataset['metadata']
variables = dataset['variables']
```

### Force Re-download

```python
# Force re-download even if cache exists
dataset = load_mushroom_dataset(force_download=True)
```

### Disable SSL Patch

```python
# If you have proper SSL certificates, disable the patch
dataset = load_mushroom_dataset(use_ssl_patch=False)
```

## Cache Location

The cached datasets are stored in:
```
week_09012025/dx-699/dataset_cache/
```

Cache files are named: `dataset_{id}.pkl`

## Finding Dataset IDs

To find the ID for a dataset:
1. Visit https://archive.ics.uci.edu/datasets
2. Search for your dataset
3. The URL will contain the ID: `https://archive.ics.uci.edu/dataset/{ID}/dataset-name`

Common Dataset IDs:
- **73**: Mushroom
- **53**: Iris
- **109**: Wine
- **1**: Abalone
- **2**: Adult
- **146**: Car Evaluation

## Examples with Different Datasets

```python
from dataset_utils import load_uci_dataset

# Load Iris dataset
iris = load_uci_dataset(53)
X_iris = iris['data']['features']
y_iris = iris['data']['targets']

# Load Wine dataset
wine = load_uci_dataset(109)
X_wine = wine['data']['features']
y_wine = wine['data']['targets']

# Load Abalone dataset
abalone = load_uci_dataset(1)
X_abalone = abalone['data']['features']
y_abalone = abalone['data']['targets']
```

## Clearing Cache

```python
from dataset_utils import clear_cache

# Clear cache for mushroom dataset (ID: 73)
clear_cache(dataset_id=73)

# Clear all cached datasets
clear_cache()
```

## How It Works

1. **First Run**: 
   - Checks if cache exists → No
   - Downloads from UCI ML Repository API
   - Applies SSL patch if needed (for office networks)
   - Saves to cache file
   - Returns dataset

2. **Subsequent Runs**:
   - Checks if cache exists → Yes
   - Loads from cache (fast, no network needed)
   - Returns dataset

3. **Network Issues**:
   - If download fails but cache exists, loads from cache
   - If download fails and no cache, raises error

## Benefits

- ✅ **No SSL Issues**: Handles SSL certificate problems automatically
- ✅ **Faster Loading**: Cached datasets load instantly
- ✅ **Offline Work**: Work without internet once cached
- ✅ **Reusable**: Import in any notebook
- ✅ **Safe**: Falls back to cache if download fails

## Example: Using in Other Notebooks

```python
# In any notebook in the same directory or subdirectory
import sys
from pathlib import Path

# Add the directory containing dataset_utils to path
sys.path.insert(0, str(Path('/path/to/week_09012025/dx-699')))

# Import the generic function (works with any dataset)
from dataset_utils import load_uci_dataset

# Load any dataset by ID
dataset = load_uci_dataset(73)  # Mushroom
# dataset = load_uci_dataset(53)  # Iris
# dataset = load_uci_dataset(109)  # Wine

X = dataset['data']['features']
y = dataset['data']['targets']
metadata = dataset['metadata']
```

## Troubleshooting

### Import Error
If you get `ModuleNotFoundError: No module named 'dataset_utils'`:
- Make sure `dataset_utils.py` is in the same directory or in your Python path
- Use `sys.path.insert(0, '/path/to/dataset_utils')` to add it

### SSL Issues
- The utility automatically handles SSL issues by default
- If you still have problems, try `use_ssl_patch=True` explicitly

### Cache Not Working
- Check if `dataset_cache` directory exists and has write permissions
- Try `force_download=True` to re-download
