import streamlit as st

st.set_page_config(page_title="DataHub", layout="wide")

st.sidebar.title("📚 Navegação")
st.sidebar.markdown("[📊 Dashboard](pages/Dashboard.py)")

st.title("📈 DataHub - Plataforma Interativa")
st.info("Escolha uma funcionalidade no menu lateral.")
