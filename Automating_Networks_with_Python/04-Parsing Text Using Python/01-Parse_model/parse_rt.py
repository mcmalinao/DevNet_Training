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

 WHAT This script does: VRF configurations parser: REGEXP testing.


"""
import re

def parse_rt_ios(text):
    """"
    Parse VRF blocks of vrf text into indexable dic entries.  this typically feeds..
    into the rt_diff function to be tested against the intended configself.

    XE/IOS
    vrf definition POLICE
     rd 65000:1
     route-target export 65000:1
     route-target import 65000:1


    """

    vrf_list = ["vrf" + s for s in text.strip().split("vrf")if s]
    return_dict ={}
    for vrf in vrf_list:
        #Parse the VRF name definition...
        name_regex = re.compile(r"vrf\s+definition\s+(?P<name>\S+)")
        name_match = name_regex.search(vrf)
        sub_dict = {}
        vrf_dict = {name_match.group("name"): sub_dict}


        #Parse the RT imports int a list of strings..
        rti_regex = re.compile(r"route-target\s+import\s+(?P<rti>\d+:\d+)")
        rti_matches = rti_regex.findall(vrf)
        sub_dict.update({"route_import": rti_matches})

        #Parse the RT exports int a list of strings..
        rte_regex = re.compile(r"route-target\s+export\s+(?P<rte>\d+:\d+)")
        rte_matches = rte_regex.findall(vrf)
        sub_dict.update({"route_export": rte_matches})


        #append dic to return list..

        return_dict.update(vrf_dict)

    #return the vrf name idexable dict for reference later...
    return return_dict

def parse_rt_iosxr(text):
    """
         XR/IOS
         vrf CHEMICAL
          address-family ipv4 unicast
           import route-target
            65001:1
         !
           export route-target
            65001:1
    """
    vrf_list = ["vrf" + s for s in text.strip().split("vrf")if s]
    return_dict = {}
    for vrf in vrf_list:
        #Parse the VRF name definition...
        name_regex = re.compile(r"vrf\s+(?P<name>\S+)")
        name_match = name_regex.search(vrf)
        sub_dict = {}
        vrf_dict = {name_match.group("name"): sub_dict}

        #Capute all the text in between the start of import route-target.
        # the first ! to grab all the import RTs.  (.+?)! non greedy stoping at the !
        rti_list = _get_iosxr_rt(r"import\s+route-target(.+?)!",vrf)
        sub_dict.update({"route_import": rti_list})

        #Parse the RT exports.
        rte_list = _get_iosxr_rt(r"export\s+route-target(.+?)!",vrf)
        sub_dict.update({"route_export": rte_list})

        #append dic to return list..
        return_dict.update(vrf_dict)

    #return the vrf name idexable dict for reference later...
    return return_dict

def _get_iosxr_rt(regex_str, vrf_str):
    """
    internal function only to parse ios xr route targets from a vrf text output..
    this is a better design pattern than copy paste.. which was done for the ios
    parser...
    """
    regex = re.compile(regex_str, re.DOTALL)
    rt_matches = regex.findall(vrf_str,re.DOTALL)
    if rt_matches:
        rt_list = [s.strip() for s in rt_matches[0].strip().split("\n")]
    else:
        rt_list = []
    # return to list of parsed route-targets..
    return rt_list
