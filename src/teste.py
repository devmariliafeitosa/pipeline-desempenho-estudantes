import pandas as pd

df = pd.read_csv("data/processed/dados_limpos_final.csv")

df["ALTO_DESEMPENHO"] = (df["GRADE"] >= 4).astype(int)

print("\n========== ANALISE PARA CLASSIFICACAO ==========")

print("\nDISTRIBUICAO DA VARIAVEL ALVO:")
print(df["ALTO_DESEMPENHO"].value_counts().sort_index())

print("\nPERCENTUAL:")
print(
    df["ALTO_DESEMPENHO"]
    .value_counts(normalize=True)
    .sort_index()
    * 100
)

print("\nMEDIA DOS PREDITORES POR CLASSE:")
print(
    df.groupby("ALTO_DESEMPENHO")[
        [
            "CUML_GPA",
            "EXP_GPA",
            "STUDY_HRS",
            "ATTEND"
        ]
    ].mean()
)