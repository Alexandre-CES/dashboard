import streamlit as st
import pandas as pd
import plotly.express as px

import csv

#Config page
st.set_page_config(
    page_title="Pokemon Dashboard",
    layout="wide",
    page_icon="Φ",
    initial_sidebar_state="expanded"
)

#CSS
with open('styles/style.css', 'r') as fp:
    st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

#Load csv data
@st.cache_data
def load_data():
    df = pd.read_csv('./data/Pokemon.csv')
    return df

df = load_data()

#Title
st.title("Pokemon Dashboard")

#Sidebar
with st.sidebar:
    st.header("Informações do Aluno")
    st.write("Nome Completo: Alexandre Cabral do Espírito Santo")
    st.write("PDITA: PD030")

    selected_generation = st.selectbox("Selecione a Geração", df['Generation'].unique())
    selected_type = st.selectbox("Selecione o Tipo", df['Type 1'].unique())
    total_range = st.slider("Selecione a Faixa de Estatística total", int(df['Total'].min()), int(df['Total'].max()), (50, 100))

filtered_df = df[(df['Generation'] == selected_generation) & (df['Type 1'] == selected_type) & (df['Total'] >= total_range[0]) & (df['Total'] <= total_range[1])]

# Exemplo de gráfico
fig = px.scatter_3d(filtered_df, x='Type 1', y='Type 2', z='Total', animation_frame='Generation', color='Total', title="Mistura de tipos com maior ataque")
st.plotly_chart(fig)