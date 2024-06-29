class car:
    name=None

    def __init__(self):
        self.public_var= "public"
        self._proctected_var= "proctected123"
        self.__private_var= "pass@123"

    @classmethod
    def __private_method(self):
        print("Proctected")

    def printName(self):
        if self.__private_var==123:  #private functions can be accessed by functions within the functions
 #private things are allowed to access within the class
            print("Hi, 123")
        print("I'm Allowed")

#end of class

alto= car()
alto.printName()

#alto.__private_method()     #not allowed







