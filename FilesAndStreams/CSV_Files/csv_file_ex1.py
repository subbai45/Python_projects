# create a file and store some data in it
import csv
filename = input("Enter the filename with extension.csv: ")
lst = [10,20,30,40,50]
with open(filename,'w+') as fp:
    csvwr = csv.writer(fp)
    csvwr.writerow(lst)
    for val in range(1,5):
        csvwr.writerow(lst)
    csvr = csv.reader(fp)
    for val in csvr:
        print(val)