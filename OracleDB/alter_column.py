# to alter the coloumn size of the existing table

def alter_modify(table_name):
    aq=f"alter table {table_name} modify"+f"{input('Enter the modify query: ')}"
    return aq
def alter_add(table_name):
    aq = f"alter table {table_name} add" + f"{input('Enter the add query: ')}"  #(percentage number(4,2) not null)
    return aq

#main program

import oracledb as orc
try:
    con=orc.connect("system/Subbai45@localhost/orcl")
    cur=con.cursor()
    table_name=input("Enter the existing table name: ")
    print("="*50)
    print("\tSelect alter operation")
    print("="*50)
    print("\t\t1. modify")
    print("\t\t2. add")
    print("="*50)
    ch=int(input("Enter ur choice: "))
    match(ch):
        case 1:
            alter_modify_query=(alter_modify(table_name))
            cur.execute(alter_modify_query)
            print("table modified successfully--verify in sql")
        case 2:
            alter_add_query=(alter_add(table_name))
            cur.execute(alter_add_query)
            print("table column added successfully--verify in sql")
        case _:
            print("please choose valid option")
except orc.DatabaseError as db:
    print("Problem in OracleDb is: ",db)