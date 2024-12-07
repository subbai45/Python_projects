# open the existing file from the folder
try:
    with open (f"{input("Enter the existing file name: ")}") as fp:
        data = fp.read()
        print("Is file readable: ",fp.readable())
        print("Does file writable : ",fp.writable())
        print("Name of the file: ",fp.name)
        print("Mode of the file: ",fp.mode) # by default the mode will be 'r' mode
        print("=" * 70)
        print(f"\t\t Content of the {fp.name} ")
        print("=" * 70)
        print(data)
        print("=" * 70)
except FileNotFoundError:
    print("File doesnt exist ")