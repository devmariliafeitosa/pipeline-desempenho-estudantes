# Pipeline de Ciência de Dados – Educação e Perfil dos Estudantes

## Integrantes

- Marília Feitosa

---

## Objetivo

Este projeto tem como objetivo desenvolver um pipeline de Ciência de Dados para realizar a extração, limpeza, análise exploratória e geração de visualizações utilizando o dataset "Higher Education Students Performance Evaluation", disponibilizado no Kaggle.

---

## Estrutura do Projeto

```
pipeline-desempenho-estudantes
│
├── data
│   ├── raw
│   ├── processed
│   └── logs
│
├── outputs
│
├── reports
│
├── src
│   ├── extract
│   ├── analysis
│   ├── transform
│   ├── visualization
│   └── reports
│
├── README.md
└── requirements.txt
```

---

## Tecnologias Utilizadas

- Python
- Pandas
- Matplotlib
- VS Code

---

## Pipeline

O pipeline executa automaticamente as seguintes etapas:

1. Carregamento dos dados.
2. Validação do arquivo.
3. Limpeza dos dados.
4. Tratamento de valores nulos.
5. Remoção de registros duplicados.
6. Identificação de possíveis outliers utilizando o método IQR.
7. Análise exploratória dos dados.
8. Geração de gráfico.
9. Geração de relatório.
10. Exportação do conjunto de dados tratado.

---

## Arquivos Gerados

Após executar:

```bash
python src/main.py
```

serão gerados:

- `data/processed/dados_limpos_final.csv`
- `outputs/grafico_bolsa.png`
- `reports/relatorio.txt`
- `data/logs/extractor.log`