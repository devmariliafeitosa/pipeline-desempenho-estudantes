# Pipeline de Ciência de Dados – Educação e Desempenho dos Estudantes

## Tema

**Educação e Desempenho dos Estudantes**

Dataset utilizado: **Higher Education Students Performance Evaluation**

Arquivo utilizado: `student_prediction.csv`

---

# Integrantes

* Marília Feitosa

---

# Objetivo

Este projeto tem como objetivo desenvolver um pipeline reprodutível de Ciência de Dados capaz de realizar a ingestão, limpeza, tratamento, análise exploratória, visualização e documentação automática de dados provenientes do dataset **Higher Education Students Performance Evaluation**, disponibilizado na plataforma Kaggle.

Além da implementação computacional, o trabalho aplica conceitos fundamentais da Ciência de Dados, incluindo amostragem, viés de seleção, modelagem estatística das variáveis, inferência causal, variáveis de confusão e o princípio do Ceteris Paribus.

---

# Tecnologias Utilizadas

* Python 3
* Pandas
* Matplotlib
* VS Code

---

# Estrutura do Projeto

```
pipeline-desempenho-estudantes/

├── data/
│   ├── raw/
│   ├── processed/
│   └── logs/
│
├── outputs/
│
├── reports/
│
├── src/
│   ├── analysis/
│   ├── extract/
│   ├── transform/
│   ├── visualization/
│   ├── __init__.py
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

# Funcionamento do Pipeline

O pipeline executa automaticamente as seguintes etapas:

1. Leitura do dataset.
2. Validação do arquivo.
3. Registro das operações em log.
4. Limpeza dos dados.
5. Padronização de variáveis.
6. Tratamento de valores ausentes.
7. Remoção de registros duplicados.
8. Identificação de possíveis outliers utilizando IQR.
9. Análise Exploratória dos Dados (EDA).
10. Geração automática de gráficos.
11. Geração automática de relatório em formato TXT.
12. Exportação do conjunto tratado.

---

# Detalhamento das Atividades (Aplicação de Conceitos)

## Camada de Ingestão

### População-alvo

A população-alvo ideal corresponde a todos os estudantes matriculados no ensino superior, independentemente da instituição, curso, localização geográfica ou condição socioeconômica.

Essa população representa o conjunto de indivíduos sobre os quais seria desejável realizar inferências estatísticas relacionadas ao perfil estudantil.

### Estrutura de Acesso (Access Frame)

A estrutura de acesso corresponde ao conjunto de estudantes efetivamente presentes no dataset disponibilizado pelo Kaggle.

O arquivo utilizado contém informações de **145 estudantes**, distribuídas em **10 variáveis**.

Portanto, os dados representam apenas uma amostra da população-alvo e não a população completa.

### Viés de Seleção

O dataset apresenta possíveis riscos de viés de seleção.

Entre eles destacam-se:

* quantidade reduzida de participantes;
* ausência de informações sobre o método de amostragem;
* possível concentração dos estudantes em uma única instituição de ensino;
* ausência de diversidade geográfica conhecida.

Esses fatores podem limitar a capacidade de generalização dos resultados obtidos para toda a população universitária.

---

# Dicionário de Dados

| Variável    | Tipo Estatístico | Descrição                                    |
| ----------- | ---------------- | -------------------------------------------- |
| STUDENTID   | Categórica       | Identificador do estudante                   |
| AGE         | Discreta         | Faixa etária codificada                      |
| GENDER      | Categórica       | Sexo do estudante                            |
| HS_TYPE     | Categórica       | Tipo de escola de origem                     |
| SCHOLARSHIP | Categórica       | Nível de bolsa de estudos                    |
| WORK        | Categórica       | Situação de trabalho                         |
| ACTIVITY    | Categórica       | Participação em atividades extracurriculares |
| PARTNER     | Categórica       | Situação de relacionamento                   |
| SALARY      | Categórica       | Faixa salarial familiar                      |
| TRANSPORT   | Categórica       | Principal meio de transporte                 |

---

# Tratamento dos Dados

Durante o processamento foram executadas as seguintes operações:

* remoção de registros duplicados;
* padronização das variáveis textuais;
* tratamento automático de valores ausentes;
* identificação de possíveis outliers utilizando o método IQR;
* geração do dataset final tratado.

### Tratamento de Valores Ausentes

Embora o conjunto de dados não apresente valores nulos, o pipeline foi preparado para realizar imputação automática.

Caso existissem valores ausentes:

* variáveis numéricas seriam preenchidas pela mediana;
* variáveis categóricas seriam preenchidas pela moda.

Essa estratégia reduz perdas de informação e preserva o tamanho da amostra.

### Impacto em Viés e Variância

A imputação por medidas de tendência central reduz a variância causada pela remoção de registros, porém pode introduzir pequeno aumento de viés ao substituir valores reais por valores representativos.

### Método IQR

Foi implementado o método do Intervalo Interquartil (IQR) para identificação de possíveis valores extremos.

Como a maioria das variáveis deste conjunto de dados representa categorias codificadas, poucos outliers são esperados. Mesmo assim, o algoritmo permanece implementado para garantir a robustez do pipeline em bases futuras contendo variáveis numéricas contínuas.

### Consolidação dos Dados (Merge)

Não foi necessário realizar operações de Merge, pois o dataset utilizado é composto por apenas um arquivo de dados.

---

# Análise de Domínio (Inferência Causal e Ceteris Paribus)

## Relação analisada

Neste trabalho foi escolhida a relação entre as variáveis **SCHOLARSHIP (nível da bolsa de estudos)** e **WORK (situação de trabalho do estudante)**.

A hipótese analisada considera que estudantes contemplados com bolsas de maior valor podem apresentar menor necessidade de exercer atividade profissional durante a graduação.

---

## a) Correlação não implica causalidade

Mesmo que uma análise estatística revele uma forte correlação entre o nível da bolsa e a situação de trabalho, essa associação não constitui evidência suficiente para afirmar uma relação causal.

Correlação indica apenas que duas variáveis apresentam comportamento semelhante, mas não demonstra que uma seja responsável por provocar alterações na outra.

Como o presente estudo utiliza dados observacionais, sem controle experimental, não é possível isolar todos os fatores externos que podem influenciar simultaneamente ambas as variáveis.

Assim, qualquer associação encontrada deve ser interpretada como evidência de relacionamento estatístico e não como comprovação de causa e efeito.

---

## b) Variáveis de Confusão (Confounders)

Duas importantes variáveis de confusão que podem influenciar simultaneamente o nível da bolsa e a necessidade de trabalhar são:

### Renda Familiar

Estudantes provenientes de famílias com menor renda podem possuir maior probabilidade de receber bolsas de auxílio financeiro e, simultaneamente, necessitar exercer atividades profissionais para complementar a renda doméstica.

Caso essa variável não seja controlada, parte do efeito observado poderá ser incorretamente atribuída apenas ao valor da bolsa.

### Custo de Vida

O custo de vida da cidade onde o estudante reside também pode afetar simultaneamente ambas as variáveis.

Mesmo recebendo bolsas elevadas, estudantes residentes em regiões com alto custo de vida podem continuar necessitando trabalhar para custear despesas básicas.

Outros possíveis fatores de confusão incluem:

* escolaridade dos pais;
* modalidade do curso;
* patrimônio familiar;
* oportunidades de estágio;
* carga horária acadêmica.

---

## c) Cenário ideal segundo o princípio do Ceteris Paribus

Segundo o princípio do **Ceteris Paribus**, para avaliar corretamente o efeito da bolsa sobre a necessidade de trabalhar seria necessário comparar estudantes que fossem semelhantes em todas as demais características, diferindo apenas quanto ao valor da bolsa recebida.

Esses estudantes deveriam possuir condições equivalentes em relação à:

* idade;
* gênero;
* renda familiar;
* curso;
* cidade;
* instituição de ensino;
* custo de vida;
* oportunidades de emprego.

Mantendo todos esses fatores constantes, seria possível observar com maior precisão se alterações no nível da bolsa realmente produzem mudanças na necessidade de trabalhar.

Na prática, esse controle pode ser obtido por meio de experimentos controlados ou técnicas de Inferência Causal, como regressão com variáveis de controle, pareamento (Matching) e Propensity Score Matching.

Como este trabalho utiliza dados observacionais, tais conclusões devem ser interpretadas apenas como evidências de associação estatística.

---

# Visualização Científica (Integridade Visual)

O pipeline gera automaticamente gráficos que representam a distribuição dos estudantes segundo o nível de bolsa.

Durante o desenvolvimento foram adotados princípios de Integridade Visual:

* utilização de títulos claros e objetivos;
* identificação dos eixos;
* escalas proporcionais;
* ausência de manipulação visual que possa induzir interpretações equivocadas;
* representação fiel dos valores observados.

Essas práticas garantem maior transparência e confiabilidade na comunicação dos resultados.

---

# Arquivos Gerados

Após executar:

```bash
python src/main.py
```

são produzidos automaticamente:

* `data/processed/dados_limpos_final.csv`
* `outputs/grafico_bolsa.png`
* `reports/relatorio.txt`
* `data/logs/extractor.log`

---

# Conclusão

O projeto implementa um pipeline reprodutível de Ciência de Dados que automatiza desde a ingestão até a geração de relatórios e visualizações.

Além da implementação computacional, o trabalho incorpora conceitos fundamentais da área, como amostragem, viés de seleção, classificação estatística das variáveis, tratamento de dados, Inferência Causal, variáveis de confusão e Ceteris Paribus.

Embora o conjunto de dados represente apenas uma amostra limitada da população de estudantes do ensino superior, o pipeline foi desenvolvido seguindo boas práticas de organização, documentação e reprodutibilidade, permitindo futuras expansões e novas análises.
