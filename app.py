import streamlit as st

# 1. CONFIGURAÇÃO BÁSICA
st.set_page_config(page_title="Meu Novo App", layout="wide")

# 2. O VISUAL (LAYOUT E CORES)
# Aqui você define o fundo, a cor do texto e dos botões
st.markdown("""
    <style>
    .stApp { background-color: #F0F2F6; } /* Cor do fundo */
    h1 { color: #2C3E50; } /* Cor do título principal */
    .stButton > button { 
        background-color: #3498DB !important; 
        color: white !important; 
        border-radius: 8px; 
    }
    </style>
""", unsafe_allow_html=True)

# 3. O CONTEÚDO DA TELA
st.title("🚀 Bem-vindo ao Meu Novo Aplicativo")
st.write("Este é o começo de um grande projeto.")

# Exemplo de um campo de digitação e um botão
nome = st.text_input("Qual é o seu nome?")
if st.button("Enviar"):
    st.success(f"Olá, {nome}! Seu aplicativo está funcionando perfeitamente.")
