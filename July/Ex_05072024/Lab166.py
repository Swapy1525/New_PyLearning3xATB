# OS Module
# OS modules are used to interact with the operation system
# get working dir, change dir, file exist, filename, size

import os

print(os.name)  # nt- windows posix ios

print(os.getcwd())

print(os.listdir())

# os.mkdir("Swapy1525")

size = os.path.getsize("Testdata.txt")
print(size)
if size != 0:
    print("file exist and has some content")
else:
    print("file does not exist, no data")

modtime= os.path.getatime("Testdata.txt")   #Epoch time
print(modtime)

# print(os.remove("Swapy"))  #to delete the file

import time
print(time.gmtime(modtime))

print(time.localtime())





