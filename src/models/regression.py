import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def executar_regressao():
    print("\n========== REGRESSAO LINEAR MULTIPLA ==========")

    df = pd.read_csv("data/processed/dados_limpos_final.csv")

    x = df[["CUML_GPA", "EXP_GPA"]]
    y = df["GRADE"]

    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42
    )

    modelo = LinearRegression()

    modelo.fit(x_treino, y_treino)

    previsoes = modelo.predict(x_teste)

    r2 = r2_score(y_teste, previsoes)

    rmse = mean_squared_error(
        y_teste,
        previsoes
    ) ** 0.5

    beta_0 = modelo.intercept_
    beta_1 = modelo.coef_[0]
    beta_2 = modelo.coef_[1]

    print("\nVariavel resposta:")
    print("Y = GRADE")

    print("\nPreditores:")
    print("X1 = CUML_GPA")
    print("X2 = EXP_GPA")

    print("\nCoeficientes:")
    print(f"Beta 0 - Intercepto: {beta_0:.4f}")
    print(f"Beta 1 - CUML_GPA: {beta_1:.4f}")
    print(f"Beta 2 - EXP_GPA: {beta_2:.4f}")

    print("\nEquacao estimada:")
    print(
        f"GRADE = {beta_0:.4f} "
        f"+ ({beta_1:.4f} * CUML_GPA) "
        f"+ ({beta_2:.4f} * EXP_GPA)"
    )

    print("\nMetricas no conjunto de teste:")
    print(f"R2: {r2:.4f}")
    print(f"RMSE: {rmse:.4f}")

    print("\nInterpretacao dos coeficientes:")

    print(
        f"CUML_GPA: mantendo EXP_GPA constante, "
        f"o aumento de uma unidade em CUML_GPA esta associado "
        f"a uma variacao media de {beta_1:.4f} em GRADE."
    )

    print(
        f"EXP_GPA: mantendo CUML_GPA constante, "
        f"o aumento de uma unidade em EXP_GPA esta associado "
        f"a uma variacao media de {beta_2:.4f} em GRADE."
    )

    return {
        "beta_0": beta_0,
        "beta_1": beta_1,
        "beta_2": beta_2,
        "r2": r2,
        "rmse": rmse
    }


if __name__ == "__main__":
    executar_regressao()