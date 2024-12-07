# Bank Account Class:
#
# Define a class BankAccount with attributes for account holder name and balance.
# Implement methods for depositing, withdrawing, and checking the balance.
# Ensure the balance does not go negative.
import re
def account():
    while True:
        try:
            number = int(input("Enter the Account number (5-7) digits: "))
            pattern = r"^\d{5,7}$"
            if re.match(pattern,str(number)):
                return number
                break
            else:
                print("\tEnter valid account number")
        except (ValueError,NameError):
            print("\tPlease enter valid number(only digits)")
def name():
    while True:
        try:
            name = input("Enter the account holder name: ").title()
            pattern = r"^[A-Za-z]+(?:\s[A-Za-z]+)*$"
            if re.match(pattern,name):
                return name
                break
            else:
                print("\tPlease enter valid name")
        except (ValueError,NameError):
            print("\tPlease enter only alphabets")
def balance():
    while True:
        try:
            total_balance = int(input("Enter the Account balance(0-7) digits: "))
            pattern = r"^\d{0,7}$"
            if re.match(pattern,str(total_balance)):
                return float(total_balance)
                break
            else:
                print("\tEnter valid account amount")
        except (ValueError,NameError):
            print("\tPlease enter valid amount(only digits)")

class BankAccount:
    def account_details(self):
        self.acc_number = account()
        self.acc_name = name()
        self.acc_balance = balance()
    def display_account_details(self):
        print(f"Account holder details are {self.__dict__}")
        print("=" * 50)
        print("\t Account details ")
        print("=" * 50)
        for key,val in self.__dict__.items():
            print("\t\t{} :- {}".format(key,val))
        print("=" * 50)

# Main Program

bankaccount = BankAccount()
bankaccount.account_details()
bankaccount.display_account_details()