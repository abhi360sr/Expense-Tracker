
This is a Python-based Expense Tracker application that helps users manage and track their expenses. Users can add expenses, view total expenses, filter expenses by category or date, and calculate the total expenses for a specific date. The program is interactive and runs via a command-line interface.

Features
Add Expense: Add a new expense with category, amount, and date.
Search by Category: Retrieve and display expenses for a specific category.
Filter by Date: Retrieve and display expenses for a specific date.
Calculate Total by Date: Calculate the total expense for a specific date.
Display Total Expense: Display the total of all recorded expenses.
Exit: Exit the application.
Requirements
Python 3.6 or later
No additional external libraries required
How to Use
Run the Application: Execute the program using:

bash
Copy code
python expense_tracker.py
Main Menu Options:

1. Add Expense: Input the category, amount, and date (in YYYY-MM-DD format) to add an expense.
2. Search by Category: Enter a category to view all expenses under it.
3. Filter by Date: Enter a date (YYYY-MM-DD) to view all expenses recorded on that date.
4. Calculate Total by Date: Enter a date (YYYY-MM-DD) to calculate the total expense for that date.
5. Display Total Expense: View the sum of all recorded expenses.
6. Exit: Close the application.
Code Explanation
Classes:

Expense: Represents an individual expense with attributes category, amount, and date.
ExpenseTracker: Manages a list of Expense objects and provides methods to interact with them.
Core Methods:

add_expense(Expense): Adds a new expense to the tracker.
display_total(): Prints the total of all expenses.
search_by_category(): Searches for expenses by category and displays matching entries.
filter_by_date(): Filters and displays expenses for a specific date.
calculate_total_by_date(): Calculates and prints the total expense for a specific date.
Interactive Menu:

The main() function provides a command-line menu for user interaction.
Sample Usage
text
Copy code
1. Add Expense
2. Search by Category
3. Filter by Date
4. Calculate Total by Date
5. Display Total Expense
6. Exit
Select an option: 1
Enter category: Food
Enter amount: 250
Enter date (YYYY-MM-DD): 2025-01-10

Expense added successfully!
Future Enhancements
Add a graphical user interface (GUI).
Include export/import functionality (e.g., save data to a file or database).
Add expense categories and amounts validation.
Generate reports based on time periods.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

Author
Abhishek SR
Enjoy tracking your expenses efficiently! 🎉
