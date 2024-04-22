"""
Bank class:

    Attributes: name (string), branches (list of Branch objects)
    Methods:
    add_branch(branch): Add a new branch to the bank.
    get_total_balance(): Return the total balance of all accounts in the bank.
    get_customer_with_highest_balance(): Return the customer object with the highest balance in the bank.

Branch class:
    Attributes: name (string), customers (list of Customer objects)
    Methods:
    add_customer(customer): Add a new customer to the branch.
    get_total_balance(): Return the total balance of all accounts in the branch.
    get_customer_with_highest_balance(): Return the customer object with the highest balance in the branch.

Customer class:
    Attributes: name (string), accounts (list of Account objects)
    Methods:
    add_account(account): Add a new account to the customer.
    get_total_balance(): Return the total balance of all accounts of the customer.
    get_account_with_highest_balance(): Return the account object with the highest balance of the customer.
Account class:
    Attributes: account_number (string), balance (float)
    Methods: None
    Your task is to implement these classes and write a program to simulate the banking system.
    The program should create a bank with multiple branches and customers, each having multiple accounts.
    It should then perform the following operations:

Add branches, customers, and accounts to the bank.
Deposit and withdraw money from the accounts.
Retrieve and display the total balance of the bank, branch, and customer.
Retrieve and display the customer and account with the highest balance in the bank.
"""
from bank_sort import merge_sort
from dataclasses import dataclass, field


@dataclass
class Account:
    account_number: str
    balance: float

    @property
    def _balance(self):
        return self._balance

    @_balance.setter
    def _balance(self, value):
        self._balance = value


@dataclass(frozen=True)
class Customer:
    customer_name: str
    accounts: dict = field(default_factory=lambda: {})

    def add_account(self, account_obj):
        self.accounts[account_obj.account_number] = account_obj

    def get_total_balance(self):
        return sum([acc.balance for acc in self.accounts.values()])

    def get_account_with_highest_balance(self):
        account_numbers = list(self.accounts.keys())
        balances = [acc.balance for acc in self.accounts.values()]
        max_balance = merge_sort(balances)[-1]
        idx = balances.index(max_balance)
        return self.accounts[account_numbers[idx]].account_number

    def deposit(self, amount, acc):
        self.accounts[acc.account_number].balance += amount
        print(self.accounts[acc.account_number].balance)

    def withdraw(self, amount, acc):
        if self.accounts[acc.account_number].balance == 0 or self.accounts[acc.account_number].balance - amount <= 0:
            raise Exception("Insufficient balance")
        self.accounts[acc.account_number].balance -= amount
        print(self.accounts[acc.account_number].balance)


@dataclass(frozen=True)
class Branch:
    branch_name: str
    customers: dict = field(default_factory=lambda: {})

    def add_customer(self, customer_obj):
        self.customers[customer_obj.customer_name] = customer_obj

    def get_total_balance(self):
        return sum([customer.get_total_balance() for customer in self.customers.values()])

    def get_customer_with_highest_balance(self):
        customer_names = list(self.customers.keys())
        balances = [cust.get_total_balance() for cust in self.customers.values()]
        max_balance = merge_sort(balances)[-1]
        idx = balances.index(max_balance)
        return self.customers[customer_names[idx]].customer_name


@dataclass(frozen=True)
class Bank:
    bank_name: str
    branches: dict = field(default_factory=lambda: {})

    def add_branch(self, branch_obj):
        self.branches[branch_obj.branch_name] = branch_obj

    def get_total_balance(self):
        return sum([branch.get_total_balance() for branch in self.branches.values()])

    def get_customer_with_highest_balance(self):
        customer_names = []
        for n in self.branches.values():
            customer_names += n.customers
        customer_objs = []
        for i in self.branches.values():
            customer_objs += list(i.customers.values())
        balances = [cus.get_total_balance() for cus in customer_objs]
        max_balance = merge_sort(balances)[-1]
        return customer_names[balances.index(max_balance)]


if __name__ == '__main__':
    account1 = Account('1', 100)
    account2 = Account('2', 2250)
    account3 = Account('3', 3200)
    account4 = Account('4', 3520)
    account5 = Account('5', 4003)
    account6 = Account('6', 26056)

    ravi = Customer("ravi")
    ravi.add_account(account1)
    # ravi.deposit(130, account1)
    # ravi.withdraw(20, account1)
    ravi.add_account(account2)
    shuvam = Customer("shuvam")
    shuvam.add_account(account3)
    shuvam.add_account(account4)
    milan = Customer("milan")
    milan.add_account(account5)
    milan.add_account(account6)

    # print(ravi.get_total_balance())
    # print(ravi.get_account_with_highest_balance())
    # print(ravi.deposit(500, 1))
    # print(ravi.withdraw(200, 1))

    # mumbai = Branch("mumbai")
    # mumbai.add_customer(shuvam)
    # mumbai.add_customer(ravi)
    # mumbai = Branch("Mumbai")
    # mumbai.add_customer(shuvam)
    # print(mumbai.get_total_balance())
    # print(mumbai.get_customer_with_highest_balance())

    # bank = Bank("SBI")
    # bank.add_branch(mumbai)
    # # print(bank.get_total_balance())
    # print(bank.get_customer_with_highest_balance())
