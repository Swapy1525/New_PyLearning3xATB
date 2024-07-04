#how to write to a file

with open("testdata.txt",'a') as file:
    file.write("Hello This is test data for python")
    file.write("\nthis can be done as well")

#to read multiple lines -> user file.readlines


with open("testdata.txt", "r") as file:
    lines=file.readlines()

for line in lines:
    print(line, end="")


