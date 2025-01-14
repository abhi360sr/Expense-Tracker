import datetime

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date
        
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, Expense):
        self.expenses.append(Expense)
        
    def display_total(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"Total Expense: {total}")
        
    def search_by_category(self):
        category = input("Enter the category to search: ")
        found = False
        for exp in self.expenses:
            if exp.category == category:
                print(f"Date: {exp.date}, Category: {exp.category}, Amount: {exp.amount}")
                found = True
        if not found:
            print(f"No expenses found for category: {category}")
    
    def filter_by_date(self):
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            found = False
            for exp in self.expenses:
                if exp.date == date:
                    print(f"Date: {exp.date}, Category: {exp.category}, Amount: {exp.amount}")
                    found = True
            if not found:
                print(f"No expenses found for the date: {date}")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    def calculate_total_by_date(self):
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            total = sum(exp.amount for exp in self.expenses if exp.date == date)
            print(f"Total Expense on {date}: {total}")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def create_expense(tracker):
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        expense = Expense(category, amount, date)
        tracker.add_expense(expense)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense")
        print("2. Search by Category")
        print("3. Filter by Date")
        print("4. Calculate Total by Date")
        print("5. Display Total Expense")
        print("6. Exit")
        option = int(input("Select an option: "))
        
        if option == 1:
            create_expense(tracker)
        elif option == 2:
            tracker.search_by_category()
        elif option == 3:
            tracker.filter_by_date()
        elif option == 4:
            tracker.calculate_total_by_date()
        elif option == 5:
            tracker.display_total()
        elif option == 6:
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
