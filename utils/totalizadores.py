from dados.escolas import df
print(df.shape)
print(df.head())
print(df.columns)
import pandas as pd
import streamlit as st
import re
from datetime import date


# Data atual
hoje = date.today()


# Cópia do DataFrame original
df_filtrado = df.copy()

#Calculo da ultima e menor data do sistema
#ultima_data =  df['data'].max()
#primeira_data =  df['data'].min()


# Calculo dos totalizadores
def calculo_total_unidades(df):
    totalUnidades = df.shape[0]
    return totalUnidades

def calculo_total_professores(df):
    totalProfessores = df['Qtd_professores'].sum()
    return f"{totalProfessores:,.0f}".replace(",", ".")

def calculo_total_alunos(df):
    totalAlunos = df['Qtd_alunos'].sum()
    return f"{totalAlunos:,.0f}".replace(",", ".")

def calculo_total_turmas(df):
    totalTurmas = df['Qtd_turmas'].sum()
    return f"{totalTurmas:,.0f}".replace(",", ".")

def calculo_total_escola_municipal(df):
    totalEscolas = (df['Tipo'] == "ESCOLA MUNICIPAL").sum()
    return totalEscolas

def calculo_total_creche_municipal(df):
    totalCreches = (df['Tipo'] == "CRECHE MUNICIPAL").sum()
    return totalCreches

def calculo_total_creche_escola_municipal(df):
    totalCrechesEscolas = (df['Tipo'] == "CRECHE ESC.RECIFE").sum()
    return totalCrechesEscolas

def calculo_total_Cmei(df):
    totalCmei = (df['Tipo'] == "CMEI").sum()
    return totalCmei

def calular_a_quantidade_de_colunas(df):
    colunasDisponiveis = sorted(df.columns)
    return len(colunasDisponiveis)  



