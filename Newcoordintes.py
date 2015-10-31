#! /usr/bin/env python

"""
Simple PDB parser
Coded by Steve Moss (gawbul [at] gmail [dot] com)
http://about.me/gawbul

Slicing features by Pierre Poulain 
http://cupnet.net/
"""

# excerpts from PDB 3UNC
# http://www.rcsb.org/pdb/explore/explore.do?structureId=3UNC
fp = open('3NXY.pdb')



with open("3NXY.pdb", "r") as ins:
    pdb = []
    for line in ins:
        pdb.append(line)

charged_res_coords = [] # store x,y,z of extracted charged resiudes
charged_res = ["ARG", "HIS", "LYS", "ASP", "GLU"]
#iterate over lines in pdb
#lines = fp.readlines()
for line in pdb:
    # check if line starts with "ATOM"
    if line.startswith('ATOM'):
        # define fields of interest
        atom_id = line[6:11].strip()
        atom_name = line[12:16].strip()
        res_name = line[17:20].strip()
        chain_name = line[21:22].strip()
        residue_id = line[22:26].strip()
        x = line[30:38].strip()
        y = line[38:46].strip()
        z = line[46:54].strip()
        if res_name in charged_res:
            # pull out third spatial (y-coordinate)
            #print z
            # append groups to list
            charged_res_coords.append([atom_id, atom_name, res_name, chain_name, residue_id, x, y, z])
#H atoms
#usratom = raw_input("enter an atom name to search")
#for atom in atom_name:
#   if atom == usratom:
#       print [item for item in charged_res_coords]
    
        
# print the stuff we added
for atom in atom_name:
    print atom+"\n"
    print [usratom for usratom in atom_name]
