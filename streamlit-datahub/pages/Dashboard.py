# pages/Dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard Interativo")

df = pd.read_csv("data/dataset.csv")

st.dataframe(df)

fig = px.bar(df, x="Cidade", y="Populacao_Estimada", title="População por Cidade")
st.plotly_chart(fig, use_container_width=True)
