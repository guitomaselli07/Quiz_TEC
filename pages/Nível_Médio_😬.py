import streamlit as st
import random

st.set_page_config(page_title='Quiz TEC', page_icon='🎯')
st.sidebar.markdown('O objetivo deste jogo é promover os conhecimentos ensinados na disciplina de Teoria da Computação, lecionada pela professora Dra. Karina Rogia, durante o semestre 2023/1 na Universidade do Estado de Santa Catarina (UDESC - CCT). Desenvolvido por Guilherme Tomaselli Borchardt.')
st.sidebar.write("---")

@st.cache_data(show_spinner=False)
def gerar_lista_aleatoria():

    lista = random.sample(range(0, 5), 5)
    
    return lista

perguntas = [
    "Pela definição do Sipser, uma Máquina de Turing possui quantos elementos?",
    "Uma Máquina de Turing Multi-Fita possui mais poder computácional do que uma Máquina de Turing convencionál?",
    "Quais são os movimentos que o cabeçote pode realizar na fita durante o processamento de uma Máquina de Turing convencionál?",
    "O que significa que uma linguagem é decidível?",
    "Quem escreveu o livro 'Dom Quixote'?",
    "Qual é a empresa mais valiosa do mundo?"
]

respostas = [
    ["5", "Infinitos", "7", "Quantos forem necessários"],
    ["Sim", "Depende da quantidade de fitas", "Apenase se possuir mais do que 2 fitas", "Não"],
    ["Direita e esquerda", "Apenas esquerda", "Apenas direita", "Direita, esquerda e estacionário"],
    ["Yen", "Won", "Dólar", "Euro"],
    ["Miguel de Cervantes", "Jorge Luis Borges", "Gabriel García Márquez", "Pablo Neruda"], 
    ["Microsoft", "Google", "Apple", "Coca-Cola", "Adidas"]
]

alternativas = [2, 3, 0, 0, 0, 2]

st.header('Bem Vindo ao Nível Médio 😬')

lista = gerar_lista_aleatoria()

acertos = 0

for i in lista:

    st.write("---")
    st.subheader(perguntas[i])
    resposta = st.radio("", respostas[i], label_visibility = 'hidden')

    verificar = st.button('Verificar', key=i)
    if(verificar):

        if respostas[i].index(resposta) == alternativas[i]:
            acertos += 1
            st.success('Boa! Essa você acertou.')
        else:
            st.error(f'Que pena, essa você errou. A {alternativas[i]+1}ª alternativa era a correta.')
