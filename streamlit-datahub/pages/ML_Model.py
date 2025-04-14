# pages/ML_Model.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🧠 Previsão de Valores (ML)")

# Dados fictícios
df = pd.DataFrame({
    "Ano": [2019, 2020, 2021, 2022, 2023],
    "Vendas": [100, 120, 130, 150, 170]
})

model = LinearRegression()
model.fit(df[["Ano"]], df["Vendas"])

ano = st.slider("Selecione o ano:", 2024, 2030)
previsao = model.predict(np.array([[ano]]))[0]

st.metric(f"Previsão para {ano}", f"{int(previsao)} vendas")
