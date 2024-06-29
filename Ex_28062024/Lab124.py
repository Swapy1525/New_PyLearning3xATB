class car:
    name=None
    make=None
    model=None
#Constructure
    def __init__(self,name,make,model):
        self.name= name
        self.make= make
        self.model= model

    def start_enine(self):
        print("Starting a car with the name"+self.name)
        print("Starting a car with the make"+self.make)
        print("Starting a car with the model"+self.model)
#end of class


doge=car("doge","italy","2024")
doge.start_enine()

lambo=car("lambo","india","urus")
lambo.start_enine()




