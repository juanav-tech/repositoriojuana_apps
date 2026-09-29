import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Repositorio de Aplicaciones IA - Juana",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.title("🤖 Repositorio IA")
    
    st.subheader("Acerca del Proyecto")
    parrafo = (
        "En este repositorio se encuentran centralizadas las distintas páginas "
        "web e interfaces interactivas diseñadas y desarrolladas a lo largo del "
        "semestre en la asignatura."
    )
    st.write(parrafo)
    
    st.divider()
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.subheader("Recursos Adicionales")
    st.markdown(f"📖 [Sitio Oficial de Guías y Ejercicios]({url_ia})")

# 3. Encabezado Principal
st.title("🚀 Repositorio de Aplicaciones de Inteligencia Artificial")
st.write("Explora las diferentes páginas web desarrolladas a lo largo del semestre organizadas por fecha de clase.")

st.divider()

# 4. Organización por Fechas usando Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📅 20 de Agosto", 
    "📅 27 de Agosto", 
    "📅 03 de Septiembre", 
    "📅 17 de Septiembre"
])

# ---------------------------------------------------------
# CLASE 1: 20 DE AGOSTO
# ---------------------------------------------------------
with tab1:
    st.header("Clase: 20 de Agosto")
    st.caption("Introducción a interfaces interactivas y multimodalidad básica.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("🌐 Mi Primera App")
            st.write("Aplicación inicial para explorar el despliegue de modelos e interfaces en Streamlit.")
            st.link_button("Abrir Aplicación ↗", "https://miprimerappjuana.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("🔊 Texto a Audio")
            st.write("Interfaz multimodal capaz de procesar entrada de texto y sintetizar voz artificial.")
            st.link_button("Abrir Aplicación ↗", "https://interfacesmultiodalesj.streamlit.app/", use_container_width=True)

# ---------------------------------------------------------
# CLASE 2: 27 DE AGOSTO
# ---------------------------------------------------------
with tab2:
    st.header("Clase: 27 de Agosto")
    st.caption("Traducción de lenguaje natural, visión por computador u OCR.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.subheader("🗣️ Traductor")
            st.write("Herramienta para procesamiento y traducción automática de lenguaje natural.")
            st.link_button("Abrir Aplicación ↗", "https://traductorjuu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("📷 OCR Cámara")
            st.write("Reconocimiento óptico de caracteres en tiempo real utilizando entrada de cámara.")
            st.link_button("Abrir Aplicación ↗", "https://ocrcamara.streamlit.app/", use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("🎙️ OCR + Audio")
            st.write("Extracción de texto desde imágenes con lectura asistida mediante síntesis de voz.")
            st.link_button("Abrir Aplicación ↗", "https://ocr-audiojuu.streamlit.app/", use_container_width=True)

# ---------------------------------------------------------
# CLASE 3: 03 DE SEPTIEMBRE
# ---------------------------------------------------------
with tab3:
    st.header("Clase: 3 de Septiembre")
    st.caption("Procesamiento de Lenguaje Natural (PLN) y análisis de texto.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.subheader("☁️ Wordcloud Studio")
            st.write("Generador de nubes de palabras para análisis de frecuencia y representación visual de texto.")
            st.link_button("Abrir Aplicación ↗", "https://Wordclouddju.streamlit.app", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("😊 Análisis de Sentimientos")
            st.write("Clasificación de emociones y polaridad en textos mediante PLN.")
            st.link_button("Abrir Aplicación ↗", "https://sentimentalju.streamlit.app/", use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("📊 TF-IDF en Español")
            st.write("Cálculo de relevancia de palabras clave en corpus de texto en idioma español.")
            st.link_button("Abrir Aplicación ↗", "https://tdfespju.streamlit.app/", use_container_width=True)

# ---------------------------------------------------------
# CLASE 4: 17 DE SEPTIEMBRE
# ---------------------------------------------------------
with tab4:
    st.header("Clase: 17 de Septiembre")
    st.caption("Modelos avanzados de visión por computador y transferencia de aprendizaje.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("🔍 Detección de Objetos (YOLOv5)")
            st.write("Identificación y localización de múltiples objetos en imágenes utilizando el modelo YOLOv5.")
            st.link_button("Abrir Aplicación ↗", "https://yolov5juu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("🧠 Teachable Machine")
            st.write("Implementación de un modelo personalizado de clasificación de imágenes exportado de Teachable Machine.")
            st.link_button("Abrir Aplicación ↗", "https://teachablemju.streamlit.app/", use_container_width=True)

# Pie de página
st.divider()
st.caption("⚡ Repositorio desarrollado con Streamlit")
