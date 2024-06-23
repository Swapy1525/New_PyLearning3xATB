# dictnory
# key and value

my_dict = {}
my_dict2 = {"name": "Swapy",
            "age": 23 ,
            "address": "Pune"
}

print(len(my_dict2))
print(my_dict2)
print(my_dict2["age"])

phone= dict(name="Swapy", age=25)
print(phone["name"])
print(phone.get("name"))

#we can use get operator or square braces

print(phone.values())
print(phone.keys())
#values of values and keys




phone["name"]= "Mayur"
print(phone)

#dict is mutable - values can be changed.






