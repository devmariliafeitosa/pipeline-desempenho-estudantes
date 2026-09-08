import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def executar_bootstrap():
    print("\n========== BOOTSTRAP ==========")

    caminho = "data/processed/dados_limpos_final.csv"

    df = pd.read_csv(caminho)

    dados = df["GRADE"].dropna().to_numpy()

    n = len(dados)

    media_amostral = np.mean(dados)
    desvio_padrao = np.std(dados, ddof=1)

    print(f"Tamanho da amostra: {n}")
    print(f"Media amostral: {media_amostral:.4f}")
    print(f"Desvio-padrao amostral: {desvio_padrao:.4f}")

    rng = np.random.default_rng(42)

    numero_replicas = 2000

    medias_bootstrap = []

    for _ in range(numero_replicas):
        amostra = rng.choice(dados, size=n, replace=True)
        medias_bootstrap.append(np.mean(amostra))

    medias_bootstrap = np.array(medias_bootstrap)

    limite_inferior_bootstrap = np.percentile(
        medias_bootstrap,
        2.5
    )

    limite_superior_bootstrap = np.percentile(
        medias_bootstrap,
        97.5
    )

    erro_padrao = desvio_padrao / np.sqrt(n)

    limite_inferior_parametrico = (
        media_amostral - 1.96 * erro_padrao
    )

    limite_superior_parametrico = (
        media_amostral + 1.96 * erro_padrao
    )

    print("\nIntervalo de confianca Bootstrap 95%:")
    print(
        f"[{limite_inferior_bootstrap:.4f}, "
        f"{limite_superior_bootstrap:.4f}]"
    )

    print("\nIntervalo de confianca Parametrico 95%:")
    print(
        f"[{limite_inferior_parametrico:.4f}, "
        f"{limite_superior_parametrico:.4f}]"
    )

    plt.figure(figsize=(10, 6))

    plt.hist(
        medias_bootstrap,
        bins=30,
        edgecolor="black",
        alpha=0.7
    )

    plt.axvline(
        limite_inferior_bootstrap,
        linestyle="--",
        label="Bootstrap 2,5%"
    )

    plt.axvline(
        limite_superior_bootstrap,
        linestyle="--",
        label="Bootstrap 97,5%"
    )

    plt.axvline(
        limite_inferior_parametrico,
        linestyle=":",
        label="Parametrico inferior"
    )

    plt.axvline(
        limite_superior_parametrico,
        linestyle=":",
        label="Parametrico superior"
    )

    plt.xlabel("Media de GRADE")
    plt.ylabel("Frequencia")
    plt.title("Distribuicao das medias Bootstrap")

    plt.legend()
    plt.tight_layout()

    nome_grafico = "distribuicao bootstrap.png"

    plt.savefig(nome_grafico, dpi=300)
    plt.close()

    print(f"\nGrafico salvo em: {nome_grafico}")

    return {
        "media": media_amostral,
        "desvio_padrao": desvio_padrao,
        "ic_bootstrap": (
            limite_inferior_bootstrap,
            limite_superior_bootstrap
        ),
        "ic_parametrico": (
            limite_inferior_parametrico,
            limite_superior_parametrico
        )
    }


if __name__ == "__main__":
    executar_bootstrap()