"""
Python script to  determine whether any host with an IP address on a given network is Alive or NOT ALive.

File Name :PingIPAdd.py 
Authors Name : Dipti Bhosale
Date : 1 Nov 2022
Version :1.0.0

overview of the codes functionality :
    Get input from a user, a network address in dotted decimal format to be scanned.
    Get input form a user, a start and end host number range to be scanned
    Iterate in Range and show  which addresses are alive 
"""


# Import modules
import subprocess
import ipaddress

# Function to validate IP Address
def validate_ip_address(ip_string):
   try:
       ip_object = ipaddress.ip_address(ip_string)
       return True
   except ValueError:
       print("The IP address " + ip_string + " is NOT valid.")
       return False

# Prompt the user to input a network address
netAddress = input("Enter the Network Address(ex.192.168.1.100) :")

# Validated a network address
if validate_ip_address(netAddress) :
    
    # Find Last occurance of dot (.) to use for IpRangeAddress
    dot = netAddress.rfind(".")
    netStartIpRange  = netAddress[0:dot + 1]

    # Prompt the user to input Starting host number and Last host Number
    startCount = int(input("Enter the Starting host number (ex.100) : "))
    endCount = int(input("Enter the Last host number (ex.110) : "))
    endCount = endCount + 1


    # For each IP address in the range, 
    # run the ping command with subprocess.run 
    # process.returncode is 0 then display ipAddress is  ALive otherwise display ipAddress is NOT ALive  

    print ("** Scanning Started **")

    for ip in range(startCount,endCount):
        ipAddress = netStartIpRange + str(ip)

        process = subprocess.run(['ping', '-n', '1', '-w', '500', ipAddress], stdout =subprocess.PIPE, text = True , shell=True)

        if process.returncode == 0:
              print(ipAddress, "is ALIVE")
        else:
              print(ipAddress, "is NOT ALIVE")     

    print ("** Scanning completed **")
    
else :
    print("exiting program : re-Run with valid input network address (ex.192.168.1.100)")









