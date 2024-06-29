
class vwlogin:
    email= None
    password = None
    my_tuple= tuple()

    def login_confirm(self):
            if (self.email=="amit@gmail.com" and
                self.password=="pass@123"):
                print("Allowed to enter")

            else:
                print("Not Allowed")

#with input fuction
email= input("Enter the email\n")
password= input("Enter the password\n")
amit=vwlogin()
amit.email=email
amit.password=password
amit.login_confirm()

swapy=vwlogin()
swapy.email="amit@gmail.com"
swapy.password="pass@124"
swapy.login_confirm()











