import streamlit as st
import pandas as pd
import requests

st.title("📊 Municípios do Paraná - Dados Reais do IBGE")

url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/41/municipios"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    # Criar DataFrame com os nomes dos municípios
    df = pd.DataFrame([{
        "Código IBGE": municipio["id"],
        "Município": municipio["nome"],
        "Microrregião": municipio["microrregiao"]["nome"],
        "Mesorregião": municipio["microrregiao"]["mesorregiao"]["nome"]
    } for municipio in dados])

    st.success(f"{len(df)} municípios carregados com sucesso.")
    st.dataframe(df)

    # Exemplo de gráfico: municípios por mesorregião
    grafico = df["Mesorregião"].value_counts().reset_index()
    grafico.columns = ["Mesorregião", "Quantidade"]

    st.bar_chart(grafico.set_index("Mesorregião"))

except Exception as e:
    st.error(f"Erro ao acessar dados: {e}")
