#walk me in the dir Question

import os

for root, dir, files in os.walk(r"C:\Users\swapy\PycharmProjects\New_PyLearning3xATB\July\Ex_05072024"):
    print(f"Current Dir {root}")
    print(f'Sub Dir Dir {dir}')
    print(f'files Dir Dir {files}')

    print(len(files))
    print(len(dir))





