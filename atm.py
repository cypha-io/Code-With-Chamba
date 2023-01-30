class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Your current balance is:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited:", amount)
        print("Your updated balance is:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("You have withdrawn:", amount)
            print("Your updated balance is:", self.balance)

atm = ATM(0)

while True:
    print("Welcome to Cypha-ATM")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 4:
        print("Thank you for using Cypha-ATM")
        break
    else:
        print("Invalid choice, please try again")
