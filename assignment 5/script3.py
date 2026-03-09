class BankAccount:
    def __init__(self, acc_no):
        self.acc_no = acc_no
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient Balance")

    def show(self):
        print("Account:", self.acc_no)
        print("Balance:", self.balance)


acc = BankAccount("12345")
acc.deposit(5000)
acc.withdraw(2000)
acc.show()