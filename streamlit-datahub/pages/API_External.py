import streamlit as st
import pandas as pd

# Lista de cidades para o selectbox (você pode adicionar mais cidades ou buscar de uma API externa)
cidades_disponiveis = [
    "Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Florianópolis"
]

st.title("📊 Dashboard Interativo")

# Seletor de cidade
cidade = st.selectbox("Selecione uma cidade:", cidades_disponiveis)

# Exemplo de dados fictícios de Faturamento e Quantidade de Municípios IBGE
dados_faturamento_ibge = {
    "Cidade": ["Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Florianópolis"],
    "Faturamento": [100000, 200000, 150000, 120000, 180000, 110000],
    "IBGE_Quantidade": [1.9, 12.2, 6.7, 3.0, 5.2, 2.4]  # Dados fictícios de quantidade de municípios (milhões)
}

# Criando DataFrame com os dados fictícios
df_faturamento_ibge = pd.DataFrame(dados_faturamento_ibge)

# Exibindo o gráfico de faturamento por cidade
st.subheader("💡 Faturamento por Cidade")
st.bar_chart(df_faturamento_ibge.set_index("Cidade")["Faturamento"])

# Exibindo o gráfico de IBGE por cidade
st.subheader("💡 Quantidade de Municípios IBGE por Cidade")
st.bar_chart(df_faturamento_ibge.set_index("Cidade")["IBGE_Quantidade"])

# Exibindo tabela com os dados
st.write("📊 Dados de Faturamento e IBGE:", df_faturamento_ibge)
