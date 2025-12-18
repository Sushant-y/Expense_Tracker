while True:
    print("\nWelcome to Expense Tracker")
    print("1. Add expense")
    print("2. View total expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = input("Enter expense amount: ")
        category = input("Enter expense category: ")

        with open("expenses.txt", "a") as file:
            file.write(amount + "," + category + "\n")

        print("Expense saved!")

    elif choice == "2":
        total = 0

        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")

                    # skip bad or old lines
                    if len(parts) != 2:
                        continue

                    amount, category = parts

                    try:
                        total += float(amount)
                    except ValueError:
                        continue

            print(f"Total expenses: {total:.2f}")

        except FileNotFoundError:
            print("No expenses found yet.")

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice. Please try again.")
