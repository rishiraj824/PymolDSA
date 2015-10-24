Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def main():
    filename = input("Welcom, please enter file name:\t")
    menu()
    choice= int(input("Enter menu choice:\t"))

    while choice != 5:
        #get file choice from user
        if choice == 1:
            #create file
            create(filename)
        elif choice == 2:
            #read file
            read(filename)
        elif choice == 3:
            #append file
            append(filename)
        elif choice == 4:
            #get total
            get_total(filename)

        choice = int(input("Enter menu choice:\t"))

    print("\nApplication Complete")

def menu():

    #user chooses a number from list
    print("Choose a number to continue:\t\n\
    Select 1 to create a file\n\
    Select 2 to read a file\n\
    Select 3 to append to a file\n\
    Select 4 to calculate the total of a file\n\
    Select 5 to exit programme")

def create(filename):

    #open file name
    outfile = open(filename,"w")
    again = "y"

    while again == "y":

        try:
            num = int(input("Input number:\t")
            outfile.write(str(num)+"\n")
            #asks user whether they want to continue or not
            again = input("Enter y to continue:\t")

        except ValueError:
                      print("An error occured,please enter an integer:\t")

        except:
                      print("An undetermined error occurred")
    #close file
    outfile.close()

def read(filename):

    read(filename)
    print("\nReading File)

    try:
        infile = open(filename,"r")

        for line in infile:

        number = int(line)
        print(number)

    except IOError:
            print("An error occured trying to read")
            print("the file", filename)

    except:
            print("An undefined error occurred")

def append(filename):

    append(filename)

    print("\nAppending to file")

    try:
        #create file object
        outfile = open(filename, "a")
        again = "y"

    while again == "y":

        try:
            num = int(input("input number to append to file:\t"))
            outfile.write(str(num)+"\n")
            again = input ("enter y to continue:\t
