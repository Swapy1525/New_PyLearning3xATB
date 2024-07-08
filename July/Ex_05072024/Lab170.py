import os

fd= os.open("Testdata.txt",os.O_RDWR)
os.write(fd,b'Hello I am writing this for you')  #we can use fun like read write append create
os.close(fd)





