class students:

    def __init__(self):
        self.name=input("Enter the name")
        self.age=input("Enter the age")

    def display(self):
        print(f'Name is {self.name}, age is {self.age}')


new_std =students()
new_std.display()