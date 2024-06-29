#web automation - selenium
#page- you are going to automate

class vwlogin:
    email= None
    password = None

#constructure is setting value for email and password
    #we can pass no of argumrnts in constructure
    def __init__(self,email,password):
        self.email= email
        self.password= password

    def login_confirm(self):
            if self.password=="pass@123":
                print("Allowed to enter")

            else:
                print("Not Allowed")

amit=vwlogin("amit@gamil.com","pass@123")
amit.login_confirm()

swapy=vwlogin("swapy@test.com","12334444")
swapy.login_confirm()









