#!/usr/bin/env python3

__version__ = "0.1.2'"
__author__ = 'Júnior (Khaled)'
__license__ = 'Unlicense'

"""
Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das
condições:
temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
    "ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."
ex:
python3 alerta.py
temperatura: 30
umidade: 90
...
"ALERTA!!! 🥵♒ Perigo de calor úmido"
"""

import logging
import sys

log = logging.Logger("alerta")

try:
    temp = float(input("Qual a tempuratura atual: ").strip())
except ValueError:
    log.error("Temperatura inválida")
    sys.exit(1)
try:
    umid = float(input("Qual a umidade atual: ").strip())
except ValueError:
    log.error("Umidade inválida")
    sys.exit(1)

if (temp > 45):
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif (temp > 30) and ((temp * 3) >= umid):
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif (temp > 30):
    print("ALERTA!!! 🥵♒ Perigo de calor seco")
elif (temp > 10) and (temp <= 30):
    print("😀 Normal")
elif (temp > 0) and (temp <= 10):
    "🥶 Frio"
elif temp <= 0:
    print("ALERTA!!! ⛄ Frio Extremo.")
else:
    print("")
