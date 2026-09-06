import streamlit as st
import json
from streamlit_gsheets import GSheetsConnection

st.title("🚀 Meu App Conectado ao Google Sheets!")

# 1. Ele pega o texto lá do cofre (Secrets) e transforma em dados
credenciais = json.loads(st.secrets["google_json"])

# 2. Inicia a conexão segura usando o robô
conn = st.connection("gsheets", type=GSheetsConnection, service_account_info=credenciais)

# COLE O LINK DA SUA PLANILHA AQUI DENTRO DAS ASPAS:
URL_PLANILHA = "COLE_AQUI_O_LINK_DA_SUA_PLANILHA"

# 3. Lê os dados da planilha e mostra na tela
df = conn.read(spreadsheet=URL_PLANILHA, worksheet="Página1")

st.write("Abaixo estão os dados da sua planilha:")
st.dataframe(df)
