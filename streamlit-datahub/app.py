# app.py
import streamlit as st
from auth.login import create_authenticator

st.set_page_config(page_title="DataHub", layout="wide")
authenticator = create_authenticator()

name, auth_status, username = authenticator.login("Login", "main")

if auth_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"Bem-vindo(a), {name} 👋")
    st.sidebar.page_link("pages/Dashboard.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/API_External.py", label="🌐 API Externa")
    st.sidebar.page_link("pages/ML_Model.py", label="🧠 Previsão com ML")

    st.title("📈 DataHub - Plataforma de Dados")
    st.info("Escolha uma funcionalidade no menu lateral.")
elif auth_status is False:
    st.error("Usuário ou senha incorretos.")
elif auth_status is None:
    st.warning("Digite suas credenciais.")
