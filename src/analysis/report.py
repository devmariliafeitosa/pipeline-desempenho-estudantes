import os


def gerar_relatorio(df):

    os.makedirs("reports", exist_ok=True)

    with open("reports/relatorio.txt", "w", encoding="utf-8") as arquivo:

        arquivo.write("RELATÓRIO DA ANÁLISE DOS DADOS\n")
        arquivo.write("=" * 50 + "\n\n")

        arquivo.write(f"Quantidade de linhas: {df.shape[0]}\n")
        arquivo.write(f"Quantidade de colunas: {df.shape[1]}\n\n")

        arquivo.write("COLUNAS DO DATASET\n")
        arquivo.write("-" * 50 + "\n")

        for coluna in df.columns:
            arquivo.write(f"- {coluna}\n")

        arquivo.write("\n")

        arquivo.write("TIPOS DAS COLUNAS\n")
        arquivo.write("-" * 50 + "\n")

        arquivo.write(str(df.dtypes))

        arquivo.write("\n\n")

        arquivo.write("VALORES NULOS\n")
        arquivo.write("-" * 50 + "\n")

        arquivo.write(str(df.isnull().sum()))

        arquivo.write("\n\n")

        arquivo.write("ESTATÍSTICAS DESCRITIVAS\n")
        arquivo.write("-" * 50 + "\n")

        arquivo.write(str(df.describe()))

        arquivo.write("\n\n")

        arquivo.write("DISTRIBUIÇÃO DA BOLSA\n")
        arquivo.write("-" * 50 + "\n")

        arquivo.write(str(df["SCHOLARSHIP"].value_counts().sort_index()))

        arquivo.write("\n\n")

        arquivo.write("DISTRIBUIÇÃO DO GÊNERO\n")
        arquivo.write("-" * 50 + "\n")

        arquivo.write(str(df["GENDER"].value_counts().sort_index()))

        arquivo.write("\n\n")

        arquivo.write("DISTRIBUIÇÃO DO TRABALHO\n")
        arquivo.write("-" * 50 + "\n")

        arquivo.write(str(df["WORK"].value_counts().sort_index()))

    print("\nRelatório salvo em reports/relatorio.txt")