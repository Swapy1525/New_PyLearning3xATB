t=("swapy", "for","swapy")
print(set(t))

set1={1,2,3,4}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)

my_set2=set1.intersection(set2)  #and - commmon elements
print(my_set2)

my_set3=set1.difference(set2)
print(my_set3)

my_set4=set2.difference(set1)
print(my_set4)


