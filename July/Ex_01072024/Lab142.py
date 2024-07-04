#Method Overloading
#not supported in python
# supports in traditional sense


class mathutiles(object):

    def add(self,a,b):
        return a+b

    def add(self,a,c):
        return a-c

math=mathutiles()
op1=math.add(3,7)
print(op1)

# 2 or more methods with same name but different arg
#traditionally it is not supported



