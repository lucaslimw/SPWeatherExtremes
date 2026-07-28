from pathlib import Path
import pandas as pd
import re

from config import DATA_DIR


# ------------------------------------------------------
# Identifica qual variável climática é o arquivo
# ------------------------------------------------------

def identificar_variavel(nome_arquivo):

    if "Precip" in nome_arquivo:
        return "Precipitation"

    if "Tmax" in nome_arquivo:
        return "Maximum Temperature"

    if "Tmin" in nome_arquivo:
        return "Minimum Temperature"

    return "Desconhecida"


# ------------------------------------------------------
# Identifica a cidade a partir do nome do arquivo
# ------------------------------------------------------
NOMES_CIDADES = {
    "Campinas": "Campinas",

    "Cordeiro": "Cordeirópolis",
    "Cordeiropolis": "Cordeirópolis",

    "Monte": "Monte Alegre do Sul",
    "MonteAlegre": "Monte Alegre do Sul",

    "Mococa": "Mococa",

    "Pindorama": "Pindorama",

    "Ribeirao": "Ribeirão Preto",

    "SP_": "São Paulo",
    "SaoPaulo": "São Paulo"
}

def identificar_cidade(nome_arquivo):

    cidade = nome_arquivo.replace(".csv", "")
    cidade = cidade.replace("Prob.", "")

    cidade = re.sub(r"Precip", "", cidade)
    cidade = re.sub(r"Tmax", "", cidade)
    cidade = re.sub(r"Tmin", "", cidade)

    cidade = cidade.strip()

    return NOMES_CIDADES.get(cidade, cidade)

# ------------------------------------------------------
# Lê todos os CSVs
# ------------------------------------------------------

def carregar_dados():

    dados = {}

    arquivos = sorted(DATA_DIR.glob("*.csv"))

    for arquivo in arquivos:

        df = pd.read_csv(arquivo)

        cidade = identificar_cidade(arquivo.name)
        variavel = identificar_variavel(arquivo.name)

        dados[(cidade, variavel)] = {
            "dados": df,
            "arquivo": arquivo,
            "cidade": cidade,
            "variavel": variavel
        }

    return dados


# ------------------------------------------------------
# Lista cidades disponíveis
# ------------------------------------------------------

def listar_cidades(dados):

    return sorted(
        list(
            set(cidade for cidade, _ in dados.keys())
        )
    )


# ------------------------------------------------------
# Lista variáveis disponíveis
# ------------------------------------------------------

def listar_variaveis(dados):

    return sorted(
        list(
            set(variavel for _, variavel in dados.keys())
        )
    )

