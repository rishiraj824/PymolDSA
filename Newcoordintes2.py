# import regex module
import re

# set fake pdb rows
pdb = ["ATOM 1512 N VAL A 222 8.544 -7.133 25.697 1.00 48.89 N", "ATOM 1513 CA VAL A 222 8.251 -6.190 24.619 1.00 48.64 C", "ATOM 1514 C VAL A 222 9.528 -5.762 23.898 1.00 48.32 C", "ATOM 1572 NH2 ARG A 228 7.890 -13.328 16.363 1.00 59.63 N", "ATOM 1617 N GLU A1005 11.906 -2.722 7.994 1.00 44.02 N"]

# create some variables
charged_res_coords = [] # store x,y,z of extracted charged resiudes 
charged_res = ["ARG", "HIS", "LYS", "ASP", "GLU"]

# compile regex
regex = re.compile("^ATOM\s([0-9]{4})\s([A-Z0-9]+)\s([A-Z]{3})\s([A-Z]{1}\s{0,1}[0-9]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([0-9\.-]+)\s([A-Z]{1})$")

# iterate over lines in pdb
for line in pdb:
    # check if starts with ATOM
    if line.startswith('ATOM'): 
        # iterate over charged residues
        for res in charged_res:
            # is residue in line?
            if res in line:
                # check for match to regex
                match = regex.match(line)
                # pull out third spatial
                third_spatial = match.group(7)
                print third_spatial
                # append groups to list
                charged_res_coords.append(match.groups()[0:-3])

# print the stuff we added
print [item for item in charged_res_coords]
