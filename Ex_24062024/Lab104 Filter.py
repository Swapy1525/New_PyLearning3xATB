# Filter in Python
# built in fun to filter the elemets in list tuple set.

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the above numbers with even numbers

new_list = [2, 4, 6, 8, 10]

def is_even(number):
    return number % 2 == 0



new_even_numbers= filter(is_even, number)
print(list(new_even_numbers))

def is_greater_5(number):
    return number>5

y=filter(is_greater_5,number)
print(list(y))





