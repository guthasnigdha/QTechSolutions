import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date):
        self.expenses.append({"amount": amount, "category": category, "date": date})
        print(f"Expense added: {amount} in {category} on {date}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nDetailed Expenses:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['date']} - {expense['category']}: ${expense['amount']}")

    def monthly_summary(self):
        summary = {}
        for expense in self.expenses:
            month = expense["date"][:7]  # Extract year and month (YYYY-MM)
            if month not in summary:
                summary[month] = {}
            if expense["category"] not in summary[month]:
                summary[month][expense["category"]] = 0
            summary[month][expense["category"]] += expense["amount"]

        if not summary:
            print("No expenses to summarize.")
            return

        print("\nMonthly Summary:")
        for month, categories in summary.items():
            print(f"{month}:")
            for category, total in categories.items():
                print(f"  {category}: ${total}")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                date = input("Enter date (YYYY-MM-DD): ")
                tracker.add_expense(amount, category, date)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.monthly_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
