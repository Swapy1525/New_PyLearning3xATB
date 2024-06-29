class bankacc:

    def __init__(self):
        self.balance = 0
        self.__private_var= 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        self.balance -=amount


    def show_balance(self):
        print("your balance is", self.balance)


jp_chase =bankacc()
print(jp_chase.balance)

jp_chase.deposit(100)
print(jp_chase.show_balance())

jp_chase.withdraw(99)
print(jp_chase.show_balance())




