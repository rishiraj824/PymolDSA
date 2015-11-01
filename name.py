#! /usr/bin/env python

"""
Simple PDB parser

"""

# excerpts from PDB 3UNC
# http://www.rcsb.org/pdb/explore/explore.do?structureId=3UNC
fileName = raw_input('Enter fileName')
fp = open(fileName)



with open(fileName, "r") as ins:
    data = ins.readlines()
    pdb = []
    for line in ins:
        pdb.append(line)

charged_res_coords = [] # store x,y,z of extracted charged resiudes
charged_res = ["ARG", "HIS", "LYS", "ASP", "GLU"]
#iterate over lines in pdb
#lines = fp.readlines()
name = raw_input('Enter name of the molecule: ')
for a in data:
    if 'ATOM' in a:
        listName = list(name)
        length = len(listName)
        if(length==2):
            if listName[0] in a[13] and  listName[1] in a[14] and ' ' in a[15]:
                print a
        elif(length==3):
            if listName[0] in a[13] and  listName[1] in a[14] and listName[2] in a[15] and ' ' in a[16] :
                print a
        elif(length==1):
            if listName[0] in a[13] and  ' ' in a[14] :
                print a
        else:
            print 'No matches found'
            break
