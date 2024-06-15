# Triangle Classifier:

side1=int(input("enter length of side 1\n"))
side2=int(input("enter length of side 2\n"))
side3=int(input("enter length of side 3\n"))

if side1==side2==side3:
    print("The triangle is equilateral")
elif side1==side2 or side2==side3 or side1==side3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")





