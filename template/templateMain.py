import streamlit as st
import datetime
import services.database


CLIENTE = services.database.SupabaseConnection()
CLIENTE.conectar()

data_atual = datetime.date.today()
# Converter a data em uma string no formato ISO 8601


def IdDoCliente(id_cliente):
    id = id_cliente
    return

# Session = CLIENTE.supabase.auth.get_session()
# id = Session.user.id


def selecione(valor):
    if "Selecione" in valor:
        return False
    else:
        return True
    

def opcaoTecnico():
    with st.form(key="tecnicoOpcao"):
        selected_option_tecnico = st.selectbox("Técnico alega que está chegando a menos por limitação do seu celular:", ["Selecione" , "Sim", "Não"])
        confirmar = st.form_submit_button("Confirmar")
        return selected_option_tecnico

def contCarac(protocolo):
        quantidade_carac = str(protocolo)
        quantidade_carac = len(quantidade_carac)
        if quantidade_carac < 6:
            return False
        else:
            return True



def IncluirNoBanco():
    pass

def templateAdicionarNovoDado():
    

    st.subheader("inclua os dados do atendimento")
    with st.form(key="include_profile"):
        selected_date = st.date_input("Data atual", min_value=None, max_value=None, key=None, disabled=True)
        selected_smart_protocol = st.number_input(label="Insira o protocolo do smart", format="%d", step=1, value=None)
        selected_sis_protocol = st.number_input(label="Insira o protocolo do sis", format="%d", step=1, value=None)
        selected_plan = st.selectbox("Selecione a quatidade de Mb contratos", options=[0,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000])
        selected_profile = st.number_input(label="Insira a quantidade que está chegando", format="%d", step=100, value=0)
        selected_regional = st.selectbox("Selecione uma regional", options=["Selecione" ,"CENTRAL", "SUL", "VALE", "CAMPINAS"])
        input_button_submit = st.form_submit_button("Enviar")

        if input_button_submit:
            if not contCarac(selected_smart_protocol):
                st.error("Insira um protocolo do smart válido")
                return
            elif not contCarac(selected_sis_protocol):
                st.error("Insira um protocolo do sis, válido")
            elif selected_plan == 0:
                st.error("A quantidade de megas contratados devem ser de no minímo 100mb")
            elif selected_profile == 0:
                st.error("Inisira a quantidade de MB que está chegando")
                return
            elif not selecione(selected_regional):
                st.error("Selecione uma regional")
                return
            else:
                try:
                    selected_date_iso = selected_date.strftime('%Y-%m-%dT%H:%M:%S')
                    data,count = CLIENTE.supabase.table("dados_profile").insert(
                        {"protocolo_sis": selected_sis_protocol,"date":selected_date_iso,
                    "protocolo_smart":selected_smart_protocol,"velocidade_contratada":selected_plan,"velocidade_entregue":selected_profile,"regional":selected_regional}
                    ).execute()
                except Exception as e:
                    st.error(f'ocorreu um erro ao inserir no banco de dados {str(e)}')

