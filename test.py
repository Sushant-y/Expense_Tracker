import os
from datetime import datetime, timedelta
import shutil

# === CONFIGURATION ===
TEST_FILE = "expense_tracker_test.txt"

# Backup real file if it exists
if os.path.exists("expense_tracker.txt"):
    shutil.copy("expense_tracker.txt", "expense_tracker_backup.txt")

# Ensure test file is clean
if os.path.exists(TEST_FILE):
    os.remove(TEST_FILE)

# === HELPER FUNCTIONS ===
def write_expense(file, timestamp, amount, category):
    with open(file, "a") as f:
        f.write(f"{timestamp}, {amount}, {category}\n")

def view_total(file):
    total = 0.0
    try:
        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                _, amount, _ = parts
                try:
                    total += float(amount)
                except ValueError:
                    continue
        return total
    except FileNotFoundError:
        return None

def view_by_date(file, date_str):
    entries = []
    total = 0.0
    try:
        with open(file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                timestamp, amount, category = parts
                if timestamp[:10] == date_str:
                    entries.append((timestamp, category, float(amount)))
                    total += float(amount)
        return entries, total
    except FileNotFoundError:
        return None, 0.0

# === TEST CASES ===

# 1. Add sample expenses
today = datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

write_expense(TEST_FILE, f"{today} 10:00:00", 250, "Food")
write_expense(TEST_FILE, f"{today} 12:30:00", 123.45, "Travel")
write_expense(TEST_FILE, f"{yesterday} 09:00:00", 50, "Snacks")
write_expense(TEST_FILE, f"{yesterday} 18:15:00", 75.55, "Transport")

# 2. Add corrupted lines
write_expense(TEST_FILE, "invalid_line_without_commas", "", "")
write_expense(TEST_FILE, f"{today} 15:00:00, abc, InvalidAmount", "", "")

# === TEST TOTAL ===
total = view_total(TEST_FILE)
assert abs(total - (250 + 123.45 + 50 + 75.55)) < 0.01, f"Total calculation failed: {total}"
print(f"[PASS] Total expenses test: {total:.2f}")

# === TEST VIEW BY DATE ===
entries_today, total_today = view_by_date(TEST_FILE, today)
assert len(entries_today) == 2, f"Expected 2 entries for today, got {len(entries_today)}"
assert abs(total_today - (250 + 123.45)) < 0.01, f"Today's total incorrect: {total_today}"
print(f"[PASS] View by date ({today}) test: {total_today:.2f}")

entries_yesterday, total_yesterday = view_by_date(TEST_FILE, yesterday)
assert len(entries_yesterday) == 2, f"Expected 2 entries for yesterday, got {len(entries_yesterday)}"
assert abs(total_yesterday - (50 + 75.55)) < 0.01, f"Yesterday's total incorrect: {total_yesterday}"
print(f"[PASS] View by date ({yesterday}) test: {total_yesterday:.2f}")

# === TEST EMPTY FILE ===
empty_file = "empty_test.txt"
if os.path.exists(empty_file):
    os.remove(empty_file)
total_empty = view_total(empty_file)
assert total_empty is None, f"Empty file total test failed: {total_empty}"
entries_empty, total_empty_date = view_by_date(empty_file, today)
assert entries_empty is None and total_empty_date == 0.0, f"Empty file view by date failed"
print("[PASS] Empty file tests")

# === CLEANUP ===
os.remove(TEST_FILE)
print("\nAll tests passed successfully!")

# Restore original file if it existed
if os.path.exists("expense_tracker_backup.txt"):
    shutil.move("expense_tracker_backup.txt", "expense_tracker.txt")
