import streamlit as st
import random

st.set_page_config(page_title='Quiz TEC', page_icon='🎯')
st.sidebar.markdown('O objetivo deste jogo é promover os conhecimentos ensinados na disciplina de Teoria da Computação, lecionada pela professora Dra. Karina Roggia, durante o semestre 2023/1 na Universidade do Estado de Santa Catarina (UDESC - CCT). Desenvolvido por Guilherme Tomaselli Borchardt.')
st.sidebar.write("---")

@st.cache_data(show_spinner=False, max_entries = 1)
def gerar_lista_aleatoria():

    lista = random.sample(range(0, 7), 5)
    
    return lista

perguntas = [
    "Pela definição do Sipser, uma Máquina de Turing é composta por quantos elementos?",
    "Uma Máquina de Turing Multi-Fita possui mais poder computácional do que uma Máquina de Turing de fita única?",
    "Quais são os movimentos que o cabeçote pode realizar na fita durante o processamento de uma Máquina de Turing definida por Sipser?",
    "Toda linguagem decidível possui uma Máquina de Turing que a reconheça?",
    "Se A é uma liguagem decidível qualquer. Então o complemento de A é reconhecível?",
    "O que signinica δ(q0, 0) = (q1, 1, E)?", 
    "A fita de entrada e a fita da máquina são iguais?"
]

respostas = [
    ["5", "Infinitos", "7", "Pelo menos um"],
    ["Sim", "Depende da quantidade de fitas", "Apenas se possuir mais do que 2 fitas", "Não"],
    ["Direita e esquerda", "Apenas esquerda", "Apenas direita", "Direita, esquerda e estacionário"],
    ["Verdadeiro", "Falso"],
    ["Verdadeiro", "Falso "], 
    ["Que a máquina partirá de q1 e irá escrever 1", "Que a máquina partirá de q0 e irá escrever 0", "Que a máquina partirá do estado 0 e irá para o estado 1", "Que a máquina partirá de q0 lendo 0 e irá para q0, escrevendo 1 e realizando o movimento do cabeçote para a direção esquerda da fita"],
    ["Verdadeiro ", "Falso"]
]

alternativas = [2, 3, 0, 0, 0, 3, 1]

st.header('Bem Vindo ao Nível Fácil 😊')

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
