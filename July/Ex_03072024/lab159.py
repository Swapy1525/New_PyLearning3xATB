class MyCustomException(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message)   #calling the parent's contructure

balance= 100
withdraw= int(input("Enter the amount\n"))

if withdraw > balance:
    raise MyCustomException("Bal is Low!!")
#RAISE - except - (raise is used when we know condition will fail)
else:
    print("Rem Balance", balance-withdraw)



