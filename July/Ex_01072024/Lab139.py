# Hybrid Inheritance

#multiple type of inheritance

#single, multiple, hierarchical

#mutliple return

class a:
    def a(self):
        print("a")

class b(a):
    def b(self):
        print("b")

class c(a):
    def c(self):
        print("c")

class d(b,c):
    def d(self):
        print("d")


D=d()
D.a()

def mutliple_return():
    return 99,"swapy", True

print(mutliple_return())
