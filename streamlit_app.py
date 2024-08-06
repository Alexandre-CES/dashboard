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
        
        type_options = ['Todos'] + df['Type 1'].unique().tolist()
        selected_type = st.selectbox("Selecione o Tipo", type_options)
        
        stat_options = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
        selected_stat = st.selectbox("Selecione a Estatística", stat_options)
        
        total_range = st.slider(f"Selecione a Faixa de {selected_stat}", int(df[selected_stat].min()), int(df[selected_stat].max()), (50, int(df[selected_stat].max())))

        theme = st.selectbox("Selecione o Tema", ["Light", "Dark"])

    return selected_generation, selected_type, selected_stat, total_range, theme

#filtrar com os requisitos selecionados
def filter_data(df, generation, p_type, stat, total_range):
    filtered_df = df[df['Generation'] == generation]
    if p_type != 'Todos':
        filtered_df = filtered_df[filtered_df['Type 1'] == p_type]
    filtered_df = filtered_df[(df[stat] >= total_range[0]) & (df[stat] <= total_range[1])]
    return filtered_df

#Gráfico
def create_chart(df, stat, theme):
    fig = px.scatter_3d(
        df,
        x='Type 1',
        y='Type 2',
        z=stat,
        animation_frame='Generation',
        color=stat,
        color_continuous_scale='Viridis',
        title=f"Mistura de tipos com maior {stat}",
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
    selected_generation, selected_type, selected_stat, total_range, theme = display_sidebar(df)

    #Aplicar tema
    if theme == "Dark":
        with open('styles/dark.css', 'r') as fp:
            st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)
    else:
        with open('styles/light.css', 'r') as fp:
            st.markdown(f"<style>{fp.read()}</style>", unsafe_allow_html=True)

    # Filtrar dados
    filtered_df = filter_data(df, selected_generation, selected_type, selected_stat, total_range)
    
    # Criar gráfico
    create_chart(filtered_df, selected_stat, theme)

if __name__ == "__main__":
    main()
