# program to remove the table from the oracleDb

import oracledb as orc
try:
    con=orc.connect("system/Subbai45@localhost/orcl")
    cur=con.cursor()
    table_name=input("Enter the table name: ")
    remove_table_query=f"drop table {table_name}"
    cur.execute(remove_table_query)
    print("Table removed successfully-- verify in sql")
except orc.DatabaseError as db:
    print("Problem in OracleDb: ",db)