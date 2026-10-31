
# Importando as bibliotecas
import pandas as pd
import plotly.io as pio

# Importando as funções dos gráficos
from graficos import (
    cria_grafico_histograma,
    cria_grafico_dispersao,
    cria_grafico_correlacao,
    cria_grafico_genero,
    cria_grafico_pizza,
    cria_grafico_densidade,
    cria_grafico_regressao
)

# Carregamento do dataset
df = pd.read_csv('../data/raw/ecommerce_estatistica.csv')

# Criando os gráficos
fig1 = cria_grafico_histograma(df)
fig2 = cria_grafico_genero(df)
fig3 = cria_grafico_pizza(df)
fig4 = cria_grafico_dispersao(df)
fig5 = cria_grafico_densidade(df)
fig6 = cria_grafico_regressao(df)
fig7 = cria_grafico_correlacao(df)

# Estrutura do dashboard HTML
html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Dashboard Interativo - E-commerce</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #F4F7FB;
            margin: 0;
            padding: 30px;
        }

        h1 {
            text-align: center;
            color: #263238;
            margin-bottom: 40px;
        }

        h2 {
            color: #34495E;
            border-bottom: 2px solid #2A9D8F;
            padding-bottom: 10px;
            margin-top: 40px;
        }

        .grafico {
            background-color: white;
            padding: 15px;
            margin-bottom: 25px;
            border-radius: 8px;
        }

        .container {
            max-width: 1200px;
            margin: auto;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>Dashboard Interativo - E-commerce</h1>

    <h2>Distribuição e Características dos Produtos</h2>
    <div class="grafico">GRAFICO_1</div>
    <div class="grafico">GRAFICO_2</div>
    <div class="grafico">GRAFICO_3</div>

    <h2>Análise de Preços e Vendas</h2>
    <div class="grafico">GRAFICO_4</div>
    <div class="grafico">GRAFICO_5</div>
    <div class="grafico">GRAFICO_6</div>

    <h2>Análise de Correlação</h2>
    <div class="grafico">GRAFICO_7</div>

</div>
</body>
</html>
"""

# Convertendo os gráficos para HTML
graficos = [fig1, fig2, fig3, fig4, fig5, fig6, fig7]

for i, fig in enumerate(graficos):
    html_grafico = pio.to_html(
        fig,
        full_html=False,
        include_plotlyjs='cdn' if i == 0 else False
    )

    html = html.replace(f'GRAFICO_{i + 1}', html_grafico)

# Salvando o arquivo HTML
with open('../dashboard_interativo.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(html)

print('Dashboard interativo gerado com sucesso!')

