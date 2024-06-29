#Encapsulation
#wrapping the data/ Hiding

#bind the data variables with methods
#data variables /class members
#method- def function within the classs
#Hide the data members (class variable, instance variable)by only using the methods
#only class methods should be able to change the pass

class car:
    name=None
    password= 123

    def __init__(self):
        print("I am called when object is created")

    def change_pass(self):
        self.password=345
#end of class

XUV= car()
XUV.password=345
