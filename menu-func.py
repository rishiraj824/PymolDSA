import os
import sys

loop = 1
while loop ==1:
        print("Welcome to the PDB World")
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

        if choice == 2:
               print("2)RMSD")
        if choice == 3:
               print("3)PDB to fasta conveter")

        if choice == 4:
               print("4)B-factor")
        if choice == 5:
               print("5)chiral center")
        if choice == 6:
               print("6)Free R- value")
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
              

        else:
                 print("please enter a valid option")

        os.system("cls")
          
          
          
          
          
          
          
          
          
          
      
   
          
          
          
          

          
          
      
