#!/usr/bin/python

#- * -coding: utf - 8 - * -
import os
import MySQLdb
import pymol


db = MySQLdb.connect('localhost','root', '54321', 'Pymoldata')# your host, #your username# your password# name of the data base
cur = db.cursor()


def addData():
    print 'Enter Details:'
    pdbid = raw_input('1)Enter PDB ID')
    orgname = raw_input('2)Enter Organism Name')
    sql = "INSERT INTO Proteins (serialno,accessid,orgname,hyperlink) values (4,'&s','%s',filename)" % (pdbid, orgname)


def searchDatabase():
    ch1 = input('1)Search by PDB ID\n2)Search by Organism')
    if ch1 == 1:
      id = raw_input('Enter PDBID')
      sql = "SELECT * FROM Proteins WHERE accessid='%s'" % id
      cur.execute(sql)
      for row in cur.fetchall():
         print row
    if ch1 == 2:
         orgname = raw_input('Enter Organism Name')
         sql = "SELECT * FROM Proteins WHERE orgname='%s'" % orgname
         cur.execute(sql)
         for row in cur.fetchall():
           print row


print 'Welcome to Main Menu'
print 'What do you intend to do:'
print '-------------------------------'
print '1)Search in Database about your protein.'
print '2)Add your own data to the database.'
print '3)Fetch and Render PDB.'
print '4)Perform functions on your PDB .'
print '5)Functions on your Protein .'
print '6)If you want to Exit'
print '-------------------------------'
choice = input('Choose your option')
choice = int(choice)
if choice == 1:
    searchDatabase()
if choice == 2:
    addData()
if choice == 3:
    execfile('fetch.py')
if choice == 4:
    execfile('menu.py')
if choice == 5:
    execfile('menu-func.py')
if choice == 6:
    exit
