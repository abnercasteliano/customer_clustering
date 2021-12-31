# Customer Segmentation - Clustering

<p align="center"><img src="images/customer.png" height="500" width="800"></p>

O objetivo do projeto é fazer uma análise exploratória dos dados da empresa, a fim de identificar possíveis grupos de clientes (clusterização).

O Dataset utilizado no projeto ("customer_data.csv") pode ser encontrado no Kaggle e contém os dados de aproximadamente 8950 clientes de uma empresa.

## Resumo do projeto e considerações

### Análise Exploratória e transformação dos dados

<p align="center"><img src="images/analysis.png" height="500" width="800"></p>

Inicialmente foi feita uma **análise exploratória** e uma **transformação/limpeza** dos dados para remover possíveis valores indesejados. Utilizou-se as técnicas de análise de distribuição e descritiva, pois todas as variáveis do dataset são númericas (não categóricas).

### Machine Learning

<p align="center"><img src="images/ai.png" height="500" width="800"></p>

#### Pré-processamento e clusterização

Antes de iniciar a criação e o teste dos modelos, utilizou-se uma técnica de **feature scaling** para padronizar os dados e melhorar a performance de cada modelo. 
Como os dados estavam altamente dimensionais, foi aplicada uma técnica de redução de dimensionalidade como o PCA (Principal Component Analysis), para reduzir as dimensões e melhorar a eficiência dos modelos de clusterização.
Após o processo de pré-processamento realizou-se a clusterização dos dados. Os algoritmos de cluster foram avaliados atráves da **Silhouette_score**, que avaliou a performance dos modelos **K-means**, **DBSCAN**, **Agglomerative Clustering**, **Mean Shift** e **Spectral Clustering**. Por fim, o algoritmo escolhido para a clusterização foi o **K-means**.

#### Criação do modelo de Classificação

Após concluir a clusterização de identificar os grupos para cada cliente do dataset, foi criado um modelo preditivo supervisionado para classificar automaticamente os clientes por grupos.
Depois de aplicar uma **feature selection** e coletar as variáveis mais relevantes para o classificador, os dados foram divididos em teste e treino através do método **train_test_split**.

Inicialmente os dados foram treinados e validados com o algoritmo **Ridge Classifier**, gerando uma acurácia de 85%.

Posteriormente, os dados foram treinados e testados com o algoritmo **Decision Tree Classifier** e obteve-se uma acurácia de 89%.

Por fim, foi utilizado o algoritmo **Random Forest Classifier** que obteve uma acurácia de 93%.

Neste problema, o algoritmo escolhido para construir o modelo classificador foi o **Random Forest Classifier**, pois obteve o maior F1_score para cada classe, além da maior acurácia.