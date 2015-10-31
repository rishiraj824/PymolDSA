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
pdb = [
"ATOM   6455  CA  HIS A 863      67.077 124.238  39.765  1.00 21.04           C  ",
"ATOM   6588  CA  ARG A 880      71.845 113.877  36.770  1.00 16.38           C  ",
"ATOM   6830  CA  PHE A 911      61.272 109.012  33.241  1.00 15.29           C  ",
"ATOM   8183  CA  ASP A1084      76.538  97.355  28.275  1.00 17.61           C  ",
"ATOM   8320  CA  LEU A1101      84.288  72.813  25.891  1.00 22.39           C  ",
"ATOM   8429  CA  GLU A1114      76.247  69.337  19.532  1.00 24.21           C  "
]

charged_res_coords = [] # store x,y,z of extracted charged resiudes 
charged_res = ["ARG", "HIS", "LYS", "ASP", "GLU"]

 # iterate over lines in pdb
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
            print z
            # append groups to list
            charged_res_coords.append([atom_id, atom_name, res_name, chain_name, residue_id, x, y, z])

# print the stuff we added
print [item for item in charged_res_coords]
