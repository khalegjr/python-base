#!/usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200
ex
`python3 numeros_pares.py`
2
4
6
8
...
"""
__version__ = "0.1.1"
__author__ = "Júnior (Khaled)"

for number in range(1, 201):
    if number % 2 != 0:
        continue

    print(number)
