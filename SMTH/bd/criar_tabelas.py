from SMTH.backend.db import Base, engine
from SMTH.bd.models import *

print("Criando tabelas...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
