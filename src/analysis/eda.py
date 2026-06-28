import pandas as pd


def analise_exploratoria(df):

    print("\n========== EDA ==========")

    print("\nPrimeiras linhas:")

    print(df.head())

    print("\nInformações gerais:")

    print(df.info())
    print("\nColunas do dataset:")

    for coluna in df.columns:
        print("-", coluna)

    print("\nValores nulos:")

    print(df.isnull().sum())

    print("\nEstatísticas:")

    print(df.describe())

    print("\nDistribuição das bolsas:")

    print(df["SCHOLARSHIP"].value_counts().sort_index())

    print("\nDistribuição por gênero:")

    print(df["GENDER"].value_counts().sort_index())

    print("\nDistribuição por trabalho:")

    print(df["WORK"].value_counts().sort_index())