import pandas as pd

df = pd.read_csv("data/processed/dados_limpos_final.csv")

print("\n========== ANALISE DA VARIAVEL WORK ==========")

print("\nValores encontrados:")
print(sorted(df["WORK"].unique()))

print("\nQuantidade por categoria:")
print(df["WORK"].value_counts().sort_index())

print("\nMedia de GRADE por categoria de WORK:")
print(df.groupby("WORK")["GRADE"].agg(["count", "mean", "std"]))