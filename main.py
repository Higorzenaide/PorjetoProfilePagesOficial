import streamlit as st
import services.database as SupaBase

conectar_Com_Banco_de_Dados = SupaBase.SupabaseConnection()
Cliente = conectar_Com_Banco_de_Dados.conectar()



Session = Cliente.auth.get_session()
st.warning(Session)

# Valor do token
token = "2343242334634235425w252523"

# Domínio do seu site
dominio = "projectprofiledesktop.streamlit.app"

# URL de destino com o token como parâmetro de consulta
url_destino = f"https://{dominio}?token={token}"

# Crie o redirecionamento em HTML
redirecionamento_html = f'<meta http-equiv="refresh" content="5;url={url_destino}">'

# Use st.markdown para renderizar o HTML
st.markdown(redirecionamento_html, unsafe_allow_html=True)

# Exiba uma mensagem para o usuário
st.write("Você será redirecionado para a página em 5 segundos")

# Capturar os parâmetros de consulta da URL
query_params = st.experimental_get_query_params()

# Verificar se o token está presente nos parâmetros de consulta
if 'token' in query_params:
    token = query_params['token']
    st.write(f'Token capturado: {token}')
else:
    st.write('Token não encontrado na URL')









