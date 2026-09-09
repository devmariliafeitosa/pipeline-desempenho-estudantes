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

Este projeto tem como objetivo desenvolver um pipeline reprodutível de Ciência de Dados capaz de realizar ingestão, limpeza, tratamento, análise exploratória, inferência estatística, modelagem supervisionada, aprendizado não supervisionado, visualização e documentação automática de dados provenientes do dataset **Higher Education Students Performance Evaluation**, disponibilizado na plataforma Kaggle.

Além da implementação computacional, o trabalho aplica conceitos fundamentais de Ciência de Dados, incluindo amostragem, viés de seleção, Bootstrap, intervalos de confiança, testes de permutação, regressão linear múltipla, classificação, PCA, K-Means, inferência causal, variáveis de confusão e princípio do Ceteris Paribus.

---

# Tecnologias Utilizadas

* Python 3
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* VS Code
* Git
* GitHub

---

# Estrutura do Projeto

```text
pipeline-desempenho-estudantes/

├── data/
│   ├── raw/
│   │   └── student_prediction.csv
│   ├── processed/
│   │   └── dados_limpos_final.csv
│   └── logs/
│
├── outputs/
│   └── grafico_bolsa.png
│
├── reports/
│   └── relatorio.txt
│
├── src/
│   ├── analysis/
│   │   ├── eda.py
│   │   └── report.py
│   │
│   ├── extract/
│   │   └── extractor.py
│   │
│   ├── inference/
│   │   ├── bootstrap.py
│   │   └── ab_testing.py
│   │
│   ├── models/
│   │   ├── regression.py
│   │   ├── machine_learning.py
│   │   └── unsupervised.py
│   │
│   ├── transform/
│   │   └── cleaner.py
│   │
│   ├── visualization/
│   │   └── visualize.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── distribuicao bootstrap.png
├── distribuicao permutacao.png
├── curva cotovelo kmeans.png
├── clusters kmeans.png
├── pca projecao.png
├── Readme.md
└── requirements.txt
```

---

# Funcionamento do Pipeline

O pipeline executa automaticamente as seguintes etapas:

1. Leitura do dataset.
2. Validação do arquivo.
3. Registro das operações em log.
4. Limpeza dos dados.
5. Padronização das variáveis.
6. Tratamento de valores ausentes.
7. Remoção de registros duplicados.
8. Avaliação de possíveis outliers utilizando IQR.
9. Análise Exploratória dos Dados (EDA).
10. Geração automática de relatório.
11. Exportação do conjunto tratado.
12. Geração das visualizações da análise exploratória.
13. Inferência estatística utilizando Bootstrap.
14. Teste A/B utilizando permutação.
15. Regressão linear múltipla.
16. Classificação utilizando Regressão Logística e KNN.
17. Redução de dimensionalidade utilizando PCA.
18. Agrupamento utilizando K-Means.
19. Geração das visualizações das análises estatísticas e dos modelos.

O pipeline completo pode ser executado com:

```bash
python src/main.py
```

---

# Detalhamento das Atividades

## Camada de Ingestão

### População-alvo

A população-alvo ideal corresponde aos estudantes matriculados no ensino superior sobre os quais se deseja realizar inferências relacionadas ao perfil e ao desempenho acadêmico.

O dataset utilizado representa apenas uma amostra dessa população.

### Estrutura de Acesso (Access Frame)

A estrutura de acesso corresponde ao conjunto de estudantes efetivamente presentes no dataset disponibilizado.

O arquivo utilizado contém informações de **145 estudantes**, distribuídas em **33 variáveis**.

Portanto, os dados representam apenas uma amostra da população-alvo e não a população completa.

### Viés de Seleção

O dataset apresenta possíveis riscos de viés de seleção.

Entre eles destacam-se:

* quantidade reduzida de participantes;
* ausência de informações suficientes para garantir uma amostragem representativa de toda a população universitária;
* possível concentração dos estudantes em um contexto acadêmico específico;
* limitações relacionadas à diversidade institucional e geográfica.

Esses fatores podem limitar a capacidade de generalização dos resultados para toda a população de estudantes do ensino superior.

---

# Dicionário de Dados

O conjunto completo utilizado possui **33 colunas**.

As principais variáveis utilizadas nas análises são:

| Variável | Tipo Estatístico | Descrição |
|---|---|---|
| STUDENTID | Categórica | Identificador do estudante |
| AGE | Ordinal | Faixa etária codificada |
| GENDER | Categórica | Gênero do estudante |
| HS_TYPE | Categórica | Tipo de escola de origem |
| SCHOLARSHIP | Ordinal | Nível de bolsa de estudos |
| WORK | Categórica | Situação de trabalho |
| ACTIVITY | Categórica | Participação em atividades extracurriculares |
| PARTNER | Categórica | Situação de relacionamento |
| SALARY | Ordinal | Faixa salarial |
| TRANSPORT | Categórica | Principal meio de transporte |
| LIVING | Categórica | Situação de moradia |
| MOTHER_EDU | Ordinal | Escolaridade da mãe |
| FATHER_EDU | Ordinal | Escolaridade do pai |
| #_SIBLINGS | Discreta | Número/faixa de irmãos |
| KIDS | Categórica | Informação relacionada a filhos |
| MOTHER_JOB | Categórica | Ocupação da mãe |
| FATHER_JOB | Categórica | Ocupação do pai |
| STUDY_HRS | Ordinal | Faixa de horas de estudo |
| READ_FREQ | Ordinal | Frequência de leitura |
| READ_FREQ_SCI | Ordinal | Frequência de leitura científica |
| ATTEND_DEPT | Categórica/ordinal | Frequência ao departamento |
| IMPACT | Categórica | Impacto percebido |
| ATTEND | Categórica/ordinal | Indicador relacionado à frequência |
| PREP_STUDY | Ordinal | Preparação para os estudos |
| PREP_EXAM | Ordinal | Preparação para provas |
| NOTES | Categórica/ordinal | Hábito relacionado a anotações |
| LISTENS | Categórica/ordinal | Indicador relacionado à atenção |
| LIKES_DISCUSS | Categórica/ordinal | Participação em discussões |
| CLASSROOM | Categórica | Ambiente/modalidade de sala |
| CUML_GPA | Ordinal | Faixa de desempenho acadêmico acumulado |
| EXP_GPA | Ordinal | Faixa de desempenho acadêmico esperado |
| COURSE_ID | Categórica | Identificador do curso |
| GRADE | Ordinal | Categoria de desempenho final |

Embora várias dessas variáveis estejam armazenadas numericamente, seus valores representam categorias ou níveis codificados. Portanto, esses códigos não devem ser interpretados automaticamente como variáveis quantitativas contínuas.

---

# Tratamento dos Dados

Durante o processamento foram executadas as seguintes operações:

* remoção de registros duplicados;
* padronização dos nomes das colunas;
* padronização das variáveis textuais;
* tratamento automático de valores ausentes;
* avaliação de possíveis outliers;
* geração do dataset final tratado.

O conjunto tratado é armazenado em:

`data/processed/dados_limpos_final.csv`

Após o processamento, o conjunto permaneceu com:

* **145 registros**;
* **33 colunas**;
* **0 valores nulos**;
* **0 registros duplicados**.

## Tratamento de Valores Ausentes

Embora o conjunto de dados utilizado não apresente valores nulos, o pipeline foi preparado para realizar imputação automática caso sejam encontrados valores ausentes.

A estratégia implementada utiliza:

* mediana para variáveis numéricas;
* moda para variáveis categóricas.

Essa estratégia busca preservar o tamanho da amostra, evitando a remoção automática de registros.

## Impacto em Viés e Variância

A imputação por medidas de tendência central pode evitar perda de observações e reduzir a variabilidade causada pela exclusão de registros.

Entretanto, também pode introduzir viés, pois valores desconhecidos são substituídos por valores representativos da distribuição.

## Método IQR

Foi implementado o método do Intervalo Interquartil (IQR) para avaliação de possíveis valores extremos.

Entretanto, a maioria das variáveis numéricas deste dataset representa categorias ou níveis ordinais codificados.

Aplicar diretamente o IQR a esses códigos poderia classificar categorias válidas como valores extremos.

Por esse motivo, o pipeline identifica essas variáveis e não realiza remoção por IQR sobre os códigos categóricos ou ordinais.

## Consolidação dos Dados

Não foi necessário realizar operações de Merge, pois o dataset utilizado é composto por apenas um arquivo principal.

---

# Análise Exploratória dos Dados

A etapa de Análise Exploratória dos Dados apresenta:

* primeiras linhas do conjunto;
* dimensões;
* tipos das variáveis;
* valores nulos;
* estatísticas descritivas;
* distribuição das bolsas;
* distribuição por gênero;
* distribuição por situação de trabalho.

Também é produzido automaticamente o gráfico:

`outputs/grafico_bolsa.png`

e o relatório:

`reports/relatorio.txt`

---

# Inferência Estatística

## Bootstrap

Para a análise Bootstrap foi utilizada a variável `GRADE` como indicador numérico do desempenho dos estudantes.

Como `GRADE` é originalmente uma variável ordinal codificada, sua utilização como medida numérica representa uma aproximação para fins de análise estatística. Os resultados devem ser interpretados considerando essa limitação.

Foram utilizadas **2.000 réplicas Bootstrap com reposição**.

### Resultados

| Medida | Resultado |
|---|---:|
| Tamanho da amostra | 145 |
| Média amostral | 3,2276 |
| Desvio-padrão amostral | 2,1977 |
| IC Bootstrap 95% | [2,8897; 3,5793] |
| IC Paramétrico 95% | [2,8699; 3,5853] |

Os dois intervalos de confiança apresentaram resultados bastante próximos.

O intervalo Bootstrap foi:

```text
[2,8897; 3,5793]
```

enquanto o intervalo paramétrico foi:

```text
[2,8699; 3,5853]
```

A proximidade entre os intervalos indica que, nesta amostra, as duas abordagens produziram estimativas semelhantes para a média de `GRADE`.

### Teorema Central do Limite

A amostra possui **145 estudantes**.

Esse tamanho amostral contribui para que a distribuição das médias amostrais apresente comportamento aproximadamente normal, conforme esperado pelo Teorema Central do Limite.

Entretanto, é necessário considerar que `GRADE` representa uma variável ordinal codificada e não uma variável genuinamente contínua.

O gráfico da distribuição das médias Bootstrap é salvo como:

`distribuicao bootstrap.png`

---

# Teste A/B por Permutação

Para o teste A/B foram utilizados os dois grupos existentes na variável `WORK`.

A variável de desempenho utilizada na comparação foi `GRADE`.

Foram definidas as seguintes hipóteses:

**H0:** não existe diferença entre as médias de `GRADE` dos dois grupos.

**H1:** existe diferença entre as médias de `GRADE` dos dois grupos.

O nível de significância adotado foi:

```text
α = 0,05
```

Foram realizadas **2.000 permutações aleatórias dos rótulos dos grupos**.

## Resultados

| Medida | Resultado |
|---|---:|
| Grupo A (`WORK = 1`) | 49 estudantes |
| Grupo B (`WORK = 2`) | 96 estudantes |
| Média do Grupo A | 2,7143 |
| Média do Grupo B | 3,4896 |
| Diferença observada | -0,7753 |
| p-valor bilateral | 0,0540 |

Como:

```text
p = 0,0540 > 0,05
```

a decisão estatística é **não rejeitar H0**.

Portanto, considerando um nível de significância de 5%, não há evidência estatística suficiente para concluir que exista diferença entre as médias de `GRADE` dos dois grupos analisados.

Isso não significa que os grupos sejam necessariamente iguais. Significa apenas que a evidência encontrada nesta amostra não foi suficiente para rejeitar a hipótese nula utilizando o critério estabelecido.

A distribuição nula obtida pelas permutações é salva como:

`distribuicao permutacao.png`

---

# Regressão Linear Múltipla

Na regressão linear múltipla foi definida:

**Variável resposta:**

`GRADE`

**Preditores:**

* `CUML_GPA`
* `EXP_GPA`

O modelo estimado foi:

```text
GRADE = 1,5818 + (0,5547 × CUML_GPA) - (0,0239 × EXP_GPA)
```

## Coeficientes

| Coeficiente | Resultado |
|---|---:|
| β0 - Intercepto | 1,5818 |
| β1 - CUML_GPA | 0,5547 |
| β2 - EXP_GPA | -0,0239 |

## Métricas

| Métrica | Resultado |
|---|---:|
| R² | 0,0614 |
| RMSE | 2,0771 |

O R² de **0,0614** indica que o modelo explicou aproximadamente **6,14% da variação de `GRADE` observada no conjunto de teste**.

Esse resultado demonstra baixo poder explicativo para a combinação de variáveis utilizada.

O RMSE foi de aproximadamente **2,08 unidades na escala codificada de `GRADE`**.

## Interpretação Ceteris Paribus

Para `CUML_GPA`, mantendo `EXP_GPA` constante, o aumento de uma unidade está associado a uma variação média de aproximadamente:

```text
+0,5547 em GRADE
```

Para `EXP_GPA`, mantendo `CUML_GPA` constante, o aumento de uma unidade está associado a uma variação média de aproximadamente:

```text
-0,0239 em GRADE
```

O coeficiente de `EXP_GPA` ficou muito próximo de zero, indicando pequena contribuição linear adicional dessa variável quando `CUML_GPA` já está presente no modelo.

Essas interpretações representam **associações estatísticas** e não relações causais.

---

# Machine Learning – Classificação

Para realizar a classificação binária foi criada a variável:

`ALTO_DESEMPENHO`

A classificação foi definida da seguinte forma:

```text
GRADE de 0 a 3 → classe 0
GRADE de 4 a 7 → classe 1
```

A distribuição encontrada foi:

| Classe | Quantidade |
|---|---:|
| 0 | 88 |
| 1 | 57 |

Foram utilizados os seguintes preditores:

* `CUML_GPA`
* `EXP_GPA`
* `STUDY_HRS`
* `ATTEND`

As variáveis foram padronizadas utilizando `StandardScaler`.

Foram comparados dois algoritmos:

* Regressão Logística;
* K-Nearest Neighbors (KNN).

A busca dos melhores hiperparâmetros foi realizada utilizando `GridSearchCV` com validação cruzada de **5 partes**, utilizando o **F1-score** como critério.

---

## Regressão Logística

O melhor valor encontrado para o hiperparâmetro foi:

```text
C = 1
```

### Matriz de Confusão

```text
[[16  2]
 [ 8  3]]
```

### Métricas

| Métrica | Resultado |
|---|---:|
| Acurácia | 0,6552 |
| Precisão | 0,6000 |
| Recall | 0,2727 |
| F1-score | 0,3750 |

A Regressão Logística apresentou acurácia de aproximadamente **65,52%**.

Entretanto, o recall da classe positiva foi de apenas **27,27%**, indicando dificuldade para identificar estudantes pertencentes à classe de alto desempenho.

---

## KNN

Os melhores hiperparâmetros encontrados foram:

```text
n_neighbors = 9
weights = distance
```

### Matriz de Confusão

```text
[[10  8]
 [10  1]]
```

### Métricas

| Métrica | Resultado |
|---|---:|
| Acurácia | 0,3793 |
| Precisão | 0,1111 |
| Recall | 0,0909 |
| F1-score | 0,1000 |

---

## Comparação dos Modelos

A Regressão Logística apresentou desempenho superior ao KNN.

O principal critério utilizado foi o F1-score:

```text
Regressão Logística = 0,3750
KNN                 = 0,1000
```

Portanto, entre os dois modelos avaliados, a **Regressão Logística foi considerada o melhor modelo**.

Apesar disso, seu desempenho ainda é limitado, principalmente devido ao baixo recall.

Por esse motivo, o modelo não deve ser utilizado isoladamente para decisões acadêmicas de alto impacto.

---

# Aprendizado Não Supervisionado

## PCA – Análise de Componentes Principais

Foi utilizada PCA para reduzir a dimensionalidade das variáveis acadêmicas selecionadas.

As variáveis utilizadas foram:

* `CUML_GPA`
* `EXP_GPA`
* `STUDY_HRS`
* `READ_FREQ`
* `READ_FREQ_SCI`
* `ATTEND`
* `PREP_STUDY`
* `PREP_EXAM`

Antes da aplicação do PCA, os dados foram padronizados utilizando `StandardScaler`.

Foram analisadas as duas primeiras componentes principais.

## Variância Explicada

| Componente | Variância explicada |
|---|---:|
| PC1 | 24,47% |
| PC2 | 19,41% |
| PC1 + PC2 | 43,88% |

As duas primeiras componentes principais preservam aproximadamente **43,88% da variabilidade total** das variáveis utilizadas.

Portanto, a projeção bidimensional permite visualizar parte importante da estrutura dos dados, mas não representa toda a informação disponível no espaço original.

O gráfico correspondente é salvo como:

`pca projecao.png`

---

# K-Means

Após a padronização das variáveis, foi utilizado o algoritmo K-Means para identificar grupos de estudantes com características semelhantes.

O método do cotovelo foi utilizado para analisar a relação entre o número de clusters e a inércia.

Foi adotado:

```text
k = 3
```

## Distribuição dos Clusters

| Cluster | Quantidade de estudantes |
|---|---:|
| 0 | 24 |
| 1 | 58 |
| 2 | 63 |

## Perfil Médio

| Cluster | CUML_GPA | EXP_GPA | STUDY_HRS | GRADE |
|---|---:|---:|---:|---:|
| 0 | 3,42 | 2,96 | 3,12 | 3,33 |
| 1 | 2,07 | 2,00 | 1,83 | 2,53 |
| 2 | 3,98 | 3,30 | 2,19 | 3,83 |

### Cluster 0

Apresentou desempenho acadêmico médio intermediário e a maior média de `STUDY_HRS` entre os três grupos.

### Cluster 1

Apresentou as menores médias de:

* `CUML_GPA`;
* `EXP_GPA`;
* `GRADE`.

Esse cluster representa o grupo com os menores indicadores acadêmicos médios entre os três grupos encontrados.

### Cluster 2

Apresentou as maiores médias de:

* `CUML_GPA`;
* `EXP_GPA`;
* `GRADE`.

Esse cluster representa o grupo com os maiores indicadores médios de desempenho acadêmico.

É importante destacar que os clusters representam **perfis identificados pelo algoritmo**, não categorias naturais ou relações causais comprovadas.

Os gráficos produzidos são:

* `curva cotovelo kmeans.png`
* `clusters kmeans.png`

---

# Análise de Domínio – Inferência Causal e Ceteris Paribus

## Correlação não implica causalidade

Mesmo quando uma análise estatística identifica associação entre duas variáveis, isso não significa que uma variável cause diretamente alterações na outra.

O presente estudo utiliza dados observacionais, sem intervenção experimental.

Por esse motivo, não é possível isolar completamente todos os fatores externos que podem influenciar simultaneamente as variáveis analisadas.

Assim, os resultados da regressão, classificação, teste de permutação e agrupamento devem ser interpretados como **associações ou padrões estatísticos**, e não como comprovação de relações de causa e efeito.

---

## Variáveis de Confusão

Diversos fatores podem atuar como variáveis de confusão nas relações envolvendo hábitos acadêmicos e desempenho.

Entre eles:

* condição socioeconômica;
* desempenho acadêmico anterior;
* necessidade de trabalhar;
* escolaridade dos pais;
* curso frequentado;
* disponibilidade de tempo para estudo;
* frequência às aulas;
* preparação para provas;
* carga horária acadêmica;
* oportunidades de estágio;
* características individuais não observadas.

Por exemplo, um estudante pode apresentar maior desempenho e também estudar mais horas.

Entretanto, isso não significa necessariamente que apenas o número de horas de estudo seja responsável pelo maior desempenho.

Outros fatores podem influenciar simultaneamente as duas características.

---

## Relação entre Bolsa e Trabalho

Uma relação de interesse presente no dataset envolve:

* `SCHOLARSHIP` – nível de bolsa;
* `WORK` – situação de trabalho.

A hipótese conceitual considera que estudantes com maior apoio financeiro poderiam apresentar menor necessidade de exercer atividade profissional durante a graduação.

Entretanto, mesmo que seja observada associação entre essas variáveis, não seria correto concluir diretamente que a bolsa causou a mudança na situação de trabalho.

Fatores socioeconômicos podem influenciar simultaneamente o recebimento de bolsa e a necessidade de trabalhar.

---

## Ceteris Paribus

Segundo o princípio do **Ceteris Paribus**, o efeito associado a uma variável deve ser analisado mantendo os demais fatores constantes.

Esse princípio foi aplicado na interpretação da regressão linear múltipla.

Por exemplo, o coeficiente de `CUML_GPA` foi interpretado mantendo `EXP_GPA` constante.

Em um cenário ideal para analisar causalidade, estudantes comparados deveriam possuir condições semelhantes em relação a fatores como:

* idade;
* gênero;
* condição socioeconômica;
* curso;
* instituição;
* carga horária;
* desempenho anterior;
* oportunidades de trabalho.

Mesmo com controles estatísticos, dados observacionais não permitem estabelecer automaticamente causalidade.

Para análises causais mais robustas poderiam ser utilizadas técnicas como:

* experimentos controlados;
* regressão com variáveis de controle;
* pareamento;
* Propensity Score Matching.

---

# Aplicação Operacional dos Resultados

Os resultados obtidos podem ser utilizados de forma exploratória para apoiar análises acadêmicas.

O K-Means, por exemplo, identificou um grupo de estudantes, representado pelo **Cluster 1**, com menores médias de `CUML_GPA`, `EXP_GPA` e `GRADE`.

Esse grupo poderia servir como ponto de partida para investigar possíveis necessidades de acompanhamento acadêmico.

A Regressão Logística também pode ser utilizada como ferramenta exploratória para identificação de padrões associados ao desempenho.

Entretanto, o modelo apresentou recall de apenas **27,27%** para a classe de alto desempenho.

Por esse motivo, as previsões não devem ser utilizadas isoladamente para decisões que afetem diretamente os estudantes.

Uma aplicação adequada seria utilizar os modelos como ferramentas complementares para:

* identificar padrões;
* direcionar análises posteriores;
* apoiar estudos acadêmicos;
* identificar grupos que mereçam investigação adicional.

---

# Visualização Científica – Integridade Visual

O pipeline gera automaticamente gráficos utilizados na interpretação das diferentes etapas da análise.

Durante o desenvolvimento foram adotados princípios de integridade visual:

* utilização de títulos claros e objetivos;
* identificação dos eixos;
* escalas proporcionais;
* representação fiel dos valores observados;
* ausência de manipulação visual que possa induzir interpretações equivocadas;
* apresentação das distribuições estatísticas relevantes.

Essas práticas contribuem para maior transparência na comunicação dos resultados.

---

# Arquivos Gerados

Após executar:

```bash
python src/main.py
```

são produzidos ou atualizados automaticamente:

### Dataset tratado

```text
data/processed/dados_limpos_final.csv
```

### Análise Exploratória

```text
outputs/grafico_bolsa.png
reports/relatorio.txt
data/logs/extractor.log
```

### Inferência Estatística

```text
distribuicao bootstrap.png
distribuicao permutacao.png
```

### Aprendizado Não Supervisionado

```text
pca projecao.png
curva cotovelo kmeans.png
clusters kmeans.png
```

---

# Reprodutibilidade

## 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Acessar a pasta:

```bash
cd pipeline-desempenho-estudantes
```

## 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

## 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 5. Executar o pipeline

```bash
python src/main.py
```

O pipeline utiliza sementes aleatórias fixas nas etapas estatísticas e de Machine Learning que envolvem aleatoriedade, contribuindo para a reprodutibilidade dos resultados.

---

# Limitações

O projeto apresenta algumas limitações importantes:

* o conjunto possui apenas 145 estudantes;
* várias variáveis são categorias ou níveis representados numericamente;
* `GRADE` é originalmente uma variável ordinal;
* algumas análises utilizam `GRADE` numericamente como aproximação;
* a regressão apresentou baixo poder explicativo;
* o modelo de classificação apresentou baixo recall;
* as duas primeiras componentes do PCA representam apenas 43,88% da variabilidade;
* o conjunto é observacional;
* podem existir variáveis de confusão não observadas;
* os resultados não devem ser generalizados automaticamente para toda a população universitária.

Essas limitações devem ser consideradas na interpretação das análises.

---

# Conclusão

O projeto implementou um pipeline reprodutível de Ciência de Dados aplicado à análise do desempenho de estudantes do ensino superior.

A etapa inicial contemplou ingestão, limpeza, tratamento, análise exploratória, visualização e geração automática de relatório.

Na inferência estatística, os intervalos de confiança Bootstrap e paramétrico apresentaram resultados próximos. O intervalo Bootstrap de 95% foi de **[2,8897; 3,5793]**, enquanto o intervalo paramétrico foi de **[2,8699; 3,5853]**.

O teste de permutação apresentou **p = 0,0540**. Dessa forma, considerando nível de significância de 5%, não foi possível rejeitar a hipótese nula.

Na regressão linear múltipla, o modelo apresentou **R² = 0,0614**, indicando baixo poder explicativo para as variáveis utilizadas.

Na classificação, a Regressão Logística apresentou desempenho superior ao KNN, com F1-score de **0,3750**, contra **0,1000** do KNN. Entretanto, o baixo recall demonstra que ainda existe espaço significativo para melhoria do modelo.

Na análise não supervisionada, as duas primeiras componentes do PCA explicaram **43,88% da variabilidade**, enquanto o K-Means identificou **três grupos de estudantes** com diferentes perfis acadêmicos médios.

Os resultados demonstram como técnicas de inferência estatística, aprendizado supervisionado e aprendizado não supervisionado podem ser integradas em um único pipeline de Ciência de Dados.

Entretanto, devido às limitações da amostra e à natureza observacional dos dados, os resultados devem ser interpretados como padrões e associações estatísticas, e não como evidências definitivas de causalidade.