import psycopg2
# data base connecting
"""con=psycopg2.connect(database="jesus",user="postgres",password="postgres",host="localhost",port="5432")
print("successfully connect")

cur=con.cursor()
cur.x("select * from sample")
a=cur.fetchall()
for i in a:
    print(i)"""
#-------------------------------------------------------------------------------
#insert,update,delete,select data to table1
con=psycopg2.connect(database="jesus",user="postgres",password="postgres",host="localhost",port="5432")
cur=con.cursor()
"""cur.execute("insert into school(name,gender,totalmarks,percentage)values('Alexander','Male',393,80.0),('Mervin','Male',450,90.0),('Vimal','Male',345,60.0),('Susai','Male',430,92.0),('Abin','Male',400,92.0)")"""
"""cur.execute("update school set name='Raj' where percentage=80 returning *")"""
"""cur.execute("delete from school where percentage=80")
cur.execute("select * from school")
f=cur.fetchall()
print(f)"""
'''cur.execute("insert into school(name,gender,totalmarks,percentage)values('John','Male',400,80)")
cur.execute("alter table school add column city varchar null")
cur.execute("select * from school")
a=cur.fetchall()
print(a)'''
con.commit()
cur.close()
con.close()
#---------------------------------------------------------------------------------
#insert,update,delete,select,alter to table2
con=psycopg2.connect(database="jesus",user="postgres",password="postgres",host="localhost",port="5432")
cur=con.cursor()
cur.execute("create table if not exists college(Name varchar(20),gender varchar(20),total int,percentage int)")
print("sucess")
cur.close()
con.close()
