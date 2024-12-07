# reading an excel sheet by using pandas
import pandas as pd
import csv
import pickle
print("="*60)
filename = r"C:\Users\hp\Downloads\sample_data_pandas.csv"
csv_data = pd.read_csv(filename)
print(csv_data)
print("="*60)
csv_data.index = ['val'+str(i) for i in range(len(csv_data))]
print(csv_data)
print("="*60)
with open (input("Enter the filename with extension.csv: "),'w+b') as fp:
    csvwr = csv.writer(fp)
    csvwr.writerows(csv_data)
    csvr = pickle.load(csvwr)
    print(csvr)
