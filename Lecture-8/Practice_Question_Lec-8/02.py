class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "is debited")
        print("Total balance : ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "is credited")
        print("Total balance : ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(12345, 10000)
print(acc1.acc_no)
print(acc1.balance)

acc1.debit(2000)
acc1.credit(5000)