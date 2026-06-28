import os
import logging
import pandas as pd


logging.basicConfig(
    filename="data/logs/extractor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def carregar_dados():

    caminho = "data/raw/student_prediction.csv"

    if not os.path.exists(caminho):

        logging.error("Arquivo não encontrado.")

        print("Arquivo não encontrado.")

        return None

    try:

        df = pd.read_csv(caminho)

        print("\n========== INGESTÃO ==========")

        print(f"Arquivo encontrado.")

        print(f"Linhas: {df.shape[0]}")

        print(f"Colunas: {df.shape[1]}")

        logging.info(f"Arquivo carregado.")

        logging.info(f"Linhas: {df.shape[0]}")

        logging.info(f"Colunas: {df.shape[1]}")

        return df

    except Exception as erro:

        logging.error(erro)

        print(erro)

        return None