#Multiple conditions

#max bet 3 numbers   commit multiple lines ctrl /

#num1, num2, num3

num1=int(input("Enter number 1\n"))
num2=int(input("Enter number 2\n"))
num3=int(input("Enter number 3\n"))

if num1>num2 and num1>num3:
    print(num1)
elif num2> num1 and num2>num3:
    print(num2)
else:
    print(num3)

#In ternary, we cant use elif

