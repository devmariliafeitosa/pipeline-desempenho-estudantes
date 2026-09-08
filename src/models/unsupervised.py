import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def executar_nao_supervisionado():
    print("\n========== PCA E K-MEANS ==========")

    df = pd.read_csv("data/processed/dados_limpos_final.csv")

    colunas = [
        "CUML_GPA",
        "EXP_GPA",
        "STUDY_HRS",
        "READ_FREQ",
        "READ_FREQ_SCI",
        "ATTEND",
        "PREP_STUDY",
        "PREP_EXAM"
    ]

    x = df[colunas]

    scaler = StandardScaler()
    x_padronizado = scaler.fit_transform(x)

    pca = PCA(n_components=2)
    componentes = pca.fit_transform(x_padronizado)

    variancia = pca.explained_variance_ratio_
    variancia_acumulada = np.sum(variancia)

    print("\nVariancia explicada:")
    print(f"PC1: {variancia[0]:.4f}")
    print(f"PC2: {variancia[1]:.4f}")
    print(
        f"Variancia acumulada das duas componentes: "
        f"{variancia_acumulada:.4f}"
    )

    plt.figure(figsize=(10, 6))
    plt.scatter(
        componentes[:, 0],
        componentes[:, 1],
        alpha=0.7
    )

    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.title("Projecao PCA dos estudantes")
    plt.tight_layout()

    plt.savefig("pca projecao.png", dpi=300)
    plt.close()

    inercias = []

    valores_k = range(1, 11)

    for k in valores_k:
        modelo = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        modelo.fit(x_padronizado)
        inercias.append(modelo.inertia_)

    plt.figure(figsize=(10, 6))

    plt.plot(
        list(valores_k),
        inercias,
        marker="o"
    )

    plt.xlabel("Numero de clusters (k)")
    plt.ylabel("Inercia")
    plt.title("Metodo do cotovelo - K-Means")
    plt.xticks(list(valores_k))
    plt.tight_layout()

    plt.savefig("curva cotovelo kmeans.png", dpi=300)
    plt.close()

    k_escolhido = 3

    kmeans = KMeans(
        n_clusters=k_escolhido,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(x_padronizado)

    plt.figure(figsize=(10, 6))

    plt.scatter(
        componentes[:, 0],
        componentes[:, 1],
        c=clusters,
        alpha=0.7
    )

    plt.xlabel("Componente Principal 1")
    plt.ylabel("Componente Principal 2")
    plt.title("Clusters K-Means na projecao PCA")
    plt.tight_layout()

    plt.savefig("clusters kmeans.png", dpi=300)
    plt.close()

    df_clusters = df.copy()
    df_clusters["CLUSTER"] = clusters

    print(f"\nNumero de clusters utilizado: {k_escolhido}")

    print("\nQuantidade de estudantes por cluster:")
    print(df_clusters["CLUSTER"].value_counts().sort_index())

    print("\nPerfil medio dos clusters:")
    print(
        df_clusters.groupby("CLUSTER")[
            colunas + ["GRADE"]
        ].mean().round(2)
    )

    print("\nGraficos gerados:")
    print("pca projecao.png")
    print("curva cotovelo kmeans.png")
    print("clusters kmeans.png")

    return {
        "variancia_pc1": variancia[0],
        "variancia_pc2": variancia[1],
        "variancia_acumulada": variancia_acumulada,
        "k": k_escolhido
    }


if __name__ == "__main__":
    executar_nao_supervisionado()