import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="54321", # your password
                      db="Pymoldata") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
id=raw_input("Enter PDBID")
# Use all the SQL you like
sql="SELECT * FROM Proteins WHERE orgname='%s'"%(id)
cur.execute(sql)

list1=[]

# print all the first cell of all the rows
for row in cur.fetchall() :
    list1.append(row)
    print "1."+row[1]
    print "2."+row[2]
    choice= raw_input("Enter which one you want to display")
    print row[choice]    
