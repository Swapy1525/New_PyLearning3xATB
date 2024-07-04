# File IO

# with open("swapy.txt",'r') as file:
#     print(file.read())
#     file.close()

# try:
#     with open("swapy.txt.", 'r') as file:  # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
#         print(file.read())
#
# except FileNotFoundError as fnfe:
#     print("i am not able to find the file.please check path")
#
# finally:
#     print("Closing the file")
#     file.close()



try:
    with open("example.txt.", 'r') as file:  # FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
        print(file.read())

except FileNotFoundError as fnfe:
    print("i am not able to find the file.please check path")

finally:
    print("Closing the file")
    try:
        file.close()
    except NameError as ne:
        print(ne)







