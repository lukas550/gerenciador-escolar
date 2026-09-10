# Módulo para carregar e salvar arquivos em .json

import json

"""
Estrutura do arquivo:
[
    {
        "nome": str
        "notas": [float, float, float],
        "media": float,
        "situacao": bool,
        "informacao": str
    }
]
"""

ARQUIVO = "alunos.json"

def salvar_arquivo(dados_a_salvar):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados_a_salvar, f, ensure_ascii=False, indent=4)

    except (OSError, TypeError) as e:
        print(f"\nErro em salvar o arquivo: {e}\n")

def carregar_arquivo():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)

            return dados

    except FileNotFoundError:
        salvar_arquivo([])

        return []

    except json.JSONDecodeError as e:
        print(f"\nErro em carregar arquivo: {e}\n")