# to create a new folder

import os
try:
    Filename=input("Enter the name of the Folder: ")
    os.mkdir(Filename)
    print("Folder created successfully")
    list_folder=os.listdir(Filename)
    if(Filename in list_folder):
        with open(Filename,'r+') as fp:
            file_data=fp.read()
            print('='*100)
            print(f"FileData {file_data}")
            print('='*100)
            if(fp.writable()):
                fp.write(input())
except FileExistsError:
    print("File already exist, Please Enter another File Name..!!")