#Multiple Inheritance

class father:
    def father_money(self):
        return "10 rupees"

    def home(self):
        print("fathers home")

class mother:

     def mother_money(self):
         return "5 rupees"

     def mother_home(self):
         return "Mothers home"

class son(father,mother):

    def home(self):
        print("3 bhk home")

#diamond problem - Java  Ambiquoty
#python
#f,m -Som
#if there is a function with same name in all classes,
# if son has the fucntion , will take preference
# and if son does not have, the will consider from 1st class added to son)


Swapy=son()
print(Swapy.father_money())
print(Swapy.mother_money())
Swapy.home()  #local has preference  -> then 1st added class
#method resolution




