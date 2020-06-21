import sys

#Checking octets
def ip_addr_valid(iplist):

    for ip in iplist:
        ip = ip.rstrip("\n")   ##strips \n newline character since the ip address in ip.txt file are listed on each line.
        octet_list = ip.split('.')  ##spliting each ip address in the list, we want to extract each of the 4rth octet to check the condtions elements of the list also a string..

        #first condtions octet list = 4 and, since the octet_list is a string we need to convert it to integer so we can compare it to a value.
        #first octet: multicaset 0-223 (1<=,  <=223) and loopback 127. (!= 127) and ( link local address microsoft dhcp failed  first octet (!= 169) or 2nd octet (!= 254)) uniqute combination of 169.254.
        #2nd-4th octet: (0<=  <=255)
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue

        else:
            print('\n* There was an invalid IP address in the file: {} :(\n'.format(ip))
            sys.exit()
