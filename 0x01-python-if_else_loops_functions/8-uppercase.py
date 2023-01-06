#!/usr/bin/python3

def uppercase(str):
    Ch_prt = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        Ch_prt = Ch_prt + i
    print("{:s}".format(Ch_prt), end="")
    print()
