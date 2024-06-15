for i in range(0,10):
    if i%3 ==0:
        print(i)
    else:
        print(i*2)

#Match case
numbers = int(input("Enter a Number\n"))
match numbers:
    case 1:
        print("You have enterd 1")
    case 2:
        print("You have enterd 2")
    case 3:
        print("You have enterd 3")
    case _:
        print("No Idea")