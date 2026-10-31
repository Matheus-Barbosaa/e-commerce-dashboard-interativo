# Importando as bibliotecas
import pandas as pd
from dash import Dash, dcc, html

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
df = pd.read_csv('data/raw/ecommerce_estatistica.csv')

def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([

        html.H1('Dashboard Interativo - E-commerce'),

        html.Br(),

        # Distribuição e características dos produtos
        html.H2('Distribuição e Características dos Produtos'),

        dcc.Graph(id='grafico-notas', figure=cria_grafico_histograma(df)),
        dcc.Graph(id='grafico-genero', figure=cria_grafico_genero(df)),
        dcc.Graph(id='grafico-pizza', figure=cria_grafico_pizza(df)),

        html.Br(),

        # Análise de preços e vendas
        html.H2('Análise de Preços e Vendas'),

        dcc.Graph(id='grafico-dispersao', figure=cria_grafico_dispersao(df)),
        dcc.Graph(id='grafico-densidade', figure=cria_grafico_densidade(df)),
        dcc.Graph(id='grafico-regressao', figure=cria_grafico_regressao(df)),

        html.Br(),

        # Análise das relações entre as variáveis
        html.H2('Análise de Correlação'),

        dcc.Graph(id='grafico-correlacao', figure=cria_grafico_correlacao(df))

    ])
    return app

# Executa App
if __name__ == '__main__':
    app = cria_app()
    app.run(debug=True, port=8050)
