import pandas as pd


def limpar_dados(df):

    print("\n========== LIMPEZA DOS DADOS ==========")

    linhas_antes = df.shape[0]

    # Remove registros duplicados
    df = df.drop_duplicates()

    # Colunas de texto
    colunas_texto = df.select_dtypes(include=["object", "string"]).columns

    for coluna in colunas_texto:
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # Trata valores nulos
    for coluna in df.columns:

        if pd.api.types.is_numeric_dtype(df[coluna]):

            df[coluna] = df[coluna].fillna(df[coluna].median())

        else:

            if not df[coluna].mode().empty:
                df[coluna] = df[coluna].fillna(df[coluna].mode()[0])

    linhas_depois = df.shape[0]

    print(f"Linhas antes: {linhas_antes}")
    print(f"Linhas depois: {linhas_depois}")

    return df

def remover_outliers_iqr(df):

    print("\n========== IQR ==========")

    colunas_numericas = df.select_dtypes(include="number").columns

    for coluna in colunas_numericas:

        # Ignora colunas com poucos valores distintos
        # (normalmente representam categorias codificadas)
        if df[coluna].nunique() <= 5:
            continue

        q1 = df[coluna].quantile(0.25)
        q3 = df[coluna].quantile(0.75)

        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        quantidade = (
            (df[coluna] < limite_inferior) |
            (df[coluna] > limite_superior)
        ).sum()

        print(f"{coluna}: {quantidade} outlier(s) encontrados.")

        df = df[
            (df[coluna] >= limite_inferior) &
            (df[coluna] <= limite_superior)
        ]

    return df