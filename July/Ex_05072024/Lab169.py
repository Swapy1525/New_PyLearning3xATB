import os

directory = r"C:\Users\swapy\PycharmProjects\New_PyLearning3xATB\July\Ex_05072024"

for root, dirs, files in os.walk(directory):
    print(f'Current Directory: {root}')

    # Print subdirectories
    if dirs:
        print(f'Subdirectories: {dirs}')

    # Print files
    if files:
        print(f'Files: {files}')