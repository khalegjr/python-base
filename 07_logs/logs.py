#!/usr/bin/env python3

import logging
import os  # stderr root loggin
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Inicio da configuração do log
# nossa instancia de loggin
# setando para o nível de debug
log = logging.Logger("logs.py", log_level)

# level
# ch = logging.StreamHandler()  # Console/terminal/stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=500,  # o recomendado é 10**6 = 1Mb
    backupCount=10,  # número de arquivos mantidos
)
fh.setLevel(log_level)

# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)

# destino
# log.addHandler(ch)
log.addHandler(fh)
# Fim da configuração do log

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução")
log.critical("Erro geral ex: banco de dados sumiu")
"""

# print("---")
try:
    1/0
except ZeroDivisionError as e:

    log.error("Deu erro %s", str(e))
