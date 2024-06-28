class person:
    # attributes
    name = None
    id = None
    age = None
    phone_no = None

    # behaviours

    def walk(self):    #No arg No return type
        print("I am walking")

    def talk(self):  # 1 Arg No return type
        print("I am talking")

    def sleep(self, name):  # 1 Arg 1 return type
        print("I am talking")
        return None
    def another(self):
        print("I am Method")

    def walk_return(self): # No Arg but return type
        return "I am Walking"

# create object in the class
surya = person()
surya.name = "surya Prakash"
surya.talk()

swapy = person()
swapy.name = "Swapy K"
swapy.walk()


