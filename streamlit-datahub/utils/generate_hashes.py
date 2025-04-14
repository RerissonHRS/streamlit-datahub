# utils/generate_hashes.py
import streamlit_authenticator as stauth

# Defina os usuários e as senhas
usernames = ["usuario"]  # Nome de usuário
senhas = ["123"]  # Senha em texto plano

# Gere o hash da senha
hashed_passwords = stauth.Hasher(senhas).generate()

# Exiba o hash gerado
print(hashed_passwords)
