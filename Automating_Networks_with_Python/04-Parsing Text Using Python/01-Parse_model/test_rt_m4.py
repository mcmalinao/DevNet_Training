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

 WHAT This script does: The pytest functions for ensuring VRF configuration parser
  for IOXXE and IOXXR are functional.. Run with "-s" to see outputs.


"""
from parse_rt import parse_rt_ios, parse_rt_iosxr


def test_parse_rt_ios():
    """
    unit test for ios/xr models.
    """

    # Creates and display some tests.
    vrf_output = """
        vrf definition POLICE
         description POLICE
         rd 65000:1
         route-target export 65000:1
         route-target import 65000:11
        !
        vrf definition POLICE2
         description POLICE2
         rd 65002:1
         route-target export 65002:2
         route-target export 65002:22
         route-target import 65003:3
         route-target import 65003:33
        !
        vrf definition POLICE123
         description POLICE123
         rd 65002:1
         route-target import 65000:303
    """
    print(vrf_output)

    #Performing parsing, print structured data, and validate

    vrf_data = parse_rt_ios(vrf_output)
    print(vrf_data)
    _check_vrf_data(vrf_data)

def test_parse_rt_iosxr():
    """
    unit test for ios/xr models.
    """
    vrf_output = """
        vrf POLICE
         description POLICE
         address-family ipv4 unicast
          import route-target
           65000:11
           !
           export route-target
            65000:1
           !
          !
         !
        vrf POLICE2
         description POLICE2
         address-family ipv4 unicast
          import route-target
           65003:3
           65003:33
           !
           export route-target
            65002:2
            65002:22
           !
          !
         !
        vrf POLICE123
         description POLICE123
         address-family ipv4 unicast
          import route-target
           65000:303
           !
          !
         !
    """
    print(vrf_output)

    #Performing parsing, print structured data, and validate

    vrf_data = parse_rt_iosxr(vrf_output)
    print(vrf_data)
    _check_vrf_data(vrf_data)

def _check_vrf_data(vrf_data):
    """
    Common asserts for al parse_rt_ios
    """

    #Returned dick should have exactly 3 keys
    assert len(vrf_data)  == 3

    # Ensure VRF POLICE parsing succeed
    assert len(vrf_data["POLICE"]["route_export"]) == 1
    assert vrf_data["POLICE"]["route_export"][0] == "65000:1"
    assert len(vrf_data["POLICE"]["route_import"]) == 1
    assert vrf_data["POLICE"]["route_import"][0] == "65000:11"

    # Ensure VRF POLICE2 parsing succeed
    assert len(vrf_data["POLICE2"]["route_export"]) == 2
    assert vrf_data["POLICE2"]["route_export"][0] == "65002:2"
    assert vrf_data["POLICE2"]["route_export"][1] == "65002:22"
    assert len(vrf_data["POLICE2"]["route_import"]) == 2
    assert vrf_data["POLICE2"]["route_import"][0] == "65003:3"
    assert vrf_data["POLICE2"]["route_import"][1] == "65003:33"

    # Ensure VRF POLICE123 parsing succeed
    assert not len(vrf_data["POLICE123"]["route_export"]) #test len == 0
    assert len(vrf_data["POLICE123"]["route_import"]) == 1
    assert vrf_data["POLICE123"]["route_import"][0] == "65000:303"
