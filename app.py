import streamlit as st
from PIL import Image
import io
import requests

st.set_page_config(layout="wide")
st.title("🖼️ Enquadre seu Mundo")

st.markdown("Simule seus quadros favoritos no ambiente desejado!")

# Ambientes padrões com links novos
ambientes = {
    "Sala de Estar": "https://i.imgur.com/B4sFHTP.jpg",
    "Quarto Minimalista": "https://i.imgur.com/CV07aRS.jpg",
    "Escritório Moderno": "https://i.imgur.com/voJrsLy.jpg"
}

# Upload ou escolha do ambiente
st.sidebar.subheader("1. Escolha o Ambiente")
ambiente_tipo = st.sidebar.radio("Tipo de ambiente:", ["Usar um ambiente padrão", "Enviar minha parede"])

if ambiente_tipo == "Usar um ambiente padrão":
    ambiente_nome = st.sidebar.selectbox("Ambiente:", list(ambientes.keys()))
    url = ambientes[ambiente_nome]
    response = requests.get(url)
    ambiente_img = Image.open(io.BytesIO(response.content)).convert("RGBA")
else:
    uploaded_ambiente = st.sidebar.file_uploader("Envie uma imagem do seu ambiente", type=["jpg", "png"])
    if uploaded_ambiente:
        ambiente_img = Image.open(uploaded_ambiente).convert("RGBA")
    else:
        st.warning("Envie uma imagem para continuar.")
        st.stop()

# Escolha do quadro
st.sidebar.subheader("2. Escolha um Quadro")
quadros = {
    "Trio Botânico 1": "26 copia 2_resized.jpg",
    "Trio Botânico 2": "26 (1)_resized.jpg",
    "Trio Orgânico": "22 copia 2_resized.jpg"
}
quadro_nome = st.sidebar.selectbox("Quadros disponíveis:", list(quadros.keys()))
quadro_path = quadros[quadro_nome]
quadro_img = Image.open(quadro_path).convert("RGBA")

# Tamanho e posição do quadro
st.sidebar.subheader("3. Tamanho e Posição")
largura_quadro = st.sidebar.slider("Largura (px):", 100, 800, 300)
w_percent = largura_quadro / float(quadro_img.width)
altura_quadro = int(float(quadro_img.height) * w_percent)
quadro_img_resized = quadro_img.resize((largura_quadro, altura_quadro))

x = st.sidebar.slider("Posição horizontal (X):", 0, ambiente_img.width - largura_quadro, 100)
y = st.sidebar.slider("Posição vertical (Y):", 0, ambiente_img.height - altura_quadro, 100)

# Colar quadro no ambiente
ambiente_editado = ambiente_img.copy()
ambiente_editado.paste(quadro_img_resized, (x, y), quadro_img_resized)

# Exibir resultado final
st.image(ambiente_editado.convert("RGB"), caption="Visualização com quadro aplicado", use_container_width=True)
st.markdown("[🛒 Ver na loja](https://cabindecore.com.br/trios/)")
