#!/usr/bin/env python3
"""Calculadora do tipo Infix

As operações são passadas como uma string, separadas por espaços. 

Funcionamento: 
[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /
    Ex.:
    sum 7 8 | 7 + 8
    sub 9 3 | 9 - 3
    mul 51 4 | 51 * 4
    div 12 6 | 12 / 6 

Uso:
    $ infixcalc.py sum 5 2
    7

    $ infixcalc.py
    $ operação: sum
    $ n1: 5
    $ n2: 2
    $ 7

Os resultados serão salvos em `inflixcalc.log`
"""
__version__ = "0.1.0"
__author__ = "Júnior (Khaled)"
__license__ = "Unlicense"

from datetime import datetime
import os
import sys

arguments = sys.argv[1:]

# Validação
if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválido")
    print("Ex.: sum 5 5")
    sys.exit(1)

operation, *nums = arguments

valid_operations = {
    "sum": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": lambda x, y: x / y
}

if operation not in valid_operations:
    print(f"Operação inválida: {operation}")
    print(f"Operações válidas: {valid_operations}")
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: repetição while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido: {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)

    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except valueError as e:
    print(e)
    sys.exit(1)

result = valid_operations[operation](n1, n2)

# Criando log da operação
path = os.curdir
filepath = os.path.join(path, "inflixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

print(f"O resultado é: {result}")

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
except PermissionError as e:
    print(str(e))
    sys.exit(1)
