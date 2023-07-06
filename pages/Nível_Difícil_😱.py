import streamlit as st
import random

st.cache_data.clear()

st.set_page_config(page_title='Quiz TEC', page_icon='🎯')
st.sidebar.markdown('O objetivo deste jogo é promover os conhecimentos ensinados na disciplina de Teoria da Computação, lecionada pela professora Dra. Karina Rogia, durante o semestre 2023/1 na Universidade do Estado de Santa Catarina (UDESC - CCT). Desenvolvido por Guilherme Tomaselli Borchardt.')
st.sidebar.write("---")

@st.cache_data(show_spinner=False)
def gerar_lista_aleatoria():

    lista = random.sample(range(0, 6), 5)
    
    return lista

perguntas = [
    "Quais das seguintes informações são verdadeiras?\n1. O problema de determinar se existe um ciclo em um grafo direcionado pertence à classe P.\n2. O problema de determinar se existe um ciclo em um grafo direcionado pertence à classe NP.\n3. Se A ∈ NP-Completo, então existe um algoritmo não determinístico que roda em tempo polinomial e decide A.",
    "Quais das seguintes linguagens são indecidíveis?\n1. {<G> | G é GLC e L(G) = Ø}\n2. {<G> | G é GLC e L(G) = ∑*}\n3. {<M> | M é MT e L(M) é liguagem regular}\n 4. {<A, N> | A é um AFD e N é um AFN e L(A) = L(N)}",
    "Quais das seguintes alternativas são falsas?\n1. Para qualquer Máquina de Turing não determinística, existe uma Máquina de Turing determinística equivalente\n2. Linguagens reconhecíveis são fechadas sobre as operações de união e complemento\n3. Linguagens decidíveis são fechadas para as operações de intersecção e complemento\n4. Linguagens reconhecíveis são fechadas sobre as operações de união e intersecção",
    "O que significa quando dizemos que um algoritmo P1 é assintoticamente mais eficiente do que o algoritmo P2?",
    "A é uma linguagem reconhecível se, e somente se, A ≤m Amt?",
    "Quais dos problemas a seguir são decidíveis?\n1. Dado programa P, P sempre produz uma saída?\n2. Se L é livre de contexto, então o complemento de L também é livre de contexto?\n3. Se L é regular, então o complemento de L também é regular?\n4. Se L é decidível, então o complemento de L também é decidível?"
]

respostas = [
    ["Todas", "Somente 1 e 3", "Somente 2 e 3", "Nenhuma"],
    ["Somente a número 3", "Somente as de número 3 e 4", "Somente as de número 2 e 3", "Nenhuma"],
    ["Somente a número 2", "Somente a número 3", "Somente as de número 1 e 4", "Nenhuma"],
    ["P1 sempre será uma escolha melhor do que P2 para entradas pequenas", "P1 sempre será uma escolha melhor do que P2 para entradas grandes", "P2 sempre será uma escolha melhor do que P1 para entradas pequenas", "P1 sempre será uma escolha melhor do que P2, independente do tamanho da entrada"],
    ["Verdadeiro", "Falso"], 
    ["2, 3 e 4", "1, 2, 3 e 4", "3 e 4", "1 e 2"]
]

alternativas = [0, 2, 0, 1, 0, 2]

st.header('Bem Vindo ao Nível Difícil 😱')

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
