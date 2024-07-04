#try , except(catch- java) and finally

# try:
#     number1= int(input("Enter the number 1\n"))
#     number2= int(input("Enter the number 2\n"))
#     print("result=",number1/number2)
#
# except Exception as e:
#     print(e)

try:
    number1= int(input("Enter the number 1\n"))
    number2= int(input("Enter the number 2\n"))
    result= number1/number2

except ValueError as ve:
    print(ve)

except ZeroDivisionError as zde:
    print(zde)

else:
    print(f'Result is {result}')

finally:    #run this code anyhow- finally is used to closing the file
    print("I will be executed anyhow!!!")





