#!/usr/bin/env python3
"""Exemplo de envio de e-mail

Para criar um servidor de email para teste no Python:
python -m smtpd -c DebuggingServer -n localhost:8025
"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "from@server.org"
TO = ["destino@server.org", "outrodestino@server.org"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo <b>Python</b>.
em>Olá mundo!</em>
"""

# SMTP
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
