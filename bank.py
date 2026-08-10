from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def display(self):
        pass

class BankAccount(Person):
    total_account = 0
    def __init__(self, account_number, balance):
        super().__init__(self.name)
        self.account_number = account_number
        self.__balance = balance
        BankAccount.total_account +=1 

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid Deposit Amount.")
        

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited Successfully.")
        print("Current Balance =", self.__balance)
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance.")
        else:
            self.__balance -= amount
            print("Withdrawal Successful.")
            print("Current Balance =", self.__balance)

    def check_balance(self):
        print("Current Balance =", self.__balance)

    def account_details(self):
        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Holder :", self.name)
        print("Account Number :", self.account_number)
        print("Balance        :", self.__balance)
    @staticmethod
    def bankrules(self):
        print("BankRules:")
        print("Minimum Balance : 1000")
        print("Working days : Mon - fri")
        print("Bank Hours : 10 -5")
        print("Interest : 5%")

    @classmethod
    def show_total(cls):
        print("Total Account :",cls.total_account)

class SavingsAccount(BankAccount):

    def __init__(self, name, account_number, balance):
        super().__init__(name, account_number, balance)

    def account_details(self):
        return super().display_details()


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
       name = input("Enter Account Holder Name: ")
       acc_no = int(input("Enter Account Number: "))
       balance = float(input("Enter Initial Balance: "))
       account = SavingsAccount(name, acc_no, balance)

       self.accounts[acc_no] = account
       print("Account is created succesfully")

    def search(self):
        account_no = int(input("Enter Account Number:"))
        if account_no in self.accounts:
            

while True:

    print("\n========== BANK MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Add Interest")
    print("5. Account Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter Withdrawal Amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.add_interest()

    elif choice == 5:
        account.account_details()

    elif choice == 6:
        print("Thank you for using the Bank Application.")
        break

    else:
        print("Invalid Choice! Please try again.")