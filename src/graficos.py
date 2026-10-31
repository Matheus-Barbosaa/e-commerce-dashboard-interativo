# Importando as bibliotecas
import plotly.express as px
import numpy as np
from scipy.stats import gaussian_kde


# Gráfico de Histograma(px.histogram) - Distribuição das Notas dos Produtos
def cria_grafico_histograma(df):

    fig1 = px.histogram(df, x='Nota', nbins=20)  # Define 20 intervalos para o histograma

    # Personalização da cor das barras
    fig1.update_traces(marker_color='#2A9D8F',  # Define a cor verde-petróleo
                       marker_line_color='white',  # Adiciona separação entre as barras
                       marker_line_width=0.5)  # Define a espessura das bordas

    # Personalização do layout
    fig1.update_layout(title='Distribuição das Notas dos Produtos',
        xaxis_title='Nota dos Produtos',
        yaxis_title='Quantidade de Produtos',
        template='plotly_white')  # Define o tema de fundo branco

    return fig1

# Gráfico de Dispersão(px.scatter) - Relação entre Preço e Quantidade Vendida
def cria_grafico_dispersao(df):

    fig2 = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod', color_discrete_sequence=['green'])

    # Personalização do layout
    fig2.update_layout(title='Relação entre Preço e Quantidade Vendida',
        xaxis_title='Preço do Produto (R$)',
        yaxis_title='Quantidade Vendida (codificada)')

    return fig2

# Mapa de Calor(px.imshow) da Correlação entre as Variáveis
def cria_grafico_correlacao(df):

    # Selecionando as variáveis e calculando a matriz de correlação
    df_corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço',
                  'Qtd_Vendidos_Cod', 'Marca_Freq', 'Material_Freq']].corr()

    # Criando o mapa de calor com escala de cores personalizada
    fig3 = px.imshow(df_corr, text_auto='.2f', aspect='auto',
        labels={'color': 'Correlação'},
        color_continuous_scale=[
            [0.0, '#D73027'],  # Vermelho: correlação muito fraca
            [0.2, '#FDAE61'],  # Laranja: correlação fraca
            [0.4, '#FEE090'],  # Amarelo-claro: correlação moderada
            [0.5, '#FFFFBF'],  # Amarelo: correlação próxima de zero
            [0.6, '#74ADD1'],  # Azul-claro: correlação positiva
            [0.8, '#4575B4'],  # Azul: correlação positiva forte
            [1.0, '#313695']   # Azul-escuro: correlação positiva muito forte
        ],
        zmin=-1, zmax=1)  # Mantém a escala de correlação entre -1 e +1

    # Personalização do layout
    fig3.update_layout(title='Mapa de Calor da Correlação entre as Variáveis')

    # Personalização da legenda de correlação
    fig3.update_coloraxes(colorbar=dict(
        title='Correlação',  # Título da legenda
        tickmode='array',  # Define posições personalizadas na escala
        tickvals=[-1, -0.5, 0, 0.5, 1],  # Valores de referência da correlação
        ticktext=['Negativa forte', 'Negativa moderada',
                  'Próxima de zero', 'Positiva moderada',
                  'Positiva forte']  # Descrições exibidas na legenda
    ))

    return fig3

# Gráfico de Barras(px.bar) - Quantidade de Produtos por Gênero
def cria_grafico_genero(df):

    df_genero = df['Gênero'].value_counts().reset_index()  # reset_index() cria as colunas Gênero e count, utilizadas no px.bar().

    fig4 = px.bar(df_genero, x='Gênero', y='count',  color='Gênero', color_discrete_sequence=px.colors.qualitative.Vivid)

    # Personalização do layout
    fig4.update_layout(title='Quantidade de Produtos por Gênero',
        xaxis_title='Gênero',
        yaxis_title='Quantidade de Produtos',
        showlegend = False) # retira a legenda lateral

    return fig4


# Gráfico de Pizza(px.pie) - Distribuição dos Produtos por Quantidade Vendida
def cria_grafico_pizza(df):

    fig5 = px.pie(df, names='Qtd_Vendidos', color_discrete_sequence=px.colors.sequential.RdBu)  # names: define as categorias que aparecem nas fatias.

    # Personalização do layout
    fig5.update_layout(title='Distribuição dos Produtos por Quantidade Vendida')

    return fig5

# Gráfico de Densidade - Distribuição dos Preços - px.area()	Área preenchida sob uma curva.
def cria_grafico_densidade(df):

    precos = df['Preço'].dropna()
    densidade = gaussian_kde(precos)  # gaussian_kde(): calcula a curva suavizada de densidade.
    x = np.linspace(precos.min(), precos.max(), 200)  # np.linspace(): cria 200 pontos entre o menor e o maior preço.

    fig6 = px.area(x=x, y=densidade(x), color_discrete_sequence=['#7B1FA2'])  # px.area(): desenha a curva e preenche sua área.

    # Personalização do layout
    fig6.update_layout(title='Densidade dos Preços dos Produtos',
        xaxis_title='Preço dos Produtos (R$)',
        yaxis_title='Densidade',
        xaxis_tickformat='.2f')

    return fig6

# Gráfico de Regressão - Relação entre Preço e Quantidade Vendida
def cria_grafico_regressao(df):

    # trendline: configura a linha de tendência.
    # 'ols': utiliza o método dos Mínimos Quadrados Ordinários para calcular a regressão linear.

    fig7 = px.scatter(df, x='Preço', y='Qtd_Vendidos_Cod',
        trendline='ols',
        color_discrete_sequence=['#34495E'],
        trendline_color_override='#F39C12')  # trendline_color_override='#E65100': define a cor da linha de regressão

    # Personalização do layout
    fig7.update_layout(title='Regressão entre Preço e Quantidade Vendida',
        xaxis_title='Preço do Produto (R$)',
        yaxis_title='Quantidade Vendida (codificada)',
        template='plotly_white',  # Define o tema de fundo branco
        plot_bgcolor='#F4F7FB',  # Cor de fundo da área do gráfico
        paper_bgcolor='#FFFFFF')  # Cor de fundo externo do gráfico

    return fig7