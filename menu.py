import subprocess 
import os
import time 
print "Welcome to main menu"

fileN = raw_input("Enter PDB file path: ")
print "Processing data for " + fileN + "\nPlease Wait..."
time.sleep(1)

print "Fasta Format: "
cmd1 = "~/PymolDSA/pdftofasta.py" + " " + fileN
#subprocess.call(cmd1, fileN)
#subprocess.Popen(cmd1, shell=True) 
os.system(cmd1)
time.sleep(3)

print "Center of Mass: "
cmd2 = "com.py" + " " + fileN
subprocess.Popen(cmd2, shell=True)
os.system(cmd2)
time.sleep(3)

print "Root Mean Square Deviation: "
cmd3 = "rmsd.py" + " " + fileN + " " + fileN
subprocess.Popen(cmd3, shell=True)
os.system(cmd3)
time.sleep(3)

print "Free R Value: "
cmd2 = "com.py" + " " + fileN
#subprocess.Popen(cmd2, shell=True)
#os.system(cmd2)
#time.sleep(3)

print "No. of non hydrogen atoms used in Refinement: "
cmd2 = "com.py" + " " + fileN
#subprocess.Popen(cmd2, shell=True)
#os.system(cmd2)
#time.sleep(3)
