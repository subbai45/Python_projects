#Program for Creating CSV File with pythom Code by using csv.writer()
#CSVWriteEx1.py
import csv # Step-1
hnames=["SNO","SNAME","MARKS","COLNAME"] # Step-2
records=[[100,"Pavan",55.55,"JNTU"],
        [200,"Tejas",66.66,"MU"],
        [300,"Kalash",46.66,"JNTU"],
        [400,"Sravan",76.66,"OUCET"],
        [500,"KVR",11.11,"OU"],
        [600,"Jadav",76.66,"HCU"]] # Step-3
with open(input("Enter the filename with extension.csv: "),"a") as fp: #step-4
    csvwr=csv.writer(fp) # Step-5
    #write the header names to the  csv file by using writerow()
    csvwr.writerow(hnames) # Step-6
    #write the records to the csv file by using writerows()
    csvwr.writerows(records) # Step-7
    print("CSV File Created --Verify")




