#!/usr/bin/env python3
 
# Copyright (C) 2017 Alcatel-Lucent, Inc.
# Authors:
#   Martin Carroll <martin.carroll@nokia.com>
#
# confidential and proprietary
# not for use or disclosure outside of nokia
# or its affiliated companies except under written agreement

#from __future__ import print_function

__all__ = ['digits']

def digits():
    # this version intentionally has a bug, last digit should be 9, not 0
    return '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170670'

if __name__ == "__main__":
    print(digits())
