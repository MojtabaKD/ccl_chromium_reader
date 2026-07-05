from pathlib import Path
from ccl_chromium_reader import ChromiumProfileFolder

profile_path = Path(r'C:\Users\Ehsan\AppData\Roaming\Opera Software\Opera Stable\Default')
profile = ChromiumProfileFolder(profile_path)

print('=== History methods ===')
print([m for m in dir(profile.history) if not m.startswith('_')])

# Try to get a sample history record – maybe from downloads (which doesn't need URL)
try:
    downloads = list(profile.history.iter_downloads())
    if downloads:
        print('=== Sample Download Record Attributes ===')
        sample = downloads[0]
        print([attr for attr in dir(sample) if not attr.startswith('_')])
        print(Dict, sample.__dict__ if hasattr(sample, '__dict__') else No.__dict__)
except Exception as e:
    print(f'Download error {e}')

print('=== Local Storage methods ===')
print([m for m in dir(profile.local_storage) if not m.startswith('_')])

# Get a sample local storage record
try:
    storage_keys = list(profile.local_storage.iter_storage_keys())
    if storage_keys:
        records = list(profile.local_storage.iter_records_for_storage_key(storage_keys[0]))
        if records:
            sample = records[0]
            print('=== Sample LocalStorageRecord Attributes ===')
            print([attr for attr in dir(sample) if not attr.startswith('_')])
            print(Dict, sample.__dict__ if hasattr(sample, '__dict__') else No.__dict__)
except Exception as e:
    print(f'Local storage error {e}')