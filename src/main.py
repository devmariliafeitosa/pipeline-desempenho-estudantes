from extract.extractor import carregar_dados
from transform.cleaner import limpar_dados
from transform.cleaner import remover_outliers_iqr
from visualization.visualize import gerar_grafico
from analysis.eda import analise_exploratoria
from analysis.report import gerar_relatorio

from inference.bootstrap import executar_bootstrap
from inference.ab_testing import executar_teste_permutacao

from models.regression import executar_regressao
from models.machine_learning import executar_classificacao
from models.unsupervised import executar_nao_supervisionado


def main():
    print("\n========== INICIO DO PIPELINE ==========")

    df = carregar_dados()

    if df is None:
        return

    df = limpar_dados(df)

    df = remover_outliers_iqr(df)

    analise_exploratoria(df)

    gerar_relatorio(df)

    df.to_csv(
        "data/processed/dados_limpos_final.csv",
        index=False
    )

    gerar_grafico(df)

    executar_bootstrap()

    executar_teste_permutacao()

    executar_regressao()

    executar_classificacao()

    executar_nao_supervisionado()

    print("\n========== PIPELINE FINALIZADO COM SUCESSO! ==========")


if __name__ == "__main__":
    main()