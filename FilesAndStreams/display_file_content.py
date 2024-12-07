# accept any file and display its content

filename=input("Enter the filename to display its data: ")
try:
    while True:
        with open(filename,"r+") as fp:
            content_in_file=fp.read()
            print("="*60)
            print("\tcontent in the ",filename)
            print("=" * 60)
            print(content_in_file)
            print("=" * 60)
            var=input("\tEverything fine with the file press '@' \n Does anything need to change in the file press '!' : ")
            if(var == '@'):
                break
            elif(var == '!'):
                data=input("Enter the new data to the file: ")
                write_the_file=fp.write(str(data+'\t'))
            else:
                break
except FileNotFoundError:
    print("File does not exist,please enter valid file name")