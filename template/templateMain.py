import streamlit as st
import datetime

data_atual = datetime.date.today()

st.title("Adicionar Novo Dado")
st.sidebar.title("Menu")
st.sidebar.selectbox('Profile Desktop', ['Incluir','Editar Dados','Visualizar'])

def templateAdicionarNovoDado():

    with st.form(key="include_profile"):
        selected_date = st.date_input("Data atual", min_value=None, max_value=None, key=None, disabled=True)
        selected_email = st.text_input(label="Insira seu E-mail")
        
        # Defina o valor padrão do número como None para deixá-lo vazio inicialmente
        selected_smart_protocol = st.number_input(label="Insira o protocolo do smart", format="%d", step=1, value=None)
        selected_sis_protocol = st.number_input(label="Insira o protocolo do sis", format="%d", step=1, value=None)
        
        # Corrigido: Adicione um rótulo ao selectbox
        selected_plan = st.selectbox("Selecione um plano", options=["100mb", "200mb"])
        
        # Defina o valor padrão do número como None para deixá-lo vazio inicialmente
        selected_profile = st.number_input(label="Insira a quantidade que está chegando", format="%d", step=100, value=None)
        
        # Corrigido: Adicione um rótulo ao selectbox
        selected_regional = st.selectbox("Selecione uma regional", options=["CENTRAL", "SUL", "VALE", "CAMPINAS"])
        
        # Adicione um botão de envio dentro do bloco do formulário
        submit = st.form_submit_button("Enviar")