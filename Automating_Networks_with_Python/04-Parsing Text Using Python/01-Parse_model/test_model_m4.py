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

 WHAT This script does: The pytest functions for ensuring platform model ID parser
  for IOXXE and IOXXR and nXOS are functional.. Run with "-s" to see outputs.


"""
from parse_model import parse_model_ios, parse_model_iosxr, parse_model_nxos


def test_parse_model_ios():
    """
    unit test for ios/xr models.
    """

    # Positive test case ; provide valid output that should parse correctly
    model_output = """
         cisco CSR1000V (VXE) processor (revision VXE) with 1078602K/3075K bytes of memory.
         Processor board ID 9XK3ZRX1VLH
         4 Gigabit Ethernet interfaces
         32768K bytes of non-volatile configuration memory.
    """
    print(model_output)

    #Performing parsing, print structured data, and validate

    model_data = parse_model_ios(model_output)
    print(model_data)
    assert model_data == "CSR1000V"

    #Negative testcase: provide invalid output that should not be parse
    model_output = """
         cisco (VXE) processor (revision VXE) with 1078602K/3075K bytes of memory.
         Processor board ID 9XK3ZRX1VLH
         4 Gigabit Ethernet interfaces
         32768K bytes of non-volatile configuration memory.
     """
    print(model_output)

    #Performing parsing, print structured data, and validate

    model_data = parse_model_ios(model_output)
    print(model_data)
    assert model_data is None


def test_parse_model_iosxr():
    """
    unit test for XRV.. " show version " command,,

    Note: XRV9K is diferrent "shos diag 0/0"
    PID                                      : R-IOSXRV9000-RP-C
    \s = [ \t\n\r\f\v], plus a few more escape char...
    #model_regex = re.compile(r"\s+PID\s+:[ \t]+(?P<model>\S+)")
    """
    # Positive test case ; provide valid output that should parse correctly
    model_output = """
         cisco IOS XRv Series (Pentium Celeron Stepping 3) processor with 3145215K bytes of memory.
    """
    print(model_output)

    #Performing parsing, print structured data, and validate

    model_data = parse_model_iosxr(model_output)
    print(model_data)
    assert model_data == "XRv"

    #Negative testcase: provide invalid output that should not be parse
    model_output = """
         cisco IOS Series (Pentium Celeron Stepping 3) processor with 3145215K bytes of memory.
     """
    print(model_output)

    #Performing parsing, print structured data, and validate

    model_data = parse_model_iosxr(model_output)
    print(model_data)
    assert model_data is None



def test_parse_model_nxos():
    """
    unit test for NXOS.. " show version " command,,
    Hardware
        cisco Nexus9000 C9300v Chassis
        with 4036632 kB of memory.
        Processor Board ID 9W94B1V5G5W
    """
    # Positive test case ; provide valid output that should parse correctly
    model_output = """
         Hardware
           cisco Nexus9000 C9300v Chassis
           with 4036632 kB of memory.
           Processor Board ID 9W94B1V5G5W
    """
    print(model_output)

    #Performing parsing, print structured data, and validate

    model_data = parse_model_nxos(model_output)
    print(model_data)
    assert model_data == "C9300v"

    #Negative testcase: provide invalid output that should not be parse
    model_output = """
         Hardware
           cisco Nexus9000 Chassis
           with 4036632 kB of memory.
           Processor Board ID 9W94B1V5G5W
     """
    print(model_output)

    #Performing parsing, print structured data, and validate

    model_data = parse_model_nxos(model_output)
    print(model_data)
    assert model_data is None
