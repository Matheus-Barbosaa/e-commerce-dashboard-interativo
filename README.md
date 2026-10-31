# E-commerce Dashboard Interativo

Este projeto representa a evolução do meu primeiro trabalho de análise de dados, o **E-commerce Data Analysis**.

Na primeira etapa, desenvolvi uma análise exploratória dos dados, trabalhando com preparação de dados, estatística e visualizações gráficas.

Nesta segunda etapa, avanço no desenvolvimento de visualizações interativas com **Plotly** e na construção de um dashboard web utilizando **Dash**, com componentes HTML para estruturar e organizar a apresentação dos gráficos no navegador.

Também desenvolvi uma organização modular das funções gráficas em Python, permitindo reutilizá-las tanto no Jupyter Notebook quanto na aplicação Dash.

O objetivo é aprofundar meus conhecimentos em análise de dados, visualização avançada, desenvolvimento web aplicado a dados e organização de projetos em Python.

---

## 🚀 Acesse o Dashboard Interativo

Explore as visualizações desenvolvidas neste projeto diretamente pelo navegador.

**[Visualizar Dashboard Interativo](https://matheus-barbosaa.github.io/e-commerce-dashboard-interativo/dashboard_interativo.html)**

---

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
│   ├── graficos.py
│   └── gerar_dashboard.py
│
├── dashboard_interativo.html
├── .gitignore
├── README.md
└── requirements.txt
```

- `data/raw`: armazena o conjunto de dados original.
- `notebooks`: contém o Jupyter Notebook utilizado para desenvolver e visualizar os gráficos.
- `src`: reúne os arquivos Python responsáveis pelas funções gráficas, pela aplicação Dash e pela geração do dashboard em HTML.
- `dashboard_interativo.html`: versão HTML dos gráficos, publicada pelo GitHub Pages.
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

## Publicação do Dashboard Interativo

Durante o desenvolvimento deste projeto, identifiquei uma limitação na visualização dos gráficos Plotly diretamente pelo GitHub. Embora o notebook (`.ipynb`) permita visualizar os gráficos durante a execução local, sua pré-visualização no GitHub não apresenta todos os recursos interativos.

Para solucionar essa limitação e permitir que outras pessoas visualizem os resultados do projeto, desenvolvi uma versão do dashboard em HTML e publiquei utilizando o GitHub Pages.

### Por que essa solução foi adotada?

O objetivo foi disponibilizar uma versão pública e interativa do dashboard, permitindo que visitantes do repositório explorem os gráficos sem precisar baixar o projeto ou executar o notebook localmente.

**Acesse o dashboard:**

[Visualizar Dashboard Interativo](https://matheus-barbosaa.github.io/e-commerce-dashboard-interativo/dashboard_interativo.html)

### Processos realizados

Para implementar essa solução, realizei as seguintes etapas:

1. **Identificação da limitação:** verifiquei que a pré-visualização de notebooks no GitHub não apresentava adequadamente a interatividade dos gráficos Plotly.
2. **Análise de alternativas:** busquei formas de disponibilizar os gráficos de maneira interativa para quem acessasse o repositório.
3. **Criação do gerador HTML:** desenvolvi o arquivo `src/gerar_dashboard.py`, responsável por carregar os dados, utilizar as funções de gráficos já criadas e gerar o arquivo HTML.
4. **Organização das visualizações:** mantive os sete gráficos do projeto, distribuídos em três seções:
   - Distribuição e Características dos Produtos;
   - Análise de Preços e Vendas;
   - Análise de Correlação.
5. **Geração do arquivo HTML:** o script exporta o dashboard para `dashboard_interativo.html`, na raiz do projeto.
6. **Publicação no GitHub Pages:** configurei a publicação do arquivo HTML a partir da branch `main`, permitindo o acesso público pelo navegador.
7. **Testes:** verifiquei o funcionamento dos sete gráficos, incluindo recursos de interação, zoom e visualização de informações ao passar o cursor.

### Aprendizado e apoio durante o desenvolvimento

Essa etapa representou um avanço na complexidade do projeto, pois exigiu conhecimentos além da criação e interpretação de gráficos. Foi necessário compreender como gerar um arquivo HTML, organizar as visualizações, trabalhar com caminhos de arquivos, versionar as alterações com Git e realizar a publicação pelo GitHub Pages.

Ao identificar a limitação do GitHub para exibir os gráficos Plotly de forma interativa, recorri ao ChatGPT como ferramenta de apoio para encontrar uma alternativa e desenvolver uma solução que permitisse disponibilizar o dashboard em HTML por meio do GitHub Pages.

Com as orientações recebidas, apliquei os ajustes necessários, acompanhei cada etapa e realizei os testes até conseguir publicar o dashboard e disponibilizar os gráficos interativos para outras pessoas.

Essa experiência também me permitiu aprender, na prática, como superar dificuldades técnicas, utilizar ferramentas de apoio e transformar uma análise desenvolvida em Python em uma apresentação interativa acessível ao público.

**O resultado foi a publicação de um dashboard que permite compartilhar as análises e demonstrar, na prática, os conhecimentos adquiridos em Python, Pandas, Plotly, Dash, HTML e GitHub.**

## Aprendizados

Durante o desenvolvimento deste projeto, aprofundei meus conhecimentos em:

- Criação de visualizações avançadas utilizando Plotly Express.
- Desenvolvimento de dashboards interativos com Dash.
- Utilização de componentes HTML na organização de aplicações web.
- Criação e reutilização de funções em módulos Python.
- Integração entre Jupyter Notebook e aplicações Dash.
- Organização e estruturação de projetos Python.
- Apresentação de informações e relações entre variáveis por meio de gráficos.
- Geração de dashboards em HTML e publicação utilizando GitHub Pages.

Este projeto contribuiu para minha evolução prática em Python, análise de dados e visualização de informações.
