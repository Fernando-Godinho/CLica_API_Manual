import streamlit as st
from datetime import datetime, timedelta

# Função para dividir o mês em grupos de 5 dias
def dividir_mes_em_grupos(mes, ano):
    data_inicial = datetime(ano, mes, 1)
    grupos = []
    while data_inicial.month == mes:
        data_final = data_inicial + timedelta(days=4)
        if data_final.month != mes:
            data_final = datetime(ano, mes + 1, 1) - timedelta(days=1)
        if data_final.day == 31 and data_inicial.day != 31:
            data_final = data_inicial + timedelta(days=3)
        grupos.append((data_inicial, data_final))
        data_inicial = data_final + timedelta(days=1)
    return grupos

# Função para gerar o link com as datas
def gerar_link(data_inicial, data_final):
    base_url = "https://www.sccloud.com.br/smartgps/index.php/Integracao/integra/id/28/data_inicial/"
    link = f"{base_url}{data_inicial.strftime('%Y-%m-%d')}/data_final/{data_final.strftime('%Y-%m-%d')}/setores/"
    return link

# Interface do usuário
st.title('Dividir Mês em Grupos de 5 Dias e Gerar Links')
mes = st.selectbox('Escolha o mês', range(1, 13))
ano = st.number_input('Escolha o ano', min_value=1900, max_value=2100, value=datetime.now().year)

# Botão para gerar os grupos
if st.button('Dividir Mês'):
    grupos = dividir_mes_em_grupos(mes, ano)
    st.write(f'Grupos de 5 dias para {mes}/{ano}:')
    for inicio, fim in grupos:
        link = gerar_link(inicio, fim)
        st.write(f'{inicio.strftime("%d/%m/%Y")} - {fim.strftime("%d/%m/%Y")}: [Link]({link})')
