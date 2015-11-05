#!/usr/bin/python
import os
import sys
import subprocess
import time


os.system("clear")
print("Welcome to the PDB World of Project PyPlot")
loopa = 1 
loopb = 1
choicemain=1 
fileN = raw_input("Enter PDB file path: ")
print "Processing data for " + fileN + "\nPlease Wait..."

while loopa==1:
	print("Options:") 
	print("1. PDB Inferences")
	print("2. Implications in Real World")
	print("3. Exit Right Away!")
	choicemain = raw_input("Choice... ")
	choicemain = int(choicemain)

	if choicemain == 1:

		
		while loopb ==1:
			print("Functions derived from PDB:")
			print("1. Center of mass")
			print("2. Root Mean Square Deviation")
			print("3. PDB to fasta conveter")
			print("4. B-factor")
			print("5. Type of ATOMS")
			print("6. PDB Parameters") 
			print("7. Secondary structure details")
			print("8. Sequence resolution")
			print("9. Exit from Program")
			

			choice = raw_input("Enter your choice...")
			choice = int(choice)
			os.system("clear")

			if choice==1:
				print("Calculating Center of Mass of file " + fileN )
				cmd2 = "~/PymolDSA/pdb_centermass.py" + " " + fileN
				os.system(cmd2)
				continue 	

			elif choice==2:
				print("Calculating Root Mean Square Deviation ")
				file2 = raw_input("Enter File2 to get the Difference: ")
				cmd3 = "~/PymolDSA/rmsd.py" + " " + fileN + " " + file2
				os.system(cmd3)
				continue

			elif choice==3:
				print("Displaying Fasta data of PDB ")
				cmd1 = "~/PymolDSA/pdftofasta.py" + " " + fileN
				os.system(cmd1)
				continue

			elif choice==4:
				print("Calculating B-factor of Protein ")
				cmd5 = "~/PymolDSA/pdb_bfactor.py"+" "+ fileN
				os.system(cmd5)
				continue
				
   			elif choice == 5:
   				print("Types of Atoms in Protein")
    			cmd4 = "~/PymolDSA/name.py" 
        		os.system(cmd4)
        		continue
        	else:
        		loopb = 0 

	elif choicemain == 2:
		fileN = raw_input("Enter PDB file path: ")
		print "Processing data for " + fileN + "\nPlease Wait..."
		time.sleep(1)
		print("Real World Application from Knowledge acquired directly from PDB:")
		print("1. Solvent Accessible Surface Area ")
		print("2. Binding site of Protein")
		print("3. Exit function")
		choiceC = raw_input("Enter your choice...")
		choiceC = int(choiceC)
		if choiceC == 1:
			print("Solvent Accessible Surface Area")
			print("Application: Accessible Surface Area is often used when calculating the transfer free energy required to move a biomolecule from aqueous solvent to a non-polar solvent such as a lipid environment")
			continue
		elif choiceC == 2:
			print("Binding Site of Protein")
			print("Appliocation: Binding site on a Protein helps us to study and analyse the post attack phase of a drug.Identify regions of tight atomic packing. This is not the same as locating pockets, since surface sites may still be regions of tight packing.Filter out sites that are too exposed to solvent. In other words, sites that are on protrusions are unlikely to be good active sites.Use hydrophobic/hydrophilic classifications. This coarse classification of chemical type is used to separate water sites from the more likely hydrophobic sites.se a definition of hydrophilic that is invariant to protonation state and tautomer state (this means no distinction between donor and acceptor atoms). Use a definition of hydrophobic that is invariant to tautomer state (this means that aromaticity cannot be used).Avoid grid-based methods since grid methods are not invariant to rotation of the atomic coordinates and can consume large amounts of memory.")
			continue


	else:
		loopa = 0
		exit	







