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

 WHAT This script does: Using Paramiko to get information from network devices
 and print it to the screen.


"""

import time
import paramiko


def send_cmd(conn, command):
    """Given an open connection  and a command, issue the command and
    wait 1 second for the command to processedself.
    """
    conn.send(command + "\n")
    time.sleep(1.0)


def get_output(conn):
    """Read all the data from the bufer and
    decode the byt string as UTF-8.
    """
    return conn.recv(65535).decode("utf-8")


def main():
    """
    Execution starts here.
    """

    # Define host inventoyr in line.  Remember our platform typesself.
    #
    #
    host_dict = {
        "172.25.254.5": "show ntp associations",
        "172.25.254.4": "show ntp associations",
    }

    # For each host in the inventory dict, extract key and valueselfself.
    for hostname, ntp_cmd in host_dict.items():
        # Parmiko can be ssh client or server..
        conn_params = paramiko.SSHClient()
        # We dont need paramiko to refuse connections due to missing keys.
        conn_params.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn_params.connect(
            hostname=hostname,
            port=22,
            username="admin",
            password="admin",
            look_for_keys=False,
            allow_agent=False,
        )

        # Get interactive shell and wait a bit for the prompt to appear..
        conn = conn_params.invoke_shell()
        time.sleep(1.0)
        print(f"Logged into {get_output(conn).strip()} successfully")

        # Iterate over the list of commands, sending each one in seriesself.
        # The final commnad in the list is the os specificself.
        commands = [
            "terminal len 0",
            "show version | i Software,",
            "show inventory",
            ntp_cmd,
        ]
        for command in commands:
            # It helps to have a custom function sending
            # commands and reading output from the devicesself.
            send_cmd(conn, command)
            print(get_output(conn))

        # close session when we are done..
        conn.close()


# calls the main function is invoke from  shelll.
if __name__ == "__main__":
    main()
