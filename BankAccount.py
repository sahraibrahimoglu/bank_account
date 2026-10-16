class BankAccount:
    account_count = 0
    def __init__(self, owner, balance = 0 ):
        self.owner = owner
        self.balance = balance
        BankAccount.account_count += 1

    def __str__(self):
        return f"{self.owner.upper()} - Balance: {self.balance:.2f}"

    def deposit(self, amount):
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            self.balance += amount
            return f"{self.owner.upper()}-New Balance is: {self.balance:.2f}"

    def withdraw(self, amount):

            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > self.balance:
                raise ValueError("Amount must be less than balance.")
            self.balance -= amount
            return f"{self.owner.upper()}-New Balance is: {self.balance:.2f}"

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        return f"{self.owner.upper()}-New Balance is: {self.balance:.2f}"

class PremiumAccount(BankAccount):
    def __init__(self, owner, balance = 0, overdraft_limit = 200):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        return f"New Balance is: {self.balance:.2f}"
    def __str__(self):
        return super().__str__() + f"- Overdraft Limit: {self.overdraft_limit}"

def show_menu():
     print("-------------------------")
     print("----BANK ACCOUNT MENU----")
     print("-------------------------")
     print("1.Create Account")
     print("2. Deposit")
     print("3. Withdraw")
     print("4. Transfer")
     print("5. Display Account")
     print("6. Delete Account")
     print("0. Exit")

def find_account(account_list, name):
    for i, acc in enumerate(account_list):
        if acc.owner.lower() == name.lower():
            return i
    return -1

accounts = []
while True:
    show_menu()
    choice =input("Enter your choice: ")
    if choice == "1":
        account_name = input("Write your account name: ").strip()
        account_balance = float(input("Enter your initial balance: "))
        print("Would you like to switch to Premium Account?")
        answer = input("Enter your choice: (y/n)").strip().lower()
        if answer == "y":
            print("You switched to Premium Account! Your overdraft limit is $200.")
            accounts.append(PremiumAccount(account_name, account_balance))
            new_acc =PremiumAccount(account_name, account_balance)
        else:
            print("Your account has created successfully.")
            accounts.append(BankAccount(account_name, account_balance))
            new_acc =BankAccount(account_name, account_balance)

    elif choice == "2":
        account_name = input("Write your account name: ").strip()
        index = find_account(accounts, account_name)
        if index == -1:
            print("Account not found.")
        else:
            try:
                amount = float(input("Enter deposit amount: "))
                print(accounts[index].deposit(amount))
            except ValueError as e:
                print("Error:", e)

    elif choice == "3":
        account_name = input("Write your account name: ").strip()
        index = find_account(accounts, account_name)
        if index == -1:
            print("Account not found.")
        else:
            try:
                amount = float(input("Enter withdraw amount: "))
                print(accounts[index].withdraw(amount))
            except ValueError as e:
                print("Error:", e)

    elif choice == "4":
        account_name = input("Write your account name: ").strip()
        index = find_account(accounts, account_name)
        if index == -1:
            print("Account not found.")
        else:
            other_name = input("Select the other account: ").strip()
            other_index = find_account(accounts, other_name)
            if other_index == -1:
                print("Other account not found.")
            elif other_index == index:
                print("You cannot transfer to the same account.")
            else:
                try:
                    amount = float(input("Enter the transfer amount: "))
                    print(accounts[index].transfer(accounts[other_index], amount))
                except ValueError as e:
                    print("Error:", e)
    elif choice == "5":
        account_name = input("Write your account name: ").strip()
        index = find_account(accounts, account_name)
        if index == -1:
            print("Account not found.")
        else:
            print(accounts[index])

    elif choice == "6":
        account_name = input("Write your account name: ").strip()
        index = find_account(accounts, account_name)
        if index == -1:
            print("Account not found.")
        else:
            answer = input(f"Delete {accounts[index].owner}'s account? (y/n): ").strip().lower()
            if answer == "y":
                del accounts[index]
                print("Account deleted.")
            else:
                print("Cancelled.")

    elif choice == "7":
        print("Thank you for using Bank Account.")
        print("Goodbye!")
        break
    else:
        print("INVALID CHOICE!")









