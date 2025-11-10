# SMTH/bd/models.py
from datetime import datetime
from SMTH.backend.db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    datasets = db.relationship("Dataset", back_populates="usuario", cascade="all, delete")

class Dataset(db.Model):
    __tablename__ = "datasets"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    nome = db.Column(db.String(200), nullable=False)
    data_upload = db.Column(db.DateTime, default=datetime.utcnow)
    arquivo = db.Column(db.LargeBinary, nullable=False)
    usuario = db.relationship("Usuario", back_populates="datasets")
