#web automation - selenium
#page- you are going to automate

class vwlogin:
    email= None
    password = None

    def login_confirm(self):
            if (self.email=="amit@gmail.com" and
                self.password=="pass@123"):
                print("Allowed to enter")

            else:
                print("Not Allowed")

amit=vwlogin()
amit.email="amit@gmail.com"
amit.password="pass@123"
amit.login_confirm()

swapy=vwlogin()
swapy.email="amit@gmail.com"
swapy.password="pass@124"
swapy.login_confirm()











