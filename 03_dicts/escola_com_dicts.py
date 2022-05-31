#!/usr/bin/env python3
""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"
__author__ = "Júnior (Khaled)"

# Dados
salas = {
    "Sala 1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "Sala 2": ["João", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "Inglês": ['Erik', "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ['Gustavo', "Sofia", "Joana", "Antonio"]
}

# Listar alunos em cada atividade por sala
for nome_aula, alunos_aula in aulas.items():
    print(f"Alunos da atividade {nome_aula}")
    print("-" * 50)

    for sala, alunos_sala in salas.items():
        # sala que tem interseção com a atividade
        alunos_atividade = set(alunos_sala) & set(alunos_aula)
        print(f"{sala}: {alunos_atividade}")
    print()
    print("#" * 50)