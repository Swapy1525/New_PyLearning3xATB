# Functions- building blocks for python
# block of code that can be used or executed

#Built in functions
#they can return something
#have parameters


result= max(2,3)

#Define and call

def say_hello():#no return parameter/Argument
    print("Hello")

say_hello()

def say_hello_arg(name):   #no return parameter/Argument
    print("Hello",name)

say_hello_arg("Swapy")
say_hello_arg("Ja")

def say_hello_arg_default(name="Swapy"):   #no return type with default Argument
    print("Hello",name)

say_hello_arg_default()
say_hello_arg_default("Malhar")
say_hello_arg_default(name="Mahesh")

#Argument with return type

def sum_no_arg_ret(a,b):
    return a + b

result = sum_no_arg_ret(3,4)
print(result)

#reformat the code Ctrl + Alt + L















