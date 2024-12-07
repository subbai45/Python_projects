# to display the voter whether eligible to vote or not
while(1):
    print("=" * 50)
    age=int(input("Enter the age of the voter: "))
    print("=" * 50)
    if(age<=18):
        print("{} - Not ELigible to vote,Enter again".format(age))
        print("=" * 50)
    else:
        print("{} Eligible to vote".format(age))
        print("=" * 50)
        break