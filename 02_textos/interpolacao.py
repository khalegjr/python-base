#!/usr/bin/env python3
"""Envio mensagem em lista de emails

O usuário passa como primeiro argumento uma lista de emails, separados por
vírgula. E um segundo argumento com um template de mensagem.

Funcionamento:
$ interpolacao.py lista_emails.txt email_tmpl.txt

NÃO MANDE SPAM!!!
"""

__version__ = "0.1.2"
__author__ = "Júnior (Khaled)"

import os
import smtplib
import sys
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
template_name = arguments[1]

path_ = os.curdir
filepath = os.path.join(path_, filename)
template_path = os.path.join(path_, template_name)

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):
        name, email = line.split(",")

        text = (
            open(template_path).read()
            % {
                "name": name,
                "product": "caneta",
                "text": "escrever muito bem",
                "link": "http://www.canetaslegias.com",
                "amount": 10,
                "price": 50.5,
            })

        from_ = "compre@loja.com"
        subject = "Compre mais"
        to = ", ".join([email])

        message = MIMEText(text)
        message["Subject"] = subject
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string())
