import streamlit as st
import pandas as pd
import plotly.express as px

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

#Sidebar
def display_sidebar(df):
    with st.sidebar:
        st.header("Informações do Aluno")
        st.write("Nome Completo: Alexandre Cabral do Espírito Santo")
        st.write("PDITA: PD030")

        selected_generation = st.selectbox("Selecione a Geração", df['Generation'].unique())
        selected_type = st.selectbox("Selecione o Tipo", df['Type 1'].unique())
        total_range = st.slider("Selecione a Faixa de Estatística total", int(df['Total'].min()), int(df['Total'].max()), (50, 780))

        theme = st.selectbox("Selecione o Tema", ["Light", "Dark"])

    return selected_generation, selected_type, total_range, theme

#filtrar com os requisitos selecionados
def filter_data(df, generation, p_type, total_range):
    filtered_df = df[(df['Generation'] == generation) & (df['Type 1'] == p_type) & (df['Total'] >= total_range[0]) & (df['Total'] <= total_range[1])]
    return filtered_df

#Gráfico
def create_chart(df, theme):
    fig = px.scatter_3d(
        df,
        x='Type 1',
        y='Type 2',
        z='Total',
        animation_frame='Generation',
        color='Total',
        color_continuous_scale='Viridis',
        title="Mistura de tipos com maior total de estatísticas",
        hover_data={'Name': True}
    )
    fig.update_layout(
        paper_bgcolor='#11141B' if theme == 'Dark' else '#F1F1F1',
        font=dict(color='white' if theme == 'Dark' else 'black'),
        title_font=dict(color='white' if theme == 'Dark' else 'black'),
        font_color='white' if theme == 'Dark' else 'black'
    )
    st.plotly_chart(fig)


def main():
    # Carregar dados
    df = load_data()
    
    # Exibir título
    st.title("Pokemon Dashboard")
    
    # Exibir barra lateral
    selected_generation, selected_type, total_range, theme = display_sidebar(df)

    #Aplicar tema
    if theme == "Dark":
        with open('styles/dark.css', 'r') as fp:
            st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)
    else:
        with open('styles/light.css', 'r') as fp:
            st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

    # Filtrar dados
    filtered_df = filter_data(df, selected_generation, selected_type, total_range)
    
    # Criar gráfico
    create_chart(filtered_df, theme)

if __name__ == "__main__":
    main()