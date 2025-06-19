
import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")
st.title("🖼️ Enquadre seu Mundo")

st.markdown("Simule seus quadros favoritos no ambiente desejado!")

# Ambientes padrões
ambientes = {
    "Sala de Estar": "https://i.imgur.com/hvV6BPv.jpg",
    "Quarto Minimalista": "https://i.imgur.com/6F0YOeD.jpg",
    "Escritório Moderno": "https://i.imgur.com/ZgOrDsG.jpg"
}

# Upload do usuário
st.sidebar.subheader("1. Escolha o Ambiente")
ambiente_tipo = st.sidebar.radio("Tipo de ambiente:", ["Usar um ambiente padrão", "Enviar minha parede"])

if ambiente_tipo == "Usar um ambiente padrão":
    ambiente_nome = st.sidebar.selectbox("Ambiente:", list(ambientes.keys()))
    ambiente_path = ambientes[ambiente_nome]
    st.image(ambiente_path, use_column_width=True)
else:
    uploaded_ambiente = st.sidebar.file_uploader("Envie uma imagem do seu ambiente", type=["jpg", "png"])
    if uploaded_ambiente:
        img = Image.open(uploaded_ambiente)
        st.image(img, caption="Seu ambiente", use_container_width=True)

st.sidebar.subheader("2. Escolha um Quadro")
quadros = {
    "Trio Botânico 1": "26 copia 2_resized.jpg",
    "Trio Botânico 2": "26 (1)_resized.jpg",
    "Trio Orgânico": "22 copia 2_resized.jpg"
}
quadro_nome = st.sidebar.selectbox("Quadros disponíveis:", list(quadros.keys()))
quadro_path = quadros[quadro_nome]
quadro_img = Image.open(os.path.join(".", quadro_path))

st.sidebar.subheader("3. Tamanho do Quadro")
largura = st.sidebar.slider("Largura do quadro (em % da tela):", 10, 100, 40)

st.markdown("---")
st.markdown(f"### Visualização com: {quadro_nome}")
st.image(quadro_img, width=int(8 * largura))

st.markdown(f"[🛒 Ver na loja](https://cabindecore.com.br/trios/)")
