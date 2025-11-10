from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, LargeBinary, func
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    datasets = relationship("Dataset", back_populates="usuario")


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    nome = Column(String, nullable=False)
    data_upload = Column(DateTime(timezone=True), server_default=func.now())
    arquivo = Column(LargeBinary, nullable=False)

    usuario = relationship("Usuario", back_populates="datasets")
