import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####

st.title("Buscar CEP")

st.image("principal.png")

##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####

st.sidebar.image("logo.png")
st.write("Aplicação para buscar endereço a partir do CEP e mostrar Localizaçao no mapa")
opcao = st.sidebar.selectbox("Você quer?",opcoes)

##### BOTÃO BUSCAR CEP #####

if opcao == "Buscar CEP":
    st.header("Buscar Endereço pelo CEP")
    cep = st.text_input("digite o CEP(somente numeros):")



    if st.button("Buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("Por favor, insira um Cep valido com 8 digitos numericos")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("Endereço encontrado:")
                    st.write(f"Cep:{endereco[0]}")
                    st.write(f"Endereço:{endereco[1]}")
                    st.write(f"Bairro:{endereco[2]}")
                    st.write(f"Cidade:{endereco[3]}")
                    st.write(f"Estado:{endereco[4]}")

                ###  mapas

                    st.title("Localização no Mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                    st.map(df, zoom=15)

                else:
                    st.error("CEP não encontrado")
            except Exception as e:
                st.error(f"Ocorreu um erro buscar ao buscar o CEP:{e} ")




##### BOTÃO DESCOBRIR CEP #####

elif opcao == "Descobrir CEP":
    st.header("Descobrir Cep pelo Endereço")
    endereco_usuario = st.text_input("digite o endereço(ex:Rua Olga, Barueri, SP)")
    
    if st.button("Descobrir"):
        if not endereco_usuario.strip():
            st.error("Por favor, insira um endereço valido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro ao descobrir o CEP: {e}") 