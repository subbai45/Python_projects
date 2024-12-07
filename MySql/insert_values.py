# program to insert the values in the existing file

import mysql.connector as mc
try:
    con=mc.connect(host="localhost",user = "root", passwd = "Subbai45", database = "subbai")
    cur = con.cursor()
    database_name = input("Enter the database name: ")
    iq = (f"insert into {database_name} values (%d,%s,%s,%s,%s,%s,%s,%s) ")
    id = int(input("Enter id: "))
    name = input("Enter name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    mail = input("Enter mail: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    institute = input("Enter institute name: ")
    print(iq %(id,name,username,password,mail,dob,gender,institute))
   '''# cur.execute(iq %(id,name,username,password,mail,dob,gender,institute))
    # con.commit()
    row = cur.rowcount
    print("{} entry successfully inserted".format(row))'''
'''except mc.DatabaseError as db:
    print("Problem in Database: ",db)'''


