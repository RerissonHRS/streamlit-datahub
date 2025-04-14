# pages/API_External.py
import streamlit as st
import requests

st.title("🌦️ Consulta de Clima - API OpenWeather")

cidade = st.text_input("Digite a cidade:")

if cidade:
    chave_api = "SUA_CHAVE_API_AQUI"  # Substitua pela sua chave real da OpenWeather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
    resp = requests.get(url).json()

    if resp.get("cod") != "404":
        st.metric("Temperatura", f"{resp['main']['temp']} °C")
        st.write("Condições:", resp["weather"][0]["description"].capitalize())
    else:
        st.error("Cidade não encontrada.")
