# create a table dynamically

import oracledb as orc
def createtable():
    #while True:
        try:
            con=orc.connect("system/Subbai45@localhost/orcl")
            cur=con.cursor()
            table_name=input("Enter the table name: ")
            print("Table name is: ",table_name)
            create_table_query=f"create table {table_name}"+f"{input('CREATE TABLE TABLE_NAME(COL-1 DB DATATYPE,COL2 DB DATA TYPE,...,COL-N DB DATATYPE)):')}"
            #create_table_query=f"{input('Enter the Query to create table (CREATE TABLE TABLE_NAME(COL-1 DB DATATYPE,COL2 DB DATA TYPE,...,COL-N DB DATATYPE)): ')}"
            cur.execute(create_table_query)
            print("Table created successfully-verify in sql")
        except orc.DatabaseError as db:
            print("Problem in oracleDb is: ",db)

#main program
createtable()
#create table student(sno number(2) primary key,sname varchar2(10) not null,marks number(5,2) not null,grade varchar2(2) not null,school varchar2(20) not null)