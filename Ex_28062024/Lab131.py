class bankacc:

    def __init__(self):
        self.balance = 0
        self.__private_var= 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance +=amount

    def __withdraw(self,amount):
        self.balance -=amount


    def __show_balance(self):
        print("your balance is", self.balance)

    def if_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def if_auth_user(self,auth,amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not allowed")


jp_chase =bankacc()
print(jp_chase.balance)

jp_chase.deposit(1000)

secret_pass= input("Enter your pin")
if secret_pass == "1234":
    jp_chase.if_auth(True)
else:
    jp_chase.if_auth(False)

# jp_chase.if_auth(False)

# jp_chase.if_auth_user(True,100)
# jp_chase.if_auth(True)




