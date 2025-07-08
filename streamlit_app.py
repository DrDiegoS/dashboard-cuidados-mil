import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(layout="wide", page_title="Dashboard Cuidados Mil")

# Conectar ao Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(credentials)

# URL da planilha
spreadsheet_url = st.secrets["spreadsheet_url"]
spreadsheet = client.open_by_url(spreadsheet_url)

# Carregar dados da aba "Linhas"
sheet = spreadsheet.worksheet("Linhas")
df = pd.DataFrame(sheet.get_all_records())

# Interface
st.title("📊 Dashboard de Acompanhamento")
st.dataframe(df, use_container_width=True)