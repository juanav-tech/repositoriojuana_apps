import streamlit as st
from PIL import Image

# 1. Configuración de la página
st.set_page_config(
    page_title="Repositorio de Aplicaciones IA - Juana",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado suave
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.title("🤖 Repositorio IA")
    st.image("https://images.unsplash.com/photo-1677442136019-21780efad99a?w=500&q=80", use_container_width=True)
    
    st.subheader("Acerca del Proyecto")
    parrafo = (
        "La Inteligencia Artificial permite mejorar la toma de decisiones "
        "con el uso de datos, automatizar tareas rutinarias y proporcionar "
        "análisis avanzados en tiempo real, lo que resulta en una mayor eficiencia "
        "y precisión en diversos campos."
    )
    st.write(parrafo)
    
    st.divider()
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.subheader("Recursos Adicionales")
    st.markdown(f"📖 [Sitio Oficial de Guías y Ejercicios]({url_ia})")

# 3. Encabezado Principal
st.title("🚀 Repositorio de Aplicaciones de Inteligencia Artificial")
st.write("Explora las diferentes aplicaciones desarrolladas a lo largo del curso organizadas por fecha de clase.")

st.divider()

# Función auxiliar para cargar imágenes locales con fallback a URL por defecto
def cargar_imagen(nombre_archivo, url_fallback):
    try:
        return Image.open(nombre_archivo)
    except Exception:
        return url_fallback

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
            img = cargar_imagen('txt_to_audio2.png', 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Aplicación inicial para explorar el despliegue de modelos e interfaces en Streamlit.")
            st.link_button("Abrir Aplicación ↗", "https://miprimerappjuana.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("🔊 Texto a Audio")
            img = cargar_imagen('txt_to_audio.png', 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Interfaz multimodal capaz de procesar entrada de texto y sintetizar voz sintetizada.")
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
            img = cargar_imagen('OIG8.jpg', 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Herramienta para procesamiento y traducción automática de lenguaje natural.")
            st.link_button("Abrir Aplicación ↗", "https://traductorjuu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("📷 OCR Cámara")
            img = cargar_imagen('data_analisis.png', 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Reconocimiento óptico de caracteres en tiempo real utilizando entrada de cámara.")
            st.link_button("Abrir Aplicación ↗", "https://ocrcamara.streamlit.app/", use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("🎙️ OCR + Audio")
            img = cargar_imagen('OIG3.jpg', 'https://images.unsplash.com/photo-1589254065878-42c9da997008?w=500&q=80')
            st.image(img, use_container_width=True)
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
            img = cargar_imagen('Chat_pdf.png', 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Generador de nubes de palabras para análisis de frecuencia y representación visual de texto.")
            st.link_button("Abrir Aplicación ↗", "https://Wordclouddju.streamlit.app", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("😊 Análisis de Sentimientos")
            img = cargar_imagen('OIG4.jpg', 'https://images.unsplash.com/photo-1507146426996-ef05306b995a?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Clasificación de emociones y polaridad en comentarios mediante PLN.")
            st.link_button("Abrir Aplicación ↗", "https://sentimentalju.streamlit.app/", use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("📊 TF-IDF en Español")
            img = cargar_imagen('OIG6.jpg', 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&q=80')
            st.image(img, use_container_width=True)
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
            img = cargar_imagen('OIG5.jpg', 'https://images.unsplash.com/photo-1535378273068-9bb67d5bfaca?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Identificación y localización de múltiples objetos en imágenes utilizando el modelo YOLOv5.")
            st.link_button("Abrir Aplicación ↗", "https://yolov5juu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("🧠 Teachable Machine")
            img = cargar_imagen('OIG5.jpg', 'https://images.unsplash.com/photo-1507146426996-ef05306b995a?w=500&q=80')
            st.image(img, use_container_width=True)
            st.write("Implementación de un modelo personalizado de clasificación de imágenes exportado de Teachable Machine.")
            st.link_button("Abrir Aplicación ↗", "https://teachablemju.streamlit.app/", use_container_width=True)

# Pie de página
st.divider()
st.caption("⚡ Repositorio desarrollado con Streamlit")

