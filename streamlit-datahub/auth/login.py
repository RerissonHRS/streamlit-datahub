# auth/login.py
import streamlit_authenticator as stauth

def create_authenticator():
    names = ["Usuário Teste"]
    usernames = ["usuario"]
    passwords = ["123"]

    hashed_passwords = stauth.Hasher(passwords).generate()

    authenticator = stauth.Authenticate(
        names,
        usernames,
        hashed_passwords,
        "datahub_app",
        "abcdef",
        cookie_expiry_days=1
    )
    return authenticator
