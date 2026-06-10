expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def show_expenses():
    for e in expenses:
        print(f"{e['category']}: ₹{e['amount']}")

def total_spending():
    total = sum(e['amount'] for e in expenses)
    print(f"Total Spending: ₹{total}")

# Example usage
add_expense(200, "Food")
add_expense(500, "Books")
show_expenses()
total_spending()
