import os
import sys
import subprocess
import time
print("Welcome to the PDB World")
fileN = raw_input("Enter PDB file path: ")
print "Processing data for " + fileN + "\nPlease Wait..."
time.sleep(3)
loop = 1
while loop ==1:        
        print("What do you want to do:")
        print("1)Center of mass")
        print("2)RMSD")
        print("3)PDB to fasta conveter")
        print("4)B-factor")
        print("5)chiral center")
        print("6)Free R- value")
        print("7)PROT ATOMS")
        print("8)NUC ACID ATOMS")
        print("9) HETEROGEN ATOMS")
        print("10)SOLVENT ATOMS")
        print("11)Chiral center restraints")
        print("12)Related entries")
        print("13)Secondary structure details")
        print("14)Sequence resolution")
        print("15)if you want to exit")

        choice = input("Choice your options")
        choice = int(choice)
        os.system("cls")

        if choice == 1:
               print("1)Center of mass")
               cmd2 = "com.py" + " " + fileN
               subprocess.Popen(cmd2, shell=True)
               os.system(cmd2)
               time.sleep(3)
               

        if choice == 2:
               print("2)RMSD")
               cmd3 = "rmsd.py" + " " + fileN + " " + fileN
               subprocess.Popen(cmd3, shell=True)
               os.system(cmd3)
               time.sleep(3)
        if choice == 3:
               print("3)PDB to fasta conveter")
               cmd1 = "pdftofasta.py" + " " + fileN
               subprocess.Popen(cmd1, shell=True) 
               os.system(cmd1)
               time.sleep(3)

        if choice == 4:
               print("4)B-factor")
        if choice == 5:
               print("5)chiral center")
        if choice == 6:
               print("6)Free R- value")
               cmd2 = "com.py" + " " + fileN
        if choice == 7:
               print("7A)PROT ATOMS")
        if choice == 8:
               print("7B)NUC ACID ATOMS")
        if choice == 9:
               print("7C) HETEROGEN ATOMS")
        if choice == 10:
               print("7D)SOLVENT ATOMS")
        if choice == 11:
               print("8)Chiral center restraints")
        if choice == 12:
               print("9)Related entries")
        if choice == 13:
               print("10)Secondary structure details")
        if choice == 14:
               print("11)Sequence resolution")
        if choice == 15:
               loop ==0
               exit
              

        else:
                 print("please enter a valid option")

        os.system("cls")
          
          
          
          
          
          
          
          
          
          
      
   
          
          
          
          

          
          
      
