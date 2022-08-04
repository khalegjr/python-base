#!/usr/bin/env python3
""" Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"
__author__ = "Júnior (Khaled)"

import os
import sys

cmd = ("read", "new")
path_ = os.curdir
filepath = os.path.join(path_, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Número de argumentos inválido")
    sys.exit(1)

if arguments[0] not in cmd:
    print(f"Comando inválido.\nComandos válidos: {cmd}")
    print("Ex.: new \"Minha Nota\"")
    sys.exit(1)

while True:
    if arguments[0] == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag? ").strip().lower()

        # leitura das notas
        for line in open(filepath):
            title, tag, text = line.split("\t")

            if tag.lower() == arg_tag:
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 50)
        sys.exit()

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError:
            title = input("Qual é o título? ").strip().title()

        print(f"Criando nova nota")
        text = [
            f"{title}",
            input("tag: ").strip(),
            input("text:\n").strip(),
        ]

        # \t - tsv (usando tab para separar os elementos)
        with open(filepath, "a") as f:
            f.write("\t".join(text))
            f.write("\n")

        print("Nota criada com sucesso")

        if input("Quer continuar adicionando notas: [N/y]").strip().lower() != "y":
            break
else:
    print("Número de argumentos inválido")
    sys.exit(1)
