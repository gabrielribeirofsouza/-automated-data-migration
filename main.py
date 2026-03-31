import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

# config

CSV_PATH = "data/produtos.csv"
DB_PATH = "database/base_dados.db"
LOG_PATH = "logs/erros.log"
TABLE_NAME = "produtos"



os.makedirs("logs", exist_ok=True)
os.makedirs("database", exist_ok=True)

#converte em tabelas

if CSV_PATH.lower().endswith(".csv"): # VALIDA SE O FINAL DO CAMINHO
    df = pd.read_csv(
        CSV_PATH,
        sep=",",
        engine="python",
        on_bad_lines="skip"
    )

elif CSV_PATH.lower().endswith(".xlsx"):
    df = pd.read_excel(CSV_PATH,
    engine="openpyxl"
)

else:
    raise ValueError("Formato de arquivo não suportado. Use CSV ou XLSX.")

# validações nos registros 

linhas_invalidas = []

for index, row in df.iterrows():
    try:
        if pd.isna(row["nome_produto"]):
            raise ValueError("Nome vazio")

        preco = float(row["preco"])
        estoque = int(row["estoque"])

        df.at[index, "preco"] = preco
        df.at[index, "estoque"] = estoque

    except Exception as erro:
        linhas_invalidas.append((index, str(erro)))

# remove linhas inválidas

df_limpo = df.drop(index=[i[0] for i in linhas_invalidas])



with open(LOG_PATH, "w") as log:
    for linha in linhas_invalidas:
        log.write(f"Linha {linha[0]}: {linha[1]}\n")


df_limpo["data_migracao"] = datetime.now() # pega a data que o script roda



engine = create_engine(f"sqlite:///{DB_PATH}")


# carga

df_limpo.to_sql(
    TABLE_NAME,
    engine,
    if_exists="replace",
    index=False
)


print("Migração concluída!")
print(f"Total de registros no arquivo: {len(df)}")
print(f"Registros válidos: {len(df_limpo)}")
print(f"Registros inválidos: {len(linhas_invalidas)}")
print(f"Banco criado em: {DB_PATH}")