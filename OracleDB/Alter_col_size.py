# to alter the col size of the existing table

import oracledb as orc
try:
    con=orc.connect("system/Subbai45@localhost/orcl")
    cur=con.cursor()
    alter_col_query=("alter table student modify column marks to grade")
    cur.execute(alter_col_query)
    print("Modified successfully")
except orc.DatabaseError:
    print("something went wrong")