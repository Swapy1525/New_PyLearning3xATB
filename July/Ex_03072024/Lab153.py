print("---start of program---")

try:   #to fix the exception
    a = int(input("\nEnter the number1"))  # name- data type mismatch (swapy)
    b = int(input("\nEnter the number2"))
    c = a / b  # zero div error

    print("Result Div is", c)

except Exception as e:   #Exception is a class
    print(e)
    print("please enter integer")

print('---End of program---')



