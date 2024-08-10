# Pokemon Dashboard

## Descrição Geral
O **Pokemon Dashboard** é um projeto desenvolvido para visualização e análise de dados dos Pokémon. Utilizando a biblioteca Streamlit para a construção do dashboard interativo e Plotly para a criação de gráficos, este projeto permite explorar as estatísticas dos Pokémon de forma dinâmica e visual. O objetivo principal é proporcionar uma ferramenta intuitiva para fãs e pesquisadores que desejam analisar as estatísticas dos Pokémon.

## Demonstração de Uso
Captura de tela do dashboard em funcionamento:

-imagem-

### Funcionalidades:
- **Seleção de Geração:** Permite escolher a geração de Pokémon que deseja visualizar.
- **Seleção de Tipo:** Filtra os Pokémon pelo seu tipo primário.
- **Seleção de Estatística:** Permite escolher qual estatística analisar (Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed).
- **Faixa de Estatística:** Filtra Pokémon dentro de uma faixa de valores da estatística selecionada.
- **Tema:** Alterna entre os temas Light e Dark.
- **Comparação de Pokémon:** Exibe os dois Pokémon com os maiores valores da estatística selecionada, mostrando a diferença entre eles.

## Tecnologias Utilizadas
- **Linguagens de Programação:**
  - Python
- **Bibliotecas:**
  - Streamlit
  - Pandas
  - Plotly
- **CSS:**
  - Customizado para temas Light e Dark

## Informações sobre os Dados Originais
O dataset utilizado neste projeto é uma lista de Pokémon com as seguintes colunas:

- **Name:** Nome do Pokémon
- **Type 1:** Tipo primário do Pokémon
- **Type 2:** Tipo secundário do Pokémon (se houver)
- **Total:** Soma total das estatísticas base do Pokémon
- **HP:** Pontos de vida do Pokémon
- **Attack:** Estatística de ataque do Pokémon
- **Defense:** Estatística de defesa do Pokémon
- **Sp. Atk:** Estatística de ataque especial do Pokémon
- **Sp. Def:** Estatística de defesa especial do Pokémon
- **Speed:** Velocidade do Pokémon
- **Generation:** Geração à qual o Pokémon pertence
- **Legendary:** Indica se o Pokémon é lendário ou não

## Instruções para Executar o Projeto
Para executar este projeto localmente, siga os seguintes passos:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Alexandre-CES/dashboard.git
   cd pokemon-dashboard

2. Ative o ambiente virtual:
    <br><br>
    Linux/MacOS:
    <pre><code>source venv/bin/activate</code></pre>
    Windows:
    <pre><code>venv\Scripts\activate</code></pre>
    
3. Execute o aplicativo:
    ```bash
    streamlit run streamlit_app.py
