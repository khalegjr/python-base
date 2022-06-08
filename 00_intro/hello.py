#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada, ex:

    export LANG=pt_BR

Ou informe através do CLI argument '--lang'

Ou o usuário terá que digitar a linguagem desejada.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Júnior (Khaled)"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: logging
        print("[Error] {e}")
        print("You need to use `=`")
        print("try with --key=value")
        sys.exit(1)
    
    key = key.lstrip("-").strip()
    value = value.strip()

    # Validação
    if key not in arguments:
        print(f"Argumento inválido: {key}")
        sys.exit(1)
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: usar repetições
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "Choose a language: "
        )

current_language = current_language[:5]
# dicts tem Hash Tables - O(1)
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
    "de_DE": "Hallo Welt!"
}

# # LBYL
# if current_language in msg:
#     message = msg[current_language]
# else:
#     print(f"Language is invalid, choose from: {list(msg.keys())}")
#     sys.exit(1)

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[Error] {e}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

# Usando a estrutura de dados do dicionário
# try com valor default
# message = msg.get(current_language, msg["en_US"])

print((message + "\n") * int(arguments["count"]))
