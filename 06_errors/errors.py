#!/usr/bin/env python3
# LBYL: Look Before You Leap



import os
import sys

if os.path.exists("names.txt"):
    print("Arquivo existe")
    input("...") # Race condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)