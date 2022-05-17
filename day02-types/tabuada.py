#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.
---Tabuada do 1---
     1 x 2 = 2
     1 x 3 = 3
     1 x 1 = 1
...
###################
---Tabuada do 2---
     2 x 1 = 2
     2 x 2 = 4
     2 x 3 = 6
...
###################
...
"""
__version__ = "0.1.1"
__author__ = "Júnior (Khaled)"

template_base = """
---Tabuada do 1---
     
     {bloco:^}

###################
"""

# bases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bases = list(range(1,11))
bloco = ""

for base in bases:
    print("{:-^18}".format(f"Tabuada do {base}"))
    print()
    for fator in bases:
        resultado = base * fator
        print("{:^18}".format(f"{base} X {fator} = {resultado}\n"))
    
    print('#' * 18)
