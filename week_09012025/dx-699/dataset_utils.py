"""
Utility functions for loading and caching UCI ML Repository datasets.

This module provides functions to download and cache ANY UCI ML Repository
dataset locally, avoiding repeated API calls and handling network/SSL issues.

Main Functions:
    - load_uci_dataset(): Load any UCI dataset by ID (PRIMARY FUNCTION)
    - load_mushroom_dataset(): Convenience wrapper for Mushroom dataset (ID: 73)
    - clear_cache(): Clear cached datasets

Key Features:
    - Works with ANY UCI ML Repository dataset (not just Mushroom)
    - Automatic caching (download once, use forever)
    - Handles SSL issues automatically
    - Works offline once cached
    - Fast loading from cache

Example:
    >>> from dataset_utils import load_uci_dataset
    >>> 
    >>> # Load Mushroom dataset (ID: 73)
    >>> dataset = load_uci_dataset(73)
    >>> 
    >>> # Load Iris dataset (ID: 53)
    >>> iris = load_uci_dataset(53)
    >>> 
    >>> # Load Wine dataset (ID: 109)
    >>> wine = load_uci_dataset(109)
"""

import os
import ssl
import urllib.request
from pathlib import Path
from typing import Optional

# Import pickle - ensure we get the standard library version
# This handles cases where pickle might be overwritten in the namespace
try:
    import pickle
    # Verify pickle functions exist and are callable
    if not hasattr(pickle, 'dump') or pickle.dump is None:
        import importlib
        import sys
        # Force reload pickle from standard library
        if 'pickle' in sys.modules:
            del sys.modules['pickle']
        import pickle
except Exception:
    # Fallback: import directly
    import pickle

try:
    from ucimlrepo import fetch_ucirepo
except ImportError:
    fetch_ucirepo = None


def _get_cache_dir():
    """Get the cache directory for storing datasets."""
    cache_dir = Path(__file__).parent / "dataset_cache"
    cache_dir.mkdir(exist_ok=True)
    return cache_dir


def _get_cache_path(dataset_id: int) -> Path:
    """Get the cache file path for a given dataset ID."""
    cache_dir = _get_cache_dir()
    return cache_dir / f"dataset_{dataset_id}.pkl"


def _setup_ssl_context():
    """Create an unverified SSL context for environments with SSL issues."""
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context


# Store the original urlopen function to avoid recursion
_original_urlopen = None
_urlopen_patched = False


def _patch_urlopen_for_ssl():
    """Monkey patch urllib to use unverified SSL context."""
    global _original_urlopen, _urlopen_patched
    
    # Only patch once
    if not _urlopen_patched:
        # Get the original urlopen function
        # If it's already been patched (by us or someone else), we need to be careful
        current_urlopen = urllib.request.urlopen
        
        # Store the current as original (before we patch)
        # If this module was reloaded, current_urlopen might already be patched
        # In that case, the user should restart the kernel for best results
        _original_urlopen = current_urlopen
        
        # Create the patch function with a closure that captures the original
        # This ensures we always call the true original, not a patched version
        original_func = _original_urlopen
        
        def urlopen_patch(*args, **kwargs):
            # Always override the context to use unverified SSL
            # This handles cases where the caller provides their own context (like certifi)
            kwargs['context'] = _setup_ssl_context()
            # Call the original function captured in the closure
            return original_func(*args, **kwargs)
        
        # Apply the patch
        urllib.request.urlopen = urlopen_patch
        _urlopen_patched = True


def load_mushroom_dataset(force_download: bool = False, use_ssl_patch: bool = True):
    """
    Convenience function to load the Mushroom dataset (UCI ID: 73).
    
    This is a convenience wrapper around load_uci_dataset() specifically for
    the Mushroom dataset. For other datasets, use load_uci_dataset() directly.
    
    Parameters
    ----------
    force_download : bool, default=False
        If True, force re-download even if cache exists.
    use_ssl_patch : bool, default=True
        If True, apply SSL context patch for environments with SSL issues.
        Set to False if you have proper SSL certificates.
    
    Returns
    -------
    dict
        Dictionary containing:
        - 'data': Dict with 'features' and 'targets' DataFrames
        - 'metadata': Dataset metadata
        - 'variables': Variable information DataFrame
    
    Examples
    --------
    >>> dataset = load_mushroom_dataset()
    >>> X = dataset['data']['features']
    >>> y = dataset['data']['targets']
    >>> metadata = dataset['metadata']
    
    Notes
    -----
    - This is equivalent to: load_uci_dataset(73, force_download, use_ssl_patch)
    - The dataset is cached in a 'dataset_cache' directory
    - Once cached, loads instantly without network access
    
    See Also
    --------
    load_uci_dataset : Generic function to load any UCI dataset
    """
    return load_uci_dataset(dataset_id=73, force_download=force_download, 
                           use_ssl_patch=use_ssl_patch)


def load_uci_dataset(dataset_id: int, force_download: bool = False, 
                     use_ssl_patch: bool = True, cache_name: Optional[str] = None):
    """
    Load any UCI ML Repository dataset with automatic caching.
    
    This is the primary function for loading UCI datasets. It automatically:
    - Checks for cached version first (fast, no network needed)
    - Downloads from UCI ML Repository if cache doesn't exist
    - Handles SSL issues automatically
    - Caches the dataset for future use
    
    Parameters
    ----------
    dataset_id : int
        The UCI ML Repository dataset ID. Common examples:
        - 73: Mushroom dataset
        - 1: Abalone dataset
        - 2: Adult dataset
        - 53: Iris dataset
        - 109: Wine dataset
        Find more at: https://archive.ics.uci.edu/datasets
    
    force_download : bool, default=False
        If True, force re-download even if cache exists.
        Useful when you want to update to the latest version.
    
    use_ssl_patch : bool, default=True
        If True, apply SSL context patch for environments with SSL issues
        (common in office networks). Set to False if you have proper SSL certificates.
    
    cache_name : str, optional
        Custom name for cache file. If None, uses 'dataset_{dataset_id}.pkl'
        Useful when you want to cache multiple versions of the same dataset.
    
    Returns
    -------
    dict
        Dictionary containing:
        - 'data': Dict with 'features' and 'targets' DataFrames
        - 'metadata': Dataset metadata (dict with info about the dataset)
        - 'variables': DataFrame with variable information
    
    Examples
    --------
    >>> # Load Mushroom dataset (ID: 73)
    >>> dataset = load_uci_dataset(73)
    >>> X = dataset['data']['features']
    >>> y = dataset['data']['targets']
    >>> print(dataset['metadata']['name'])
    
    >>> # Load Iris dataset (ID: 53)
    >>> iris = load_uci_dataset(53)
    >>> X_iris = iris['data']['features']
    >>> y_iris = iris['data']['targets']
    
    >>> # Force re-download
    >>> dataset = load_uci_dataset(73, force_download=True)
    
    >>> # Load with custom cache name
    >>> dataset = load_uci_dataset(73, cache_name='mushroom_v2')
    
    Notes
    -----
    - The dataset is cached in a 'dataset_cache' directory next to this file
    - Cache file format: pickle (.pkl)
    - Once cached, the dataset loads instantly without network access
    - If download fails but cache exists, automatically falls back to cache
    - Works offline once dataset is cached
    
    See Also
    --------
    load_mushroom_dataset : Convenience function for mushroom dataset (ID: 73)
    clear_cache : Clear cached datasets
    """
    if cache_name is None:
        cache_path = _get_cache_path(dataset_id)
    else:
        cache_dir = _get_cache_dir()
        cache_path = cache_dir / f"{cache_name}.pkl"
    
    # Check if cache exists
    if cache_path.exists() and not force_download:
        # Check if file is empty or too small (likely corrupted)
        if cache_path.stat().st_size == 0:
            print(f"Warning: Cache file is empty. Deleting and re-downloading...")
            cache_path.unlink()
        else:
            print(f"Loading dataset {dataset_id} from cache: {cache_path}")
            try:
                with open(cache_path, 'rb') as f:
                    return pickle.load(f)
            except (EOFError, pickle.UnpicklingError, Exception) as e:
                # Cache file is corrupted or incomplete
                print(f"Warning: Cache file is corrupted or incomplete. Error: {e}")
                print(f"Deleting corrupted cache file and re-downloading...")
                cache_path.unlink()  # Delete corrupted cache file
                # Fall through to download section
    
    # Download from API
    if fetch_ucirepo is None:
        raise ImportError(
            "ucimlrepo package is not installed. "
            "Install it with: pip install ucimlrepo"
        )
    
    print(f"Downloading dataset (ID: {dataset_id}) from UCI ML Repository...")
    
    # Apply SSL patch if requested
    if use_ssl_patch:
        _patch_urlopen_for_ssl()
    
    try:
        # Fetch the dataset
        dataset = fetch_ucirepo(id=dataset_id)
        
        # Extract data for caching
        dataset_dict = {
            'data': {
                'features': dataset.data.features,
                'targets': dataset.data.targets
            },
            'metadata': dataset.metadata,
            'variables': dataset.variables
        }
        
        # Save to cache
        print(f"Saving dataset to cache: {cache_path}")
        try:
            with open(cache_path, 'wb') as f:
                pickle.dump(dataset_dict, f)
            print("Dataset downloaded and cached successfully!")
        except Exception as save_error:
            # If saving fails, still return the data but warn about cache
            print(f"Warning: Failed to save cache. Error: {save_error}")
            print("Dataset loaded successfully, but not cached.")
        
        return dataset_dict
        
    except Exception as e:
        # Only try to load from cache if it exists AND the error wasn't a cache corruption issue
        if cache_path.exists():
            print(f"Download failed. Attempting to load from cache...")
            print(f"Download error: {e}")
            try:
                with open(cache_path, 'rb') as f:
                    cached_data = pickle.load(f)
                print("Successfully loaded from cache!")
                return cached_data
            except (EOFError, pickle.UnpicklingError, Exception) as load_error:
                # Cache is also corrupted, delete it and raise error
                print(f"Cache file is also corrupted. Error: {load_error}")
                print("Deleting corrupted cache file...")
                cache_path.unlink()
                raise RuntimeError(
                    f"Failed to download dataset and cache is corrupted. "
                    f"Download error: {e}, Cache error: {load_error}\n"
                    f"Try again with force_download=True or check your network connection."
                ) from e
        else:
            raise RuntimeError(
                f"Failed to download dataset and no cache exists. "
                f"Error: {e}\n"
                f"Try again with force_download=True or check your network connection."
            ) from e


def clear_cache(dataset_id: Optional[int] = None):
    """
    Clear cached dataset files.
    
    Parameters
    ----------
    dataset_id : int, optional
        If provided, clears only the cache for this dataset ID.
        If None, clears all cached datasets.
    """
    cache_dir = _get_cache_dir()
    
    if dataset_id is None:
        # Clear all cache files
        for cache_file in cache_dir.glob("*.pkl"):
            cache_file.unlink()
            print(f"Deleted: {cache_file}")
        print("All cache files cleared.")
    else:
        # Clear specific dataset cache
        cache_path = _get_cache_path(dataset_id)
        if cache_path.exists():
            cache_path.unlink()
            print(f"Deleted cache for dataset {dataset_id}: {cache_path}")
        else:
            print(f"No cache found for dataset {dataset_id}")


if __name__ == "__main__":
    # Example usage - showing it works with any dataset
    print("=" * 60)
    print("Example 1: Loading Mushroom dataset (ID: 73)")
    print("=" * 60)
    dataset = load_mushroom_dataset()
    print(f"Features shape: {dataset['data']['features'].shape}")
    print(f"Targets shape: {dataset['data']['targets'].shape}")
    print(f"Dataset name: {dataset['metadata'].get('name', 'Unknown')}")
    
    print("\n" + "=" * 60)
    print("Example 2: Using generic function for any dataset")
    print("=" * 60)
    print("You can load any UCI dataset by ID:")
    print("  - load_uci_dataset(73)  # Mushroom")
    print("  - load_uci_dataset(53)   # Iris")
    print("  - load_uci_dataset(109)  # Wine")
    print("  - load_uci_dataset(1)    # Abalone")
    print("\nFind more datasets at: https://archive.ics.uci.edu/datasets")
