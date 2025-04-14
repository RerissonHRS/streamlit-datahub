import streamlit as st
import pandas as pd
import requests

st.title("📊 Dashboard - Comparativo PIB x Municípios do Paraná")

# -------------------------------
# 🔹 1. Dados do IBGE - Municípios do Paraná
# -------------------------------
url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/41/municipios"
resposta = requests.get(url_ibge)
dados = resposta.json()

df_ibge = pd.DataFrame([{
    "Município": item["nome"],
    "Mesorregião": item["microrregiao"]["mesorregiao"]["nome"]
} for item in dados])

# -------------------------------
# 🔹 2. Dados reais de PIB por município (arquivo CSV)
# -------------------------------
try:
    df_pib = pd.read_csv("data/pib_municipios_pr.csv")  # Substitua pelo nome real do arquivo
    df_pib["Município"] = df_pib["Município"].str.strip()  # Ajustar nomes
    df_pib["Município"] = df_pib["Município"].str.title()

    # -------------------------------
    # 🔹 3. Merge dos dados
    # -------------------------------
    df_merge = pd.merge(df_ibge, df_pib, on="Município", how="inner")

    st.success(f"🔎 {len(df_merge)} municípios encontrados com dados de PIB")

    st.dataframe(df_merge)

    # -------------------------------
    # 🔹 4. Gráficos comparativos
    # -------------------------------

    st.subheader("📈 PIB Total por Mesorregião")
    pib_meso = df_merge.groupby("Mesorregião")["PIB (R$ milhões)"].sum().sort_values(ascending=False)
    st.bar_chart(pib_meso)

    st.subheader("🏙️ Quantidade de Municípios por Mesorregião")
    qtd_meso = df_ibge["Mesorregião"].value_counts()
    st.bar_chart(qtd_meso)

    st.subheader("📉 PIB Médio por Município (por Mesorregião)")
    media_meso = df_merge.groupby("Mesorregião")["PIB (R$ milhões)"].mean().sort_values(ascending=False)
    st.bar_chart(media_meso)

except FileNotFoundError:
    st.error("⚠️ Arquivo com dados de PIB não encontrado. Certifique-se de que 'data/pib_municipios_pr.csv' existe.")
