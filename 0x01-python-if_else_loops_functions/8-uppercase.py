#!/usr/bin/python3

def uppercase(str):
    last = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            last += chr(ord(char)-32)
        else:
            last += char
    print("{}".format(last))
