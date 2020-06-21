#  part#1
import random
import sys

def subnet_calc():
    try:
        print("\n")
        #Checking IP address validity
        while True:
            ip_address = input("Enter an IP address: ")

            #Checking octets
            ip_octets = ip_address.split('.')

            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break

            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        #Checking Subnet Mask validity
        while True:
            subnet_mask = input("Enter a subnet mask: ")

            #Checking octets
            mask_octets = subnet_mask.split('.')
            ## first octet should be  255,  the 2nd to 4rth octed value should fall inside the "mask", 1st octed should be greater than or equal to 2nd octet and so on..
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break

            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue

#Algorithm for subnet identification, based on IP and Subnet Mask

# Part2:
        #Algorithm for subnet identifacation based on the IP and subnet masks.
        #Convert mask to binary string, before that it must be converted to integer first.. note that when it is in binary it will be preceded by"0b". a strip was used.

        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            #print(binary_octet)
            #zfill method, if the lenght of the binary is less than 8 it will fill up zeros. aka padding.
            mask_octets_binary.append(binary_octet.zfill(8))

        #print(mask_octets_binary)

        binary_mask = "".join(mask_octets_binary)
        #print(decimal_mask)
        #Example: for 255.255.255.0 => 11111111111111111111111100000000

        #Counting host bits in the mask and calculating number of hosts/subnet  host per subnets = ((2 the power of x) - 2)
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) #return a positive value for the /32 mask (all 255s) absolute..in case a /32 host..

        #print(no_of_zeros)
        #print(no_of_ones)
        #print(no_of_hosts)

        #Obtaining wildcard mask, inverted subnet mask.  = 255.255.255.255 - subnet mask.
        wildcard_octets = []
        #subtracting 255 o each octet mof mask_octets (split mask ). and converted to integer
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))

        #print(wildcard_octets)

        wildcard_mask = ".".join(wildcard_octets)
        #print(wildcard_mask)

#Part3

        #Convert IP to binary string
        ip_octets_binary = []

        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            #print(binary_octet)

            ip_octets_binary.append(binary_octet.zfill(8))

        #print(ip_octets_binary)
        #Example: for 192.168.10.1 =>

        binary_ip = "".join(ip_octets_binary)

        #print(binary_ip)
        #Example: for 192.168.2.100 => 11000000101010000000101000000001

        #Getting the network address and broadcast address from the binary strings obtained above
        #zfill can be address as well.
        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        #print(network_address_binary)

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        #print(broadcast_address_binary)

        #Converting everything back to decimal (readable format)
        net_ip_octets = []

        #range(0, 32, 8) means 0, 8, 16, 24   step of 8..
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

        #We will end up with 4 slices of the binary IP address: [0: 8], [8: 16], [16: 24] and [24:31]; remember that each slice goes up to, but not including, the index on the right side of the colon!
        # 1st octet - 8 bits  index 0-7 slice [0: 8].....4th octet 8 bit index 24-31 - slice [24:32]* -- *32 is the correct boundary index.
        #print(net_ip_octets)

        net_ip_address = []
        ##convert binary to decimal..remember int function help us to convert binary to decimal. and convert them to string..  to join them a single string ntwork ip addresss.
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        #print(net_ip_address)

        network_address = ".".join(net_ip_address)
        #print(network_address)

        bst_ip_octets = []

        #range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)

        #print(bst_ip_octets)

        bst_ip_address = []

        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        #print(bst_ip_address)

        broadcast_address = ".".join(bst_ip_address)
        #print(broadcast_address)

        #Results for selected IP/mask  review string formats..
        print("\n")
        print("Network address is: %s" % network_address)
        print("Broadcast address is: %s" % broadcast_address)
        print("Number of valid hosts per subnet: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")

#PART4
        #Generation of random IP addresses in the subnet
        # while was used while loop keeps asking the user after generating the previous one as long the user is replying y.
        while True:
            generate = input("Generate random IP address from this subnet? (y/n)")

            if generate == "y":
                generated_ip = []
                #Obtain available IP address in range, based on the difference between octets in broadcast address and network address
                # bst_ip_address and net_ip_address are list octet ip address..
                for indexb, oct_bst in enumerate(bst_ip_address):
                    #print(indexb, oct_bst)  it will show like these   0 192 \n 1 168 \n 2 10 \n 3 255
                    for indexn, oct_net in enumerate(net_ip_address):
                        #print(indexn, oct_net) #it will show like these   0 192 \n 1 168 \n 2 10 \n 3 0  nexted 4 loops 4 iteration
                        if indexb == indexn:
                            if oct_bst == oct_net:
                                #Add identical octets to the generated_ip list, appending the network ip address to the list= common octet of broadcast and network.
                                generated_ip.append(oct_bst)
                            else:
                                #Generate random number(s) from within octet intervals and append to the list,  generate randomInteger..(x, y)  so it will be int(oct_net), int(oct_bst) then convert to string and added to the same list generated_ip
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

                #IP address generated from the subnet pool
                #print(generated_ip)
                y_iaddr = ".".join(generated_ip)
                #print(y_iaddr)

                print("Random IP address is: %s" % y_iaddr)
                print("\n")
                continue

            else:
                print("Ok, bye!\n")
                break


    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

#Calling the function
subnet_calc()

#End of program
