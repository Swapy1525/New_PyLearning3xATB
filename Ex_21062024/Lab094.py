#Decorators

#decorate functions
#It is a function that takes another function as a argument
#returns a new function that extends the behaviour

def decorate(func):
    def wrapper():
        print("Starting.....")
        print("***************")
        func()
        print("*******************")
        print("Ending/////////////")

    return wrapper()

@decorate
def say_hello():
    print("Hello")
#no neeed to call the func will be called by decorator




