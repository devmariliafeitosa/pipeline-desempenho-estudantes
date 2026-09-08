import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def executar_teste_permutacao():
    print("\n========== TESTE A/B POR PERMUTACAO ==========")

    df = pd.read_csv("data/processed/dados_limpos_final.csv")

    grupo_a = df[df["WORK"] == 1]["GRADE"].to_numpy()
    grupo_b = df[df["WORK"] == 2]["GRADE"].to_numpy()

    alpha = 0.05
    numero_permutacoes = 2000

    media_a = np.mean(grupo_a)
    media_b = np.mean(grupo_b)

    diferenca_observada = media_a - media_b

    print("\nHipoteses:")
    print("H0: nao existe diferenca entre as medias de GRADE dos grupos.")
    print("H1: existe diferenca entre as medias de GRADE dos grupos.")

    print(f"\nNivel de significancia: {alpha}")

    print(f"\nTamanho do Grupo A: {len(grupo_a)}")
    print(f"Tamanho do Grupo B: {len(grupo_b)}")

    print(f"\nMedia do Grupo A: {media_a:.4f}")
    print(f"Media do Grupo B: {media_b:.4f}")

    print(f"Diferenca observada: {diferenca_observada:.4f}")

    valores = np.concatenate([grupo_a, grupo_b])

    tamanho_a = len(grupo_a)

    rng = np.random.default_rng(42)

    diferencas_permutadas = []

    for _ in range(numero_permutacoes):
        valores_permutados = rng.permutation(valores)

        grupo_a_permutado = valores_permutados[:tamanho_a]
        grupo_b_permutado = valores_permutados[tamanho_a:]

        diferenca = (
            np.mean(grupo_a_permutado)
            - np.mean(grupo_b_permutado)
        )

        diferencas_permutadas.append(diferenca)

    diferencas_permutadas = np.array(diferencas_permutadas)

    p_valor = (
        np.sum(
            np.abs(diferencas_permutadas)
            >= np.abs(diferenca_observada)
        ) + 1
    ) / (numero_permutacoes + 1)

    print(f"\nP-valor bilateral: {p_valor:.4f}")

    if p_valor < alpha:
        print(
            "Decisao: rejeitar H0. "
            "Existe evidencia de diferenca entre os grupos."
        )
    else:
        print(
            "Decisao: nao rejeitar H0. "
            "Nao ha evidencia suficiente de diferenca entre os grupos."
        )

    plt.figure(figsize=(10, 6))

    plt.hist(
        diferencas_permutadas,
        bins=30,
        edgecolor="black",
        alpha=0.7
    )

    plt.axvline(
        diferenca_observada,
        linestyle="--",
        linewidth=2,
        label=f"Diferenca observada = {diferenca_observada:.4f}"
    )

    plt.axvline(
        -diferenca_observada,
        linestyle="--",
        linewidth=2,
        label="Limite simetrico"
    )

    plt.xlabel("Diferenca entre medias")
    plt.ylabel("Frequencia")
    plt.title("Distribuicao nula do teste de permutacao")

    plt.legend()
    plt.tight_layout()

    nome_grafico = "distribuicao permutacao.png"

    plt.savefig(nome_grafico, dpi=300)
    plt.close()

    print(f"\nGrafico salvo em: {nome_grafico}")

    return {
        "media_grupo_a": media_a,
        "media_grupo_b": media_b,
        "diferenca_observada": diferenca_observada,
        "p_valor": p_valor,
        "alpha": alpha
    }


if __name__ == "__main__":
    executar_teste_permutacao()