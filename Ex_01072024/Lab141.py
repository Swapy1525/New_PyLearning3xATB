class father:

    def home(self):
        print("2bhk")

class son(father):
    def home(self):
        super().home()
        print("No home")

swapy=son()
swapy.home()

#Super-- call my father (parents) func as well mine






