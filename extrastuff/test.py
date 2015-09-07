import os


fileN = raw_input("Enter PDB file path: ")
print "Processing data for " + fileN + "\nPlease Wait..."


os.system("pdftofasta.py")
