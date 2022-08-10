#!/usr/bin/env python3

__version__ = "0.1.3'"
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

info = {
    "temperatura": 0.0,
    "umidade": 0.0
}
keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual a {key} atual? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umid = info["umidade"]

if (temp > 45):
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif (temp > 30 and (temp * 3) >= umid):
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif (temp > 10) and (temp <= 30):
    print("😀 Normal")
elif (temp >= 0) and (temp <= 10):
    "🥶 Frio"
elif temp < 0:
    print("ALERTA!!! ⛄ Frio Extremo.")
