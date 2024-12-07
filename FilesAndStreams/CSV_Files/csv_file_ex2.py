# reading the data from the csv existing file
import csv

filename = input("Enter the existing filename: ")
with open(filename,'r') as fp:
    data = csv.reader(fp)
    for record in data:  # here record is of type list
        print(record)
    print("------------------------------------------")
