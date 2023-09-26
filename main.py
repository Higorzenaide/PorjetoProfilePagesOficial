import streamlit as st
import services.database as SupaBase
import time
import template.templateMain as incluir
token2 = ''


conectar_Com_Banco_de_Dados = SupaBase.SupabaseConnection()
Cliente = conectar_Com_Banco_de_Dados.conectar()
query_params = st.experimental_get_query_params()

# Session = Cliente.auth.get_session()
# st.warning(Session.access_token)


if 'token' in query_params:
    try:
        token = query_params['token']
        tokenValido = token[0]
        get_user = Cliente.auth.get_user(tokenValido)

        # Caso queira saber os dados do usuário
        # st.warning(get_user.user.email)
        # st.warning(get_user.user.id)

        # Id_cliente = get_user.user.id
        # incluir.IdDoCliente(Id_cliente)
        # user_id = Cliente.auth.get_user()
        # st.warning(user_id)

        st.write("<h1 style='color: red;'>PROFILE DESKTOP</h1>", unsafe_allow_html=True)
        st.sidebar.title("Profile Desktop Menu")
        opcoes_menu = ['Selecione','Incluir','Editar Dados','Visualizar']  # Opções iniciais do menu
        page_cliente = st.sidebar.selectbox("Escolha uma opção", opcoes_menu)
        if page_cliente == 'Incluir':
            incluir.templateAdicionarNovoDado()
        else:
            pass
    except Exception as e:
        if "invalid JWT: unable to parse or verify signature, token contains an invalid number of segments" in str(e):
            st.error("O token passsado para sessão é inválido ou foi expirado, faça login novamente para acessar o site!")
        elif "invalid JWT: unable to parse or verify signature, token is expired by" in str(e):
            st.error("Sua sessão expirou, faça login novamente para acessar o site")
        else:
            st.error(e)
else:
    st.error("É necessário fazer login na aplicação para acessar o site")











