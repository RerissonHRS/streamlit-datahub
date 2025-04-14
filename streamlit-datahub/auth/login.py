# auth/login.py
import streamlit_authenticator as stauth

def create_authenticator():
    names = ["Usuário Teste"]
    usernames = ["usuario"]
    
    # Use o hash gerado para a senha "123"
    hashed_passwords = [
        "$2b$12$xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Substitua pelo hash gerado
    ]

    authenticator = stauth.Authenticate(
        names,
        usernames,
        hashed_passwords,
        "datahub_app",
        "abcdef",
        cookie_expiry_days=1
    )
    return authenticator

