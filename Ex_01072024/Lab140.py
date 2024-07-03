#Polymorphism

#allows objects of different classes to be trated as
#objects from common class

#a morphism that sows poly behaviour

#Object can behave differently

# 2 methods
#method overloading--- does not exist in case of python

#method overriding

class Shape:

    def area(self):
        print("Area of the shape")

class rectangle(Shape):

    def __init__(self,length,width):

        self.length= length
        self.width= width

    def area(self):
        return self.length*self.width

class circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

shape1=rectangle(3,4)
print(shape1.area())

shape2= circle(10)
print(shape2.area())

shape3=Shape()
shape3.area()

#son can have a same name method
# but the function will be different---
# different execution or definition
#-- In java ---need to write Override ---but bot in python

#child will always override the parent function





