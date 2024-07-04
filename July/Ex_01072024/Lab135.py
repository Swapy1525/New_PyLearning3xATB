class parent:

    gold = "gold 2kg"

    def BHK2(self):
        print("2BHK")


class child(parent):

    def BHK3(self):
        print("3BHK")

child_ref=child()
child_ref.BHK3()
child_ref.BHK2()
print(child_ref.gold)

# parent_ref=parent
# parent_ref.BHK3

#top to bottom
