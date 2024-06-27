#map
#pick one item and apply the function
#gives the same number of elememts
#it should work with return numbers

numbers= [1,2,3,4,5,6,7,8,9,10]
print(numbers)
def double_num(num):
    return num*2

l=lambda a:a*2  #alternative for the function

new_list= map(double_num, numbers)
print(list(new_list))

new_list1= map(lambda n:n*2, numbers)  #alternate way
print(list(new_list1))

#filter
#pick item keep if true, if false remove it
#it can give less number of items as compared to actual list
#filter only works with function which gives true/false
#filter works if the functiom returns boolean values



def even_giver(nun):
    return nun%2==0

new_filter= filter(even_giver,numbers)
print(list(new_filter))


