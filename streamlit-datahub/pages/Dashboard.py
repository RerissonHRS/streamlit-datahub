# pages/Dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Dashboard Interativo")

file_path = "data/dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    st.warning("Arquivo de dados não encontrado. Usando dados de exemplo.")
    df = pd.DataFrame({
        "Cidade": ["Curitiba", "Londrina", "Maringá"],
        "Populacao_Estimada": [1963726, 588125, 439321]
    })

st.dataframe(df)

fig = px.bar(df, x="Cidade", y="Populacao_Estimada", title="População por Cidade")
st.plotly_chart(fig, use_container_width=True)
