class Dog:
    name= None
    id= None

    def __init__(self,name, id):   #parameterized constructure - have init
        self.name=name
        self.id= id

    # def __init__(self):
    #     print("default constructure")

        #when the constructure is added , we need to enter atttributes
    #contructure
    #used to initialize the values
    #of the instance variables(Attributes)

    def sleep(self):
        print("Who is Sleeping  ->"+ self.name)

dog1=Dog("chow",1)
dog2=Dog("Jacky",2)
print(f'{dog1.name} has id {dog1.id}')
print(f'{dog2.name} has id {dog2.id}')

dog1.sleep()





