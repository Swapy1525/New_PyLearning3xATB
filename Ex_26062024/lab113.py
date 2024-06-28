class Dog:
    name= None
    id= None

    #contructure
    #used to initialize the values
    #of the instance variables(Attributes)


    def sleep(self):
        print("Sleeping")

dog1=Dog()
dog1.name= "Jacky"
print(dog1.name)
dog1.sleep()

print("----------------------------------------")

dog2=Dog()
dog2.name="Chomfy"
print(dog2.name)
dog2.sleep()

#classes are blueprints and objects are instances of the class
#object is a real entity and classes are user defined and blueprints

#def _init_(self) ---function for initilizing put put value directly


