"""
Python script for password manager - The password manager will be used to store and retrieve credentials for websites.

File Name :password_manager.py 
Authors Name : Dipti Bhosale
Date : 1 Nov 2022
Version :1.0.0

overview of the codes functionality :
    Show below Menu and Operations
        Add stored credentials and related resources (username, password and URL/resource)
        View stored credentials
        Exit the script
        Help

"""
# Import modules
import os
import sys

# appendNew function will append userName, password and website in the text file

def appendNew():
    DB = open("info.txt",'a')
    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")
    print()

    usrnm = "UserName: "+ userName + "\n"
    pwd = "Password: " + password + "\n"
    website = "website: " +website + "\n"

    DB.write(usrnm)
    DB.write(pwd)
    DB.write(website)
    DB.write("--------------------\n")
    DB.write("\n")
    DB.close()
    print("Password added")
    print()

# readPassword function will display userName, password and website from the text file

def readPassword():
    filesize = os.path.getsize("info.txt")
    if filesize==0:
        print("The file is empty.Add new credentials \n")
    else:
        DB = open("info.txt",'r')
        passwords=DB.read()
        print("Gathering passwords...Please wait \n")
        print(passwords)
        print("--End of file--\n")
        DB.close()

# help function will display help for Menu options

def help():
    print("Password Manager Help Guide\n")
    print("Add new password :This option will let you add a new Username/password to the database\n")
    print("View Password : This will show you the contents of the password database\n")
    print("Exit:This will exit the program\n")

if os.path.exists("info.txt"):
    print("File status...OK\n")

else:
    DB=open("file.txt",'w')
    print("Creating database")
    DB.close()

while True:
     print("Please make a selection from the menu below")
     print()
     print("1.Add new Password")
     print("2.View Passwords")
     print("3.exit")
     print("4.Help")
     print()
     menu_option =input("Please choose an item from the menu above: ")
     print()

     if menu_option == "1":
         appendNew()
     elif menu_option == "2":
         readPassword()
     elif menu_option =="3" :
         print("Ending program...BYE!")
         sys.exit()
     elif menu_option == "4":
         help()
     else:
         print("You did not enter valid response")
         print()
             
                    
 
