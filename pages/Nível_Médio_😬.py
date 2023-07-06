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
    "Qual dos problemas a seguir não é um problema NP-Completo?",
    "A respeito dos critérios de aceitação, rejeição e loop, qual é a alternativa correta?",
    "Seja L1 uma linguagem decidível e sejam L2 e L3 linguagens reconhecíveis não decidíveis. Qual das afirmações a seguir não é necessariamente correta?",
    "Suponha que a linguagem X pertença à classe NP-Completo, a liguagem Y pertence à classe NP e que X ≤ Y e Y ≤ X. Quais das alternativas a seguir está correta?",
    "Existem linguagens decidíveis que possuem Máquina de Turing que eventualmente entre em loop?",
    "Se M é uma Máquina de Turing que entra em loop infinito para algumas entradas, então L(M) não é decidível?", 
    "Sobre o Problema da Parada, o que é correto afirmar?"
]

respostas = [
    ["Problema do ciclo hamiltoniano", "Problema do clique em grafos", "Problema da Correspondência de Post", "Nenhum dos problemas a cima"],
    ["Uma Máquina de Turing não determinística não entra em loop infinito", "Se um ramo da Máquina de Turing não determinística tiver comprimento infinito, então essa máquina entrou em loop infinito", "Uma Máquina de Turing não determinística para somente se todos os ramos de computação possíveis para a entrada pararem", "Se uma Máquina de Turing não determinística que não aceita a palavra de entrada, então ela rejeita"],
    ["L1 ∪ L2 é reconhecível", "L1 - L3 é reconhecível", "L2 - L1 é reconhecível", "L2 ∩ L1 é reconhecível"],
    ["Y pertence à classe P", "Y pertence à classe NP-Completa", "Todas as alternativas anteriores", "Nenhuma das alternativas anteriores"],
    ["Verdadeiro", "Falso"], 
    ["Verdadeiro", "Falso "],
    ["O problema da parada é decidível, o que significa que existe um algoritmo capaz de determinar se um programa irá parar ou não em uma entrada específica", "O problema da parada é indecidível, o que significa que não existe um algoritmo capaz de determinar se um programa irá parar ou não em uma entrada específica", "O problema da parada é resolvido através da aplicação de técnicas de otimização, que podem encontrar uma solução ótima para qualquer programa", "O problema da parada só ocorre em programas com erros de sintaxe ou semântica e pode ser corrigido através de depuração adequada"]
]

alternativas = [2, 2, 1, 1, 0, 1]

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
