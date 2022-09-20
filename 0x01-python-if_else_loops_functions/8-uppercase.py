#!/usr/bin/python3
def uppercase(str):
    w_text = ""
    for i in (str):
        har = ord(i)
        if char >= ord('a') and char <= ord('z'):
            har = char - 32
            new_text = chr(char)
        else:
            new_text = i
            print("{:s}".format(new_text), end="")
            print("")
