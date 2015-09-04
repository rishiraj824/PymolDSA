
loop=0
while loop != 3:
    print("Welcome to Main Menu")
    print("What do you intend to do:")
    print("-------------------------------")
    print("1)Search in Database")
    print("2)Add your own data")
    print("3)If you want to Exit")
    print("-------------------------------")
    choice = input("Choice your options")
    choice = int(choice)

    if choice == 1:
     ch1=raw_input("1)Search by PDB ID\n2)Search by Organism")
     if ch1==1:
          execfile('database.py')
    break
     
    
    
    elif choice == 2:
        print("Enter Details:")
        ch1=raw_input("1)Enter PDB ID")
        ch1=raw_input("2)Enter Organism Name")
       
            
        
    elif choice == 3:
       print("Exiting")
       break

    else:
       print("Please enter the valid choice")

