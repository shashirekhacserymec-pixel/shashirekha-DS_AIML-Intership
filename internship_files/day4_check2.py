
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
is_present = "ID05" in unique_users
original_count = len(raw_logs)
unique_count = len(unique_users)
print("Unique User IDs:", unique_users)
print("Is ID05 present?", is_present)
print("Total log entries:", original_count)
print("Unique visitors:", unique_count)
