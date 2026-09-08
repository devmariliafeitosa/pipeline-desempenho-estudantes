import pandas as pd

df = pd.read_csv("data/processed/dados_limpos_final.csv")

colunas = [
    "GRADE",
    "CUML_GPA",
    "EXP_GPA",
    "STUDY_HRS"
]

print("\n========== ANALISE PARA REGRESSAO ==========")

print("\nRESUMO ESTATISTICO:")
print(df[colunas].describe())

print("\nCORRELACAO ENTRE AS VARIAVEIS:")
print(df[colunas].corr())

print("\nVALORES DE STUDY_HRS:")
print(df["STUDY_HRS"].value_counts().sort_index())

print("\nMEDIA DE GRADE POR STUDY_HRS:")
print(
    df.groupby("STUDY_HRS")["GRADE"]
    .agg(["count", "mean", "std"])
)