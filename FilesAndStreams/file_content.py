# to open any file content
import pickle
while True:
    try:
        filename = input("Enter the filename u want to open: ")
        with open(filename,'r') as fp:
            print("=" * 70)
            print("\t\tFile content")
            print("=" * 70)
            file_data = fp.read()
            print(file_data)
            print("=" * 70)
        break
    except FileNotFoundError:
        print(f"{filename} does not exist")