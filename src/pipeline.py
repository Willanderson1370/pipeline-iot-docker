import pandas as pd
from sqlalchemy import create_engine

# Configuração do banco de dados PostgreSQL
USER = "postgres"
PASSWORD = "sua_senha"
HOST = "localhost"
PORT = "5432"
DB = "iot_db"

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

# Carregar dataset
df = pd.read_csv("data/temperature-readings.csv")

# Inserir no banco
df.to_sql("temperature_readings", engine, if_exists="replace", index=False)

print("Dados inseridos com sucesso!")
