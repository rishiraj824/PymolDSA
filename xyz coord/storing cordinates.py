#!/usr/bin/env python
# read xyz coordinate file

filename = "Ar_L16_N64.xyz"
atoms = []
coordinates = []
xyz = open(filename)
n_atoms = int(xyz.readline())
title = xyz.readline()
for line in xyz:
    atom,x,y,z = line.split()
    atoms.append(atom)
    coordinates.append([float(x), float(y), float(z)])
xyz.close()

print("filename:         %s" % filename)
print("title:            %s" % title)
print("number of atoms:  %d" % n_atoms)
