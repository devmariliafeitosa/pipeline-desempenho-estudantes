import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score
)
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def avaliar_modelo(nome, modelo, x_teste, y_teste):
    previsoes = modelo.predict(x_teste)

    acuracia = accuracy_score(y_teste, previsoes)
    precisao = precision_score(y_teste, previsoes, zero_division=0)
    recall = recall_score(y_teste, previsoes, zero_division=0)
    f1 = f1_score(y_teste, previsoes, zero_division=0)
    matriz = confusion_matrix(y_teste, previsoes)

    print(f"\n========== {nome} ==========")

    print("\nMatriz de confusao:")
    print(matriz)

    print(f"\nAcuracia: {acuracia:.4f}")
    print(f"Precisao: {precisao:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")

    return {
        "acuracia": acuracia,
        "precisao": precisao,
        "recall": recall,
        "f1": f1,
        "matriz_confusao": matriz
    }


def executar_classificacao():
    print("\n========== CLASSIFICACAO ==========")

    df = pd.read_csv("data/processed/dados_limpos_final.csv")

    df["ALTO_DESEMPENHO"] = (df["GRADE"] >= 4).astype(int)

    x = df[
        [
            "CUML_GPA",
            "EXP_GPA",
            "STUDY_HRS",
            "ATTEND"
        ]
    ]

    y = df["ALTO_DESEMPENHO"]

    print("\nDistribuicao das classes:")
    print(y.value_counts().sort_index())

    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    pipeline_logistica = Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "modelo",
                LogisticRegression(
                    max_iter=1000,
                    random_state=42
                )
            )
        ]
    )

    parametros_logistica = {
        "modelo__C": [0.01, 0.1, 1, 10, 100]
    }

    busca_logistica = GridSearchCV(
        pipeline_logistica,
        parametros_logistica,
        cv=5,
        scoring="f1"
    )

    busca_logistica.fit(x_treino, y_treino)

    print("\nMelhores parametros - Regressao Logistica:")
    print(busca_logistica.best_params_)

    resultado_logistica = avaliar_modelo(
        "REGRESSAO LOGISTICA",
        busca_logistica.best_estimator_,
        x_teste,
        y_teste
    )

    pipeline_knn = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("modelo", KNeighborsClassifier())
        ]
    )

    parametros_knn = {
        "modelo__n_neighbors": [3, 5, 7, 9, 11],
        "modelo__weights": ["uniform", "distance"]
    }

    busca_knn = GridSearchCV(
        pipeline_knn,
        parametros_knn,
        cv=5,
        scoring="f1"
    )

    busca_knn.fit(x_treino, y_treino)

    print("\nMelhores parametros - KNN:")
    print(busca_knn.best_params_)

    resultado_knn = avaliar_modelo(
        "KNN",
        busca_knn.best_estimator_,
        x_teste,
        y_teste
    )

    print("\n========== COMPARACAO ==========")

    if resultado_logistica["f1"] > resultado_knn["f1"]:
        print("Melhor modelo pelo F1-score: Regressao Logistica")
    elif resultado_knn["f1"] > resultado_logistica["f1"]:
        print("Melhor modelo pelo F1-score: KNN")
    else:
        print("Os modelos apresentaram o mesmo F1-score.")

    return {
        "regressao_logistica": resultado_logistica,
        "knn": resultado_knn
    }


if __name__ == "__main__":
    executar_classificacao()