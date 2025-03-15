import streamlit as st
import pandas as pd
import numpy as np
import cv2

# Título da aplicação
st.title('Minha Primeira Aplicação em Streamlit')

# Cria um widget de slider
x = st.slider('Selecione um valor para x', 0, 100, 50)

# Exibe o valor de x
st.write(f'O valor de x é {x}')

# Exemplo de gráfico simples
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Exemplo de tabela
st.write('Exemplo de tabela')
st.write(pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],
    'segunda coluna': [10, 20, 30, 40]
}))


# Exemplo de gráfico de mapa
st.write('Exemplo de Mapa')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-19.55, -43.56],
    columns=['lat', 'lon'])

st.map(map_data)



# criando botões
st.write('Exemplo botão')
img = cv2.imread('title.png')
if st.button('Clique para uma mensagem'):
    # st.write('Você clicou no botão!')
    # cv2.imshow('Imagem', img)
    st.image(img, channels="BGR")
    
    






