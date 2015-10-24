atoms, coordinates = read_xyz(filename)

def read_xyz(filename):
   """Read filename in XYZ format and return lists of atoms and coordinates.

   If number of coordinates do not agree with the statd number in
   the file it will raise a ValueError.
   """

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

   if n_atoms != len(coordinates):
      raise ValueError("File says %d atoms but read %d points." % (n_atoms, len(coordinates))

   return atoms, coordinates
