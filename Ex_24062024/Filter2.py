letters= ['a', 'b','c','d','e','u']

def filter_voules(letters):
    voules= ['a', 'e','i','o','u']
    return letters in voules

v=filter(filter_voules, letters)
print(list(v))

result= filter_voules("c")
print(result)

