#!/usr/bin/python3
#-*- coding: utf-8 -*-
from   sys import argv
import re

count   = 0
for char in str(argv[1]):
    print(hex(ord(char)).replace("0x", ""), end=" ")
    count += 1
    if count % 4 == 0:
        print(end=" ")

print()
