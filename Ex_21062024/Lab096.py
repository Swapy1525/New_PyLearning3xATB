my_dict={'a':1 ,'b':2, 'c':4, 'a':433, 'd':2}
print(my_dict)
print(len(my_dict))
#we cannot have duplicate keys but we can have duplicate values
print(list(my_dict))
print(list(my_dict.values()))
print(list(my_dict.keys()))

for i in list(my_dict.values()):
    print(i)

for k,v in my_dict.items():
    print(k,v)

