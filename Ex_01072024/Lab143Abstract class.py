#Abstraction

#hiding the details and showing what is required


#encapsulation is within the class
#abstraction is not within the class-- it is within diff classes

#we have to complete it-- undefined----> incomplete method
#forceful methods that we have to give in the below functions
#mark with @abstractmethod

from abc import ABC, abstractmethod #module
#from 'folder_name' import 'file_name' ,abstractmethod
                           #class or method


class animal(ABC):  #when we add (ABC) -> becomes Abstract class
     def __init__(self,name):
         self.name=name

     @abstractmethod   #incomplete method - who is inheriting that has to complete
     def sound(self):
         pass

class Dog(animal):
#we cant pass , we need to complete the fun from parent class
    def sound(self):
        return "Bow Bow"

class cat(animal):

    def sound(self):
        return "Meow"

jacky=Dog("jacky")
print(jacky.sound())

goldie=cat("goldie")
print(goldie.sound())









