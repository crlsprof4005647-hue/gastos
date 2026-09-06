import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🚀 Meu App Conectado ao Google Sheets!")

# A conexão agora não precisa de código complexo, ela puxa do cofre sozinha!
conn = st.connection("gsheets", type=GSheetsConnection)

# COLE O LINK DA SUA PLANILHA AQUI DENTRO DAS ASPAS
URL_PLANILHA = "COLE_AQUI_O_LINK_DA_SUA_PLANILHA"

# Lê os dados da planilha e mostra na tela (lembre-se de mudar 'Dados' se o nome da sua aba for outro)
try:
    df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Dados")
    st.success("Conexão feita com sucesso! Abaixo estão seus dados:")
    st.dataframe(df)
except Exception as e:
    st.error(f"Erro ao ler a planilha: {e}")
