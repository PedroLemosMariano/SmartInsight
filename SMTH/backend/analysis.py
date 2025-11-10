import pandas as pd

def gerar_resumo_estatistico(df: pd.DataFrame):
    """Gera estatísticas descritivas básicas."""
    resumo = df.describe(include="all").transpose()
    resumo["missing_values"] = df.isna().sum()
    return resumo
