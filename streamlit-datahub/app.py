# app.py
import streamlit as st

st.set_page_config(page_title="DataHub", layout="wide")

st.sidebar.title("📚 Navegação")
st.sidebar.page_link("pages/Dashboard.py", label="📊 Dashboard")
st.sidebar.page_link("pages/API_External.py", label="🌐 API Externa")
st.sidebar.page_link("pages/ML_Model.py", label="🧠 Previsão ML")

st.title("📈 DataHub - Plataforma Interativa")
st.info("Escolha uma funcionalidade no menu lateral.")
