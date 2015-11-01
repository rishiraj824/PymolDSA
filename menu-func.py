
import os
import sys
import subprocess
import time
print("Welcome to the PDB World")
fileN = raw_input("Enter PDB file path: ")
print "Processing data for " + fileN + "\nPlease Wait..."
time.sleep(1)
loop = 1
while loop ==1:        
	print("What do you want to do:")
	print("1)Center of mass")
	print("2)RMSD")
	print("3)PDB to fasta conveter")
	print("4)B-factor")
	print("5)chiral center")
	print("6)Free R- value")
	print("7)Know the type of ATOMS")
	print("8)Chiral center restraints")
	print("9)Related entries")
	print("10)Secondary structure details")
	print("11)Sequence resolution")
	print("12)if you want to exit")

	choice = input("Choice your options")
	choice = int(choice)
	os.system("cls")

	if choice == 1:
	       print("1)Center of mass")
	       cmd2 = "~/PymolDSA/pdb_centermass.py" + " " + fileN
	       subprocess.Popen(cmd2, shell=True)
	       os.system(cmd2)
	       time.sleep(3)
	       

	if choice == 2:
	       print("Root mean Square Difference: ")
	       file2 = input("Enter File2 to get the Difference")	
	       cmd3 = "~/PymolDSA/rmsd.py" + " " + fileN + " " + file2
	       subprocess.Popen(cmd3, shell=True)
	       sys.stdin.read(1)
	       
	if choice == 3:
	       print("3)PDB to fasta conveter")
	       cmd1 = "~/PymolDSA/pdftofasta.py" + " " + fileN
	       subprocess.Popen(cmd1, shell=True) 
	       os.system(cmd1)
	       sys.stdin.read(1)

	if choice == 4:
	       print("4)B-factor")
         cmd5 = "~/PymolDSA/pdb_bfactor.py"
	if choice == 5:
	       print("5)chiral center")
	if choice == 6:
	       print("6)Free R- value")
	       cmd2 = "com.py" + " " + fileN
	if choice == 7:
	       cm4 = "~PymolDSA/name.py"
         subprocess.Popen(cmd4, shell=True) 
	if choice == 11:
	       print("8)Chiral center restraints")
	if choice == 12:
	       print("9)Related entries")
	if choice == 13:
	       print("10)Secondary structure details")
         cm5 = "~PymolDSA/pdb_torsion.py"
         subprocess.Popen(cmd5, shell=True) 
	if choice == 14:
	       print("11)Sequence resolution")
	if choice == 15:
	       loop ==0
	       exit
	      

	else:
		 print("please enter a valid option")

	os.system("cls")
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
      
   
	  
	  
	  
	  

	  
	  
      
