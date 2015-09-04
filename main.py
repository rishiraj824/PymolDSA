import pymol
import MySQLdb


#pymol.finish_launching()

#cmd.load("3NXY.pdb")
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="54321", # your password
                      db="Pymoldata") # name of the data base
cur = db.cursor()
def addData():
     print("Enter Details:")
     pdbid=raw_input("1)Enter PDB ID")
     orgname=raw_input("2)Enter Organism Name")
     sql="INSERT INTO Proteins (serialno,accessid,orgname,hyperlink) values (4,'&s','%s',filename)"%(pdbid,orgname)
    
def searchDatabase():
    ch1=input("1)Search by PDB ID\n2)Search by Organism")
    if ch1==1:
        id=raw_input("Enter PDBID")
        sql="SELECT * FROM Proteins WHERE accessid='%s'"%(id)
        cur.execute(sql)
        for row in cur.fetchall():
           print row
    if ch1==2:
        orgname=raw_input("Enter Organism Name")
        sql="SELECT * FROM Proteins WHERE orgname='%s'"%(orgname)
        cur.execute(sql)
        for row in cur.fetchall():
           print row

           
print("Welcome to Main Menu")
print("What do you intend to do:")
print("-------------------------------")
print("1)Search in Database")
print("2)Add your own data")
print("3)If you want to Exit")
print("-------------------------------")
choice = input("Choose your option")
choice = int(choice)
if choice == 1:
    searchDatabase()
if choice==2:
    addData()

    

