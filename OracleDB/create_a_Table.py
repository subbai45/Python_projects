# python program to create t table in oracleDB

import oracledb as orc
try:
    connection=orc.connect("system/Subbai45@localhost/orcl")
    cur=connection.cursor()
    create_table_query=("create table student(sno number(3) primary key,sname varchar2(10) not null, grade varchar2(2) not null, class varchar(5) not null)")
    final=cur.execute(create_table_query)
    print("Table created successfully")
except orc.DatabaseError:
    print("Name already exist")