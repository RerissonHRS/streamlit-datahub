import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Exemplo de dados fictícios de crescimento de produtos e taxa de escolaridade
dados_produtos_escolaridade = {
    "Categoria_Produto": ["Alimentos", "Eletrônicos", "Vestuário", "Móveis", "Beleza", "Saúde"],
    "Crescimento (%)": [12.5, 8.2, 14.0, 7.5, 20.5, 10.0],  # Taxa de Crescimento de Vendas
    "Taxa_Escolaridade (%)": [65, 75, 80, 60, 85, 70]  # Taxa de Escolaridade da População (em %)
}

# Criando DataFrame com os dados fictícios
df_produtos_escolaridade = pd.DataFrame(dados_produtos_escolaridade)

# Exibindo os dados na interface do Streamlit
st.title("📊 Análise de Crescimento de Produtos por Taxa de Escolaridade")

st.write("### Dados de Crescimento de Produtos e Taxa de Escolaridade", df_produtos_escolaridade)

# Divisão de dados para o modelo de Machine Learning
X = df_produtos_escolaridade[["Taxa_Escolaridade (%)"]]  # Variável independente (Taxa de Escolaridade)
y = df_produtos_escolaridade["Crescimento (%)"]  # Variável dependente (Crescimento de Vendas)

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criação e treinamento do modelo de Regressão Linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazendo previsões
y_pred = modelo.predict(X_test)

# Calculando a performance do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Exibindo o resultado do modelo
st.write(f"### Desempenho do Modelo")
st.write(f"**Erro Quadrático Médio (MSE):** {mse:.2f}")
st.write(f"**Coeficiente de Determinação (R²):** {r2:.2f}")

# Exibindo o gráfico da regressão
fig, ax = plt.subplots()
ax.scatter(X_test, y_test, color='blue', label='Dados reais')
ax.plot(X_test, y_pred, color='red', label='Previsão (Modelo Linear)')
ax.set_xlabel("Taxa de Escolaridade (%)")
ax.set_ylabel("Crescimento de Vendas (%)")
ax.set_title("Regressão Linear: Crescimento de Vendas vs. Taxa de Escolaridade")
ax.legend()
st.pyplot(fig)

# Exibindo o modelo treinado
st.write("### Coeficientes do Modelo de Regressão Linear")
st.write(f"Coeficiente (Inclinação): {modelo.coef_[0]:.2f}")
st.write(f"Intercepto: {modelo.intercept_:.2f}")
