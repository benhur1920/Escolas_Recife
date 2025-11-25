import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.marcadores import texto, sidebar

# Gráfico por região
def grafico_zona(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    df_agrupado = df.groupby('Região')[['Bairro']].count().reset_index()
    fig = px.treemap(df_agrupado, path=['Região'], values='Bairro', color='Bairro')

    fig.update_layout(
        title={
            'text': 'Unidades de ensino por região',
            'x': 0.5,
            'xanchor': 'right',
            'font': {'size': 18, 'color': texto}
        },
        font=dict(color=texto)
    )
    return fig

# Gráfico por bairro
def grafico_bairro(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL').sort_values('TOTAL', ascending=False)
    fig1 = px.bar(df_bairro, x='Bairro', y='TOTAL')

    fig1.update_layout(
        title={'text': 'Unidades de ensino por bairro', 'x': 0.5, 'xanchor': 'right', 'font': {'size': 18, 'color': texto}},
        xaxis_title='Bairro',
        yaxis_title='Total',
        xaxis_title_font=dict(size=18, color=texto),
        yaxis_title_font=dict(size=18, color=texto),
        xaxis_tickfont=dict(size=14, color=texto),
        yaxis_tickfont=dict(size=14, color=texto),
    )
    return fig1

# Gráfico por tipo de unidade
def grafico_tipo(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    df_bairro = df.groupby('Tipo').size().reset_index(name='TOTAL').sort_values('TOTAL', ascending=False)
    fig4 = px.pie(df_bairro, names='Tipo', values='TOTAL')

    fig4.update_traces(textposition='inside', textinfo='percent+label')
    fig4.update_layout(
        title={'text': 'Tipos de unidades de ensino', 'x': 0.5, 'xanchor': 'right', 'font': {'size': 18, 'color': texto}},
        legend=dict(font=dict(color=texto))
    )
    return fig4

# Gráfico com mapa
def grafico_mapa(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    fig3 = px.scatter_mapbox(
        df.dropna(subset=['Latitude', 'Longitude']),
        hover_name='Escola',
        hover_data={'Tipo': True, 'Região': True, 'Bairro': True, 'Rua': True, 'Numero': True},
        lat='Latitude',
        lon='Longitude',
        color='Tipo',
        zoom=11,
        height=700
    )
    fig3.update_traces(marker=dict(size=15))
    fig3.update_layout(
        mapbox_style="open-street-map",
        mapbox_center={"lat": -8.0476, "lon": -34.8770},
        legend=dict(
            title_text='Tipo de Escola',
            title_font=dict(size=18, color=texto),
            font=dict(size=12, color=texto),
            orientation='h',
            x=0.5,
            y=1.05,
            xanchor='right',
            yanchor='bottom',
            borderwidth=1
        ),
        margin=dict(t=150, b=20, l=10, r=10)
    )
    return fig3

# Gráfico por climatização
def grafico_climatizacao(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    df_climatizacao = df.groupby('Escola_climatizada').size().reset_index(name='TOTAL').sort_values('TOTAL', ascending=False)
    fig5 = px.bar(df_climatizacao, x='Escola_climatizada', y='TOTAL', labels={'Escola_climatizada': 'Escolas climatizadas'})

    fig5.update_layout(
        font=dict(color=texto),
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16)),
        yaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16))
    )
    return fig5

# Gráfico por sala de recursos
def grafico_sala(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    df_sala = df.groupby('Sala_recurso').size().reset_index(name='TOTAL').sort_values('TOTAL', ascending=False)
    fig6 = px.bar(df_sala, x='Sala_recurso', y='TOTAL', labels={'Sala_recurso': 'Escolas com Sala de recursos'})

    fig6.update_layout(
        font=dict(color=texto),
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16)),
        yaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16))
    )
    return fig6

# Gráfico por bibliotecas
def grafico_bibliotecas(df):
    if df.empty or 'Região' not in df.columns or 'Bairro' not in df.columns:
        st.warning("Não há dados disponíveis para gerar o gráfico de região.")
        return None

    df_bibliotecas = df.groupby('Biblioteca').size().reset_index(name='TOTAL').sort_values('TOTAL', ascending=False)
    fig7 = px.bar(df_bibliotecas, x='Biblioteca', y='TOTAL', labels={'Biblioteca': 'Escolas com bibliotecas'})

    fig7.update_layout(
        font=dict(color=texto),
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16)),
        yaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16))
    )
    return fig7

# Gráfico por bibliotecas
def grafico_quadra(df):
    

    df_bibliotecas = df.groupby('Quadra_coberta').size().reset_index(name='TOTAL').sort_values('TOTAL', ascending=False)
    fig7 = px.bar(df_bibliotecas, x='Quadra_coberta', y='TOTAL', labels={'Quadra_coberta': 'Quadra coberta'})

    fig7.update_layout(
        font=dict(color=texto),
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16)),
        yaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color=texto), title_font=dict(color=texto, size=16))
    )
    return fig7