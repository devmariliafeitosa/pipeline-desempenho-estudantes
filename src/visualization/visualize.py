import matplotlib.pyplot as plt


def gerar_grafico(df):

    print("\n========== VISUALIZAÇÃO ==========")

    plt.figure(figsize=(8,5))

    contagem = df["SCHOLARSHIP"].value_counts().sort_index()

    contagem.plot(kind="bar")

    plt.title("Distribuição dos estudantes por nível de bolsa")

    plt.xlabel("Nível da bolsa")

    plt.ylabel("Quantidade de estudantes")

    plt.grid(axis="y")

    plt.tight_layout()

    plt.savefig("outputs/grafico_bolsa.png")

    plt.close()

    print("Gráfico salvo em outputs/grafico_bolsa.png")