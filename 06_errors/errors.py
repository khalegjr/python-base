#!/usr/bin/env python3

import os
import sys

# EAFP - Easier to Ask Forgiveness than Permission
# è mais fácil pedir perdão do que permissão

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1/1 # ZeroDivisionError
    print(names.count) # AttributeError
except (FileNotFoundError, ZeroDivisionError, AttributeError) as e:
    print(f"[Error] {str(e)}")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
