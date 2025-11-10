import pandas as pd

def gerar_resumo_estatistico(df):
    resumo = df.describe(include="all").transpose()
    resumo["missing_values"] = df.isna().sum()
    return resumo
