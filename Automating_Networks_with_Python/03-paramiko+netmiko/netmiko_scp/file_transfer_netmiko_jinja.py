#!/usr/bin/env python

"""Copyright (c) 2020 Author:Marlon Malinao	Email:marlon.c.malinao@outlook.com
All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 SUCH DAMAGE.

 WHAT This script does: Using SCP via netmiko to configure network devices.


"""

import sys
from yaml import safe_load
from netmiko import Netmiko, file_transfer


def main(argv):
    """
    Execution starts here.
    """

    # Read host file into structured data, may raise YAMLerror.
    #
    #
    with open("host.yml", "r") as handle:
        host_root = safe_load(handle)

    # Netmiko uses "cisco_ios" instead of "ios"  AND
    # "cisco_xr" instead of "iosxr", so use a mapping dict to convert
    # "cisco_nxos" instead of "nxos"
    platform_map = {"ios": "cisco_ios", "nxos": "cisco_nxos"}

    # Iterate over the list of hosts (list of dictionaries)
    for host in host_root["host_list"]:

        # uset the map to get the poper netmiko paltform
        platform = platform_map[host["platform"]]

        # Create a netmiko SSH connection handler to access the device:
        # Initialie ssh connection
        print(f"Connecting to {host['name']}")
        conn = Netmiko(
            host=host["name"],
            username="admin",
            password="admin",
            device_type=platform,
        )

        # Upload the file specified. the dict.get(key) function dictionaries
        # to  retrieve the value at the specified key and returns Environment
        # if it does not exist. Very usefule for network automtions!
        print(f" Uploading {argv[1]}")
        result = file_transfer(
            conn,
            source_file=argv[1],
            dest_file=argv[1],
            file_system=host.get("file_system"),
        )

        # Print result details
        print(f" Details: {result}\n")

        # close session when we are done..
        conn.disconnect()


# calls the main function is invoke from  shelll.
if __name__ == "__main__":
    main(sys.argv)
