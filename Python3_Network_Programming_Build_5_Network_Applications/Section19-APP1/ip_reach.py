import sys
import subprocess

#Checking IP reachability
def ip_reach(iplist):

    for ip in iplist:
        ip = ip.rstrip("\n")

        # ping  2 packets.  stdout ping output supress. windows /n.. for linux -c
        ping_reply = subprocess.call('ping %s -c 2' % ip, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL, shell=True)
        #reply type echo reply type 0
        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue

        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()
