# to create a application to track the expenses of a person
import json
import os
from textwrap import indent
import time


class expense_tracker:
    def __init__(self, filename = 'Exp.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as fp:
                expense_file = json.load(fp)
                return expense_file
        return []

    def save_expenses(self):
        with open(self.filename,'w') as fp:
            json.dump(self.expenses, fp, indent=4)

    def add_expense(self,description,amount):
        expense = {"Description": description, "Amount": amount}
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded")
            return
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp['Description']} : ${exp['Amount']}")

    def delete_expense(self, index):
        if 0<= index <= len(self.expenses):
            groc = self.expenses[index-1]

            self.expenses.pop(index-1)
            self.save_expenses()
            print(f"{groc['Description']} Expenses deleted")
        else:
            print("Invalid Index.")

    def total_expenses(self):
        try:
            total = 0
            for exp in self.expenses:
                if exp['Amount'] == int(exp['Amount']) or float(exp['Amount']):
                    total += exp['Amount']
            print(f"\tTotal amount spent is ${total}")
        except (ValueError,NameError):
            print("Invalid Sum, Total Contains str's")

def main():
    tracker = expense_tracker()
    while True:
        print("=" * 60)
        print("\t\t\tExpense Tracker")
        print("=" * 60)
        print("\t1. Add Expense")
        print("\t2. View Expense")
        print("\t3. Total Expenses")
        print("\t4. Delete Expense")
        print("\t5. Exit")
        print("=" * 60)

        # creating the match statement for choosing the option
        try:
            choice = int(input("Choose the choice from the menu: "))
        except (ValueError,NameError):
            print("\tEnter Only integers as choice")

        print("=" * 60)
        match(choice):
            case 1:
                try:
                    Description = input("Enter the Description: ")
                    Amount = float(input("Enter the Amount: "))
                    tracker.add_expense(Description,Amount)
                except (ValueError,NameError):
                    print("="*60)
                    print("\tEnter inputs accordingly")
            case 2:
                tracker.view_expenses()
            case 3:
                tracker.total_expenses()
            case 4:
                try:
                    tracker.view_expenses()
                    print("="*60)
                    index = int(input("Enter the index which want to be delete: "))
                    tracker.delete_expense(index)
                except ValueError:
                    print("Enter only +ve numerics")
            case 5:
                print("\tThank You for using this tracker-Get Lost now")
                print("=" * 60)
                et = time.time()
                print('total time: ', et - st)
                exit()
            case _:
                print("Invalid Choice, Please enter choice from the Menu...!")

# Main Program
if __name__ == "__main__":
    st = time.time()
    main()