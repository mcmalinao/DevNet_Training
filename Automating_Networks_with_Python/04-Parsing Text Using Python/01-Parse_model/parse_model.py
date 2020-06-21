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

 WHAT This script does: Parser for IOX-XE and XR: REGEXP testing.


"""
import re

def parse_model_ios(text):
    """
    Parse model ID from the IOS "show version" command..
    IF not match is found, None is returned.  Sample:
    cisco CSR1000V (VXE) processor (revision VXE) with 1078602K/3075K bytes of memory.
    """
    # raw string..
    model_regex = re.compile(r"cisco\s+(?P<model>\S+)\s+\(\S+\)\s+processor\s+")

    #attempt to match the regex againts the specific input..
    model_match = model_regex.search(text)
    if model_match:
        return model_match.group("model")

    #no match found..
    return None

def parse_model_iosxr(text):
    """
    Parse XRV.. " show version " command,,
    cisco IOS XRv Series (Pentium Celeron Stepping 3) processor with 3145215K bytes of memory.
    Note: XRV9K is diferrent "shos diag 0/0"
    PID                                      : R-IOSXRV9000-RP-C
    \s = [ \t\n\r\f\v], plus a few more escape char...
    #model_regex = re.compile(r"\s+PID\s+:[ \t]+(?P<model>\S+)")
    """
    model_regex = re.compile(r"cisco\s+IOS\s+(?P<model>\S+)\s+Series\s+")

    #attempt to match regexp agaings he specific inputself.
    model_match = model_regex.search(text)
    if model_match:
        return model_match.group("model")


    #no match found..
    return None

def parse_model_nxos(text):
    """
    Parse NXOS.. " show version " command,,
    cisco IOS XRv Series (Pentium Celeron Stepping 3) processor with 3145215K bytes of memory.
    Hardware
        cisco Nexus9000 C9300v Chassis
        with 4036632 kB of memory.
        Processor Board ID 9W94B1V5G5W
    """
    model_regex = re.compile(r"cisco\s+Nexus9000\s+(?P<model>\S+)\s+Chassis\s+")

    #attempt to match regexp agaings he specific inputself.
    model_match = model_regex.search(text)
    if model_match:
        return model_match.group("model")


    #no match found..
    return None
