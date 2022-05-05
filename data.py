import sqlite3

#connect to the database
conn=sqlite3.connect('movies.db')

#create a cursor
c=conn.cursor()


#execute our command uing cursor

c.execute("INSERT into movies VALUES('Bale','Romanoff',2016,'Nolen')")
c.execute("INSERT into movies VALUES('Bale','Romanoff',2017,'Nolen')")
c.execute("INSERT into movies VALUES('Lenardo','Rose',2019,'Cameroon')")
c.execute("INSERT into movies VALUES('Avatar-1','Avatar-2',2016,'Cameroon')")

print("Code executed successfully..")

#commit our command
conn.commit()
#close our command
conn.close() 
 BIN +12 KB 
movies.db
