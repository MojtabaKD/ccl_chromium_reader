from pathlib import Path
from ccl_chromium_reader import ChromiumProfileFolder

profile_path = Path(r'C:\Users\<username>\AppData\Roaming\Opera Software\Opera Stable\Default')
profile = ChromiumProfileFolder(profile_path)

# -----------------------------------------------------------------
# 1. DOWNLOADS
# -----------------------------------------------------------------
print("=" * 60)
print("DOWNLOADS")
print("=" * 60)

try:
    for dl in profile.history.iter_downloads():
        print(f"URL: {dl.url}")
        print(f"File: {dl.target_path}")
        print(f"Size: {dl.file_size} bytes")
        print(f"Start: {dl.start_time}")
        print(f"End: {dl.end_time}")
        print("-" * 40)
except Exception as e:
    print(f"Error: {e}")

# -----------------------------------------------------------------
# 2. LOCAL STORAGE
# -----------------------------------------------------------------
print("\n" + "=" * 60)
print("LOCAL STORAGE")
print("=" * 60)

try:
    for storage_key in profile.local_storage.iter_storage_keys():
        print(f"\nStorage Key: {storage_key}")
        print("-" * 30)
        for record in profile.local_storage.iter_records_for_storage_key(storage_key):
            value = record.value[:200] + "..." if len(record.value) > 200 else record.value
            print(f"  {record.script_key} = {value}")
except Exception as e:
    print(f"Error: {e}")

# -----------------------------------------------------------------
# 3. SESSION STORAGE
# -----------------------------------------------------------------
print("\n" + "=" * 60)
print("SESSION STORAGE")
print("=" * 60)

try:
    for storage_key in profile.session_storage.iter_storage_keys():
        print(f"\nStorage Key: {storage_key}")
        print("-" * 30)
        for record in profile.session_storage.iter_records_for_storage_key(storage_key):
            value = record.value[:200] + "..." if len(record.value) > 200 else record.value
            print(f"  {record.script_key} = {value}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 60)
print("Note: For browsing history, use the SQLite script separately.")
print("=" * 60)