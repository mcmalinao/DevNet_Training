import paramiko #Implementation of the SSHv2 protocol [1], providing both client and server functionality.
import datetime
import os.path
import time  ##insert some waiting time..
import sys
import re   ##search


#Checking username/password file if it exist in the local file system.
#Prompting user for input - USERNAME/PASSWORD FILE
user_file = input("\n# Enter user file path and name (e.g. D:\\MyApps\\myfile.txt): ")

#Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

#Checking commands file
#Prompting user for input - COMMANDS FILE
cmd_file = input("\n# Enter commands file path and name (e.g. D:\\MyApps\\myfile.txt): ")

#Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :) Sending command(s) to device(s)...\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()

#Open SSHv2 connection to the device
def ssh_connection(ip):
    ##importing these 2 global variables from above to local fucntion.
    global user_file
    global cmd_file

    #Creating SSH CONNECTION
    try:
        #Define SSH parameters
        selected_user_file = open(user_file, 'r')

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the username from the file  stript to separate the user from the password. its only index0 ['admin,python'] rstrip to avoid cathing new line char.
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the password from the file
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        #Logging into device, ssh connection using sshclient class.
        session = paramiko.SSHClient()

        #For testing purposes, this allows auto-accepting unknown host keys
        #Do not use in production! The default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the device using username and password  safety measur for the rstrip to remove \n.
        session.connect(ip.rstrip("\n"), username = username, password = password)

        #Start an interactive shell session on the router
        connection = session.invoke_shell()

        #Setting terminal length for entire output - disable pagination  ( Paramikos way of sending command..)
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        #Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        #Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        #Starting from the beginning of the file
        selected_cmd_file.seek(0)

        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #Closing the user file
        selected_user_file.close()

        #Closing the command file
        selected_cmd_file.close()

#Checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))

        else:
            print("\nDONE for device {}. Data sent to file at {}.\n".format(ip, str(datetime.datetime.now())))

        #Test for reading command output
        #print(str(router_output) + "\n")

        #Searching for the CPU utilization value within the output of "show processes top once" b stands for bytes (bytes like object)
        #output pattern %Cpu(s): 26.5 us,  \(s\) - () is part of output itself, next (\s) there is one or more space to consider..then + for the value (.+?) .=any char, += previous expression may repeat one or moretimes , ?=matching minimal fastion
        # as few as possible..until the first spacce is found (\s) followed by "us"  Note so there will be 3 groups here.. (\s) (.+?) (\s).. important group is the CPU,  group number starts at 1..so we are interested on group2
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s) +us,", router_output)

        #Extracting the second group, which matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
        utilization = cpu.group(2).decode("utf-8")

        #Printing the CPU utilization value to the screen
        #print(utilization)

        #Opening the CPU utilization text file and appending the results
        with open("/home/devnetadmin/DevNet/Training/Python3_Network_Programming_Build_5_Network_Applications/Section21-APP-CPU-Graph/cpu.txt", "a") as f:
            #f.write("{},{}\n".format(str(datetime.datetime.now()), utilization))
            f.write(utilization + "\n")

        #Closing the connection
        session.close()
        # paramiko AuthenticationException
    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")
