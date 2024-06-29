class vwologin:

    def __init__(self,email,password,name):
        self.__email= email
        self.__password= password
        self.name= name

    def login_confirm(self):
        if self.__email=="swapy@gmail.com" and self.__password== 123:

            print("you can login with private data")
        else:
            print("not allowed")
#end of class

page1= vwologin("swapy@gmail.com",123,"swapy")
page1.login_confirm()
print(page1.name)
# print(page1.__email) Not able to access as private


page2= vwologin("swapy@we.com",123,"RAJA")
page2.login_confirm()








