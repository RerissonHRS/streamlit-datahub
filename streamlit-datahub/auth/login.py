# auth/login.py
import streamlit_authenticator as stauth

def create_authenticator():
    names = ["Usuário Teste"]
    usernames = ["usuario"]
    hashed_passwords = [
        "$2b$12$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ]

    authenticator = stauth.Authenticate(
        names,
        usernames,
        hashed_passwords,
        "datahub_app",
        "abcdef",  # Um segredo qualquer
        cookie_expiry_days=1
    )
    return authenticator
