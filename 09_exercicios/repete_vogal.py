#!/usr/bin/env python3

__version__ = "0.1.0'"
__author__ = 'Júnior (Khaled)'
__license__ = 'Unlicense'

"""
Repete vogais
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.
ex:
python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""

VOGAIS = "aeiouãõâêôáéíóú"

palavras = []

while True:
    palavra = input("Digite uma palavra (ou enter para sair): ").strip()

    if not palavra:
        break

    palavra_final = ""

    for letra in palavra:
        if letra.lower() in VOGAIS:
            palavra_final += letra * 2
        else:
            palavra_final += letra

    palavras.append(palavra_final)

print(*palavras, sep="\n")
