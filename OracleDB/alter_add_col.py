# to alter the col by adding new col to the existing table
import oracledb
import oracledb as orc
try:
    con=orc.connect("system/Subbai45@localhost/orcl")
    cur=con.cursor()
    alter_query=("alter table student add clgname varchar2(10) not null")
    cur.execute(alter_query)
    print("new col added successfully")
except oracledb.DatabaseError:
    print("Data already exists")