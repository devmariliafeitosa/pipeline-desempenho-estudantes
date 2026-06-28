from extract.extractor import carregar_dados
from transform.cleaner import limpar_dados
from transform.cleaner import remover_outliers_iqr
from visualization.visualize import gerar_grafico
from analysis.eda import analise_exploratoria
from analysis.report import gerar_relatorio


def main():

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

    print("\nPipeline finalizado com sucesso!")


if __name__ == "__main__":
    main()