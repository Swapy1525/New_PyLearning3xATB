#Multi level inheritance

#grandfather -> father -> child


class Grandparent:

    key ="gold 10 kg"   #property

    def grandfather_method(self):
         print("grandfathers method")


class parent(Grandparent):
    key1= "10 cr"
    def parents_method(self):
        print("parents method")

class child(parent):

    def child_method(self):
        print("childs method")

Swapy=child()
Swapy.child_method()
Swapy.parents_method()
Swapy.grandfather_method()
print(Swapy.key)
print(Swapy.key1)






