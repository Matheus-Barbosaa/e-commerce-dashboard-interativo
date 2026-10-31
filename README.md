# E-commerce Dashboard Interativo

Este projeto representa a evolução do meu primeiro trabalho de análise de dados, o **E-commerce Data Analysis**.

Na primeira etapa, desenvolvi uma análise exploratória dos dados, trabalhando com preparação de dados, estatística e visualizações gráficas.

Nesta segunda etapa, avanço no desenvolvimento de visualizações interativas com **Plotly** e na construção de um dashboard web utilizando **Dash**, com componentes HTML para estruturar e organizar a apresentação dos gráficos no navegador.

Também desenvolvi uma organização modular das funções gráficas em Python, permitindo reutilizá-las tanto no Jupyter Notebook quanto na aplicação Dash.

O objetivo é aprofundar meus conhecimentos em análise de dados, visualização avançada, desenvolvimento web aplicado a dados e organização de projetos em Python.

## Objetivo

Desenvolver um dashboard interativo para explorar e visualizar informações de um conjunto de dados de e-commerce, utilizando Python, Plotly e Dash.

O projeto busca aplicar conceitos de análise de dados e visualização avançada, organizar funções gráficas reutilizáveis e apresentar os resultados de forma clara e interativa no navegador.

## Tecnologias Utilizadas

- **Python:** linguagem utilizada no desenvolvimento do projeto.
- **Pandas:** carregamento e manipulação dos dados.
- **Plotly Express:** criação das visualizações gráficas.
- **Dash:** desenvolvimento do dashboard interativo.
- **HTML:** estruturação e organização dos elementos visuais da aplicação.
- **Jupyter Notebook:** desenvolvimento e visualização dos gráficos durante a análise.

## Desenvolvimento do Projeto

O desenvolvimento foi realizado em etapas, dando continuidade ao projeto anterior de análise de dados de e-commerce.

1. **Organização dos dados:** carregamento do conjunto de dados utilizando Pandas.
2. **Desenvolvimento dos gráficos:** criação de sete visualizações utilizando Plotly Express.
3. **Organização do código:** criação do módulo `graficos.py`, reunindo as funções responsáveis pelas visualizações.
4. **Jupyter Notebook:** importação e reutilização das funções para visualizar os gráficos individualmente.
5. **Dashboard interativo:** integração das funções ao Dash, com organização dos gráficos em seções temáticas e apresentação no navegador.

Essa organização permite reutilizar o código e manter as visualizações centralizadas em um único módulo Python.

## Visualizações Desenvolvidas

O projeto conta com sete visualizações gráficas, organizadas em três grupos de análise:

### 1. Distribuição e Características dos Produtos

- **Histograma:** distribuição das notas dos produtos.
- **Gráfico de Barras:** quantidade de produtos por gênero.
- **Gráfico de Pizza:** distribuição dos produtos por quantidade vendida.

### 2. Análise de Preços e Vendas

- **Gráfico de Dispersão:** relação entre preço e quantidade vendida.
- **Gráfico de Densidade:** distribuição dos preços dos produtos.
- **Gráfico de Regressão:** análise da relação entre preço e quantidade vendida, com linha de tendência.

### 3. Análise de Correlação

- **Mapa de Calor (Heatmap):** visualização da correlação entre as variáveis selecionadas.

## Estrutura do Projeto

```text
e-commerce-dashboard-interativo/
│
├── data/
│   └── raw/
│       └── ecommerce_estatistica.csv
│
├── notebooks/
│   └── dashboard_interativo.ipynb
│
├── src/
│   ├── app.py
│   └── graficos.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

- `data/raw`: armazena o conjunto de dados original.
- `notebooks`: contém o Jupyter Notebook utilizado para desenvolver e visualizar os gráficos.
- `src`: reúne os arquivos Python responsáveis pelas funções gráficas e pela aplicação Dash.
- `requirements.txt`: lista as bibliotecas necessárias para executar o projeto.
- `.gitignore`: define os arquivos e pastas que não devem ser enviados ao GitHub.

## Como Executar o Projeto

Para executar o projeto localmente, siga as etapas abaixo:

1. Clone este repositório do GitHub.
2. Acesse a pasta do projeto.
3. Crie e ative um ambiente virtual Python.
4. Instale as dependências utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. Execute a aplicação Dash:

```bash
python src/app.py
```

6. Abra o endereço abaixo no navegador:

```text
http://127.0.0.1:8050/
```

O dashboard será exibido localmente no navegador.

## Aprendizados

Durante o desenvolvimento deste projeto, aprofundei meus conhecimentos em:

- Criação de visualizações avançadas utilizando Plotly Express.
- Desenvolvimento de dashboards interativos com Dash.
- Utilização de componentes HTML na organização de aplicações web.
- Criação e reutilização de funções em módulos Python.
- Integração entre Jupyter Notebook e aplicações Dash.
- Organização e estruturação de projetos Python.
- Apresentação de informações e relações entre variáveis por meio de gráficos.

Este projeto contribuiu para minha evolução prática em Python, análise de dados e visualização de informações.
