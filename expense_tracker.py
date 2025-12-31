from datetime import datetime

FILE_NAME = "expense_tracker.txt"

def show_menu():
    print("\nWelcome to Expense Tracker")
    print("1. Add expense")
    print("2. View total expenses")
    print("3. View expenses by date")
    print("4. Exit")

def add_expense():
    while True:
        amount_input = input("Enter expense amount (or type '0' to return): ").strip()
        
        if amount_input == "0":
            print("Returning to main menu...")
            return  # go back immediately

        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount cannot be zero or negative. Returning to main menu.")
                return  # go back if invalid
            break
        except ValueError:
            print("Invalid amount. Enter numbers only.")

    # Validate category
    while True:
        category = input("Enter expense category (or type '0' to return): ").strip()
        if category <= "0":
            print("Returning to main menu...")
            return
        if category:
            break
        print("Category cannot be empty.")

    # Save to file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a") as file:
        file.write(f"{timestamp}, {amount}, {category}\n")

    print("Expense saved!")



def view_total():
    total = 0.0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                _, amount, _ = parts
                try:
                    total += float(amount)
                except ValueError:
                    continue
        print(f"Total expenses: {total:.2f}")
    except FileNotFoundError:
        print("No expenses found yet.")

def view_expense_by_date():
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    total = 0.0
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                timestamp, amount, category = parts
                entry_date = timestamp[:10]
                if entry_date == date_input:
                    print(f"{timestamp} | {category} | {float(amount):.2f}")
                    total += float(amount)
                    found = True

        if found:
            print(f"\nTotal expenses for {date_input}: {total:.2f}")
        else:
            print(f"No expenses found for {date_input}.")

    except FileNotFoundError:
        print("No expenses file found.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            view_expense_by_date()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
