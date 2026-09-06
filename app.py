import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🚀 Meu App Conectado ao Google Sheets!")

# Cria a conexão puxando as senhas do cofre
conn = st.connection("gsheets", type=GSheetsConnection)

# COLE O LINK DA SUA PLANILHA AQUI DENTRO DAS ASPAS
URL_PLANILHA = "COLE_AQUI_O_LINK_DA_SUA_PLANILHA"

# Lê a planilha forçando a atualização na mesma hora (ttl=0)
df = conn.read(spreadsheet=URL_PLANILHA, ttl=0)

st.success("Conexão feita com sucesso! Abaixo estão seus dados:")
st.dataframe(df)
