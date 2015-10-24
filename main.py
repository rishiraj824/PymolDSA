#!/usr/bin/python

#- * -coding: utf - 8 - * -
import os
import MySQLdb
import pymol
import urllib
import subprocess


db = MySQLdb.connect('localhost','root', '54321', 'Pymoldata')# your host, #your username# your password# name of the data base
cur = db.cursor()


def addData():
    print 'Enter Details:'
    pdbid = raw_input('1)Enter PDB ID')
    orgname = raw_input('2)Enter Organism Name')
    filename=raw_input('3)Enter File Name')
    sql = "INSERT INTO Proteins (serialno,accessid,orgname,hyperlink) values (4,'&s','%s','%s')" % (pdbid, orgname,filename)


def searchDatabase():
    ch1 = input('1)Search by PDB ID\n2)Search by Organism')
    if ch1 == 1:
      id = raw_input('Enter PDBID')
      #sql = "SELECT * FROM Proteins WHERE accessid='%s'" % (id)
      # if cur.execute(sql)== 0:
       #   for row in cur.fetchall():
        #     print row
         #    file1=row[1]+".pdb"
      #else: 
      file1 = id+".pdb" 
      #print "\n\n\n"
      #subprocess.Popen('menu-func.py',shell=True)
      
      
      hyperlink="http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId="+id
      print hyperlink			
      pymol.finish_launching()
        
      pymol.cmd.load(file1)
      #urllib.urlretrieve (hyperlink, file1)
    

      print '1)Perform functions on your PDB .'
      ch=raw_input('Give your choice!')
      if ch== 1:
                   execfile('menu-func.py')
      
    if ch1 == 2:
         orgname = raw_input('Enter Organism Name')
         sql = "SELECT * FROM Proteins WHERE orgname='%s'" %(orgname)
         cur.execute(sql)
         for row in cur.fetchall():
           print row
         file1 = row[1]+".pdb"
         #print file1
         #hyperlink="http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId="+row[1]
         #urllib.urlretrieve (hyperlink, file1)
         pymol.finish_launching()
         pymol.cmd.load(file1)


print 'Welcome to Main Menu'
print 'What do you intend to do:'
print '-------------------------------'
print '1)Search in Database about your protein.'
print '2)Add your own data to the database.'
print '3)Exit'
print '-------------------------------'
choice = input('Choose your option')
choice = int(choice)
if choice == 1:
    searchDatabase()
if choice == 2:
    addData()
if choice == 3:
    exit

