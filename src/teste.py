import pandas as pd

df = pd.read_csv("data/processed/dados_limpos_final.csv")

print("\n========== VALIDACAO DO DATASET FINAL ==========")

print("\nDIMENSOES:")
print(df.shape)

print("\nVALORES NULOS:")
print(df.isnull().sum().sum())

print("\nLINHAS DUPLICADAS:")
print(df.duplicated().sum())

print("\nVALORES DE GRADE:")
print(sorted(df["GRADE"].unique()))

print("\nDISTRIBUICAO DE GRADE:")
print(df["GRADE"].value_counts().sort_index())

print("\nVALORES DE CUML_GPA:")
print(sorted(df["CUML_GPA"].unique()))

print("\nVALORES DE EXP_GPA:")
print(sorted(df["EXP_GPA"].unique()))