#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.
Tabuada do 1
1
2
3
...
----------------
Tabuada do 2
2
4
6
...
----------------
...
"""
__version__ = "0.1.0"
__author__ = "Júnior (Khaled)"

# bases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bases = list(range(1,11))

for base in bases:
    print("Tabuada do:", base)

    for fator in bases:
        print(base * fator)
    
    print("----------")