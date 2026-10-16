import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Repositorio de Aplicaciones - Juana",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.title("🤖 Repositorio")
    
    st.subheader("Acerca del Proyecto")
    parrafo = (
        "En este repositorio se encuentran centralizadas las distintas páginas "
        "web e interfaces interactivas diseñadas y desarrolladas a lo largo del "
        "semestre en la asignatura."
    )
    st.write(parrafo)
    
    st.markdown("---")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.subheader("Recursos Adicionales")
    st.markdown(f"📖 [Sitio Oficial de Guías y Ejercicios]({url_ia})")

# 3. Encabezado Principal
st.title("🚀 Repositorio de Aplicaciones")
st.write("Explora las diferentes páginas web desarrolladas a lo largo del semestre organizadas por fecha de clase.")

st.markdown("---")

# 4. Organización por Fechas usando Tabs (Incluyendo Primera y Segunda Entrega)
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📅 20 de Agosto", 
    "📅 27 de Agosto", 
    "📅 03 de Septiembre", 
    "📅 17 de Septiembre",
    "📅 24 de Septiembre",
    "📅 8 de Septiembre",
    "📅 15 de Septiembre"
])

# ---------------------------------------------------------
# PRIMERA ENTREGA
# ---------------------------------------------------------

# CLASE 1: 20 DE AGOSTO
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

# CLASE 2: 27 DE AGOSTO
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

# CLASE 3: 03 DE SEPTIEMBRE
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

# CLASE 4: 17 DE SEPTIEMBRE
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

# ---------------------------------------------------------
# SEGUNDA ENTREGA
# ---------------------------------------------------------

# CLASE 11
with tab5:
    st.markdown("---")
    st.subheader("📌 Segunda Entrega")
    st.header("Clase 11")
    st.caption("Sistemas RAG para lectura de documentos e inteligencia de visión computacional.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("📄 Chat PDF")
            st.write("Asistente RAG para consulta e interacción conversacional sobre documentos PDF.")
            st.link_button("Abrir Aplicación ↗", "https://chatpdfjuuu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("👁️ App Visión")
            st.write("Aplicación multimodal para análisis e interpretación visual de imágenes mediante modelos LLM.")
            st.link_button("Abrir Aplicación ↗", "https://visionapp-juu.streamlit.app/", use_container_width=True)

# CLASE 12
with tab6:
    st.markdown("---")
    st.subheader("📌 Segunda Entrega")
    st.header("Clase 12")
    st.caption("Reconocimiento de escritura a mano, tableros interactivos y modelos predictivos.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.subheader("✍️ Handwrite")
            st.write("Reconocimiento y predicción de dígitos escritos a mano utilizando el dataset MNIST.")
            st.link_button("Abrir Aplicación ↗", "https://mnistpredictjuuu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("🎨 Tablero Propio")
            st.write("Lienzo de dibujo interactivo para captura y procesamiento de trazos.")
            st.link_button("Abrir Aplicación ↗", "https://tableroropioju.streamlit.app/", use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("🔑 Tablero API Key")
            st.write("Reconocimiento de dibujos e interacción gráfica mediante integración con API Key externa.")
            st.link_button("Abrir Aplicación ↗", "https://drawrecogjuuu.streamlit.app/", use_container_width=True)

# CLASE 13
with tab7:
    st.markdown("---")
    st.subheader("📌 Segunda Entrega")
    st.header("Clase 13")
    st.caption("Protocolos IoT (MQTT), lectura de sensores y control por voz.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container(border=True):
            st.subheader("📡 Lector de Sensor MQTT")
            st.write("Recepción y visualización de datos de telemetría enviados en tiempo real vía MQTT.")
            st.link_button("Abrir Aplicación ↗", "https://recepmqtt-juu.streamlit.app/", use_container_width=True)

    with col2:
        with st.container(border=True):
            st.subheader("🎛️ MQTT Control")
            st.write("Panel domótico para envío de comandos de control analógicos y digitales hacia dispositivos IoT.")
            st.link_button("Abrir Aplicación ↗", "https://sendcmqtt-juu.streamlit.app/", use_container_width=True)

    with col3:
        with st.container(border=True):
            st.subheader("🎙️ Control de Voz")
            st.write("Interfaz de voz para transmisión de comandos hacia hardware simulado (Wokwi).")
            st.link_button("Abrir Aplicación ↗", "https://ctrlvoice-juu.streamlit.app/", use_container_width=True)

# Pie de página
st.markdown("---")
st.caption("⚡ Repositorio desarrollado con Streamlit")
