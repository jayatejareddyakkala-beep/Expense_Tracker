expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for e in expenses:
            print(f"{e['category']}: ₹{e['amount']}")

def total_spending():
    total = sum(e['amount'] for e in expenses)
    print(f"Total Spending: ₹{total}")

def save_expenses():
    with open("expenses.txt", "w") as f:
        for e in expenses:
            f.write(f"{e['category']},{e['amount']}\n")

def load_expenses():
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                category, amount = line.strip().split(",")
                expenses.append({"category": category, "amount": int(amount)})
    except FileNotFoundError:
        pass

def main():
    load_expenses()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Total Spending")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = int(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(amount, category)
            print("Expense added successfully!")
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            save_expenses()
            print("Expenses saved. Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
