#Inheritance
#acquire the attributes or behaviour
#data members and methods

# Types of Inheritance
# Single -80 %-> API web automation
# Multiple
# Multi level
# Hierarchical

class grandparent:  #parent class, base class
    key= "pass@123"

    def grandparent_method(self):
        return "Grandparent's Method"

class parent(grandparent): #child class sub class #single inheritance

    def parent_method(self): #no arg return type function
        return "Parents method"

Father= parent()
print(Father.parent_method())
print(Father.grandparent_method())
print(Father.key)
#single inheritance






