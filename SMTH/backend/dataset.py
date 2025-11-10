# app/backend/dataset.py
import io
import pandas as pd
from SMTH.backend.app import db
from SMTH.bd.models import Dataset
from SMTH.backend.db import db


def validar_dataset(file):
    try:
        df = pd.read_csv(file)
        if df.empty:
            raise ValueError("O arquivo está vazio.")
        return df
    except Exception as e:
        raise ValueError(f"Erro ao processar o dataset: {e}")

def salvar_dataset(usuario_id, nome, df):
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    novo_dataset = Dataset(usuario_id=usuario_id, nome=nome, arquivo=buffer.getvalue())
    db.session.add(novo_dataset)
    db.session.commit()
    return novo_dataset

def carregar_dataset(dataset_id):
    dataset = Dataset.query.get(dataset_id)
    if not dataset:
        raise ValueError("Dataset não encontrado.")
    return pd.read_csv(io.BytesIO(dataset.arquivo))
