class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_dict = {self.account_number: {"account_holder_name": self.account_holder_name,
                                           "account_number": self.account_number,
                                           "balance": self.balance}}

    def deposit(self, amount, account_number):
        if account_number in obj.final_dict.keys():
            available_balance = obj.final_dict.get(account_number).get("balance")
            balance = available_balance + amount
            obj.final_dict.get(account_number).update({"balance": balance})
            return f"Account Debited Successfully "
        else:
            return f"Enter correct account number"

    def withdraw(self, amount, account_number):
        if account_number in obj.final_dict.keys():
            if amount < obj.final_dict.get(account_number).get("balance"):
                available_balance = obj.final_dict.get(account_number).get("balance")
                balance = available_balance - amount
                obj.final_dict.get(account_number).update({"balance": balance})
                return "Withdraw Successfully"
            else:
                return f"Insufficient Balance"
        else:
            return f"Enter correct account number"

    def transfer(self, account1, account2, amount):
        acc1_bal = obj.final_dict.get(account1).get("balance")
        acc2_bal = obj.final_dict.get(account2).get("balance")
        balance1 = acc1_bal - amount
        obj.final_dict.get(account1).update({"balance": balance1})
        balance2 = acc2_bal + amount
        obj.final_dict.get(account2).update({"balance": balance2})
        return f"Rs {amount} transfer to account {account2} from {account1}"


class Bank:
    def __init__(self):
        self.input_dict = {}
        self.final_dict = {}

    def user_inputs(self):
        account_number = int(input("Enter Account Number :"))
        account_holder_name = input("Enter Account Holder Name :")
        balance = int(input("Enter Creating Balance :"))
        self.input_dict.update({"account_holder_name": account_holder_name,
                                "account_number": account_number, "balance": balance})

    def create_account(self):
        obj = BankAccount(self.input_dict.get("account_number"), self.input_dict.get("account_holder_name"),
                      self.input_dict.get("balance"))
        self.final_dict.update(obj.account_dict)
        return obj

    def open_account(self):
        self.user_inputs()
        obj = self.create_account()
        print(obj.account_dict)
        print("Account Created Successfully ")

    def deposit(self):
        obj = self.create_account()
        account_number = int(input("Enter Account Number :"))
        amount = int(input("Enter amount to deposit :"))
        a_dict = obj.deposit(amount, account_number)
        print(a_dict)

    def withdraw(self):
        obj = self.create_account()
        account_number = int(input("Enter Account Number :"))
        amount = int(input("Enter amount to withdraw :"))
        a_dict = obj.withdraw(amount, account_number)
        print(a_dict)

    def transfer_money(self):
        obj = self.create_account()
        account1 = int(input("Enter account number from transfer"))
        account2 = int(input("Enter account number to transfer"))
        amount = int(input("Enter amount to transfer"))
        a_dict = obj.transfer(account1, account2, amount)
        print(a_dict)

    def display_data(self):
        print(self.final_dict)

    def display_account_info(self):
        account_number = int(input("Enter account number :"))
        print(self.final_dict.get(account_number))


if __name__=='__main__':
    obj=Bank()
    # obj.user_inputs()
    # print(obj.create_account())
    # obj.open_account()
    # obj.deposit()
    # obj.withdraw()
    # obj.transfer_money()
    # obj.display_data()
    # obj.display_account_info()
