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

from datetime import datetime
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

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")

        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 50)
    sys.exit()

# TODO: usar Exceptions
if arguments[0] == "new" and len(arguments) == 2:

    print(f"Criando nova nota - {arguments[1]}")
    title = arguments[1]
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
else:
    print("Número de argumentos inválido")
    sys.exit(1)
