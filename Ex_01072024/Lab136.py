#Hierarchical inheritance

#father  -> Multiple childern

class father:

    def bhk1(self):
        print("you have 1bhk")

class swapy(father):

      def bhk2(self):
          print("you have 2bhk")

class vaishu(father):
    def bhk4(self):
        print("you have 4bhk")

class noclass(father):
    def nohouse(self):
        print("No House")

Swapnil=swapy()
Swapnil.bhk2()
Swapnil.bhk1()

print("------------------------")

Vaishnavi=vaishu()
Vaishnavi.bhk4()
Vaishnavi.bhk1()
print("------------------------")
No=noclass()
No.bhk1()
No.nohouse()

