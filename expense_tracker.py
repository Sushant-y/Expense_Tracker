FILE_NAME = "expense_tracker.txt"


def show_menu():
    print("\nWelcome to Expense Tracker")
    print("1. Add expense")
    print("2. View total expenses")
    print("3. Exit")


def add_expense():
    # Validate amount
    while True:
        amount = input("Enter expense amount: ")

        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid amount. Enter numbers only.")

    # Validate category
    while True:
        category = input("Enter expense category: ").strip()

        if category:
            break
        else:
            print("Category cannot be empty. Please enter a valid category.")

    # Save to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category}\n")

    print("Expense saved!")



def view_total():
    total = 0.0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 2:
                    continue

                amount, _ = parts

                try:
                    total += float(amount)
                except ValueError:
                    continue

        print(f"Total expenses: {total:.2f}")

    except FileNotFoundError:
        print("No expenses found yet.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

