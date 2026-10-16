import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob
import paho.mqtt.client as paho
import json
from gtts import gTTS
from googletrans import Translator

# Configuración de página con diseño estético
st.set_page_config(
    page_title="Control de Puerta por Voz - Smart Home",
    page_icon="🚪",
    layout="centered"
)

# Estilos CSS personalizados (incluye la corrección para eliminar bordes blancos en componentes de Bokeh)
st.markdown("""
    <style>
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    .main-header {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        padding: 24px;
        border-radius: 14px;
        border-left: 6px solid #38BDF8;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        text-align: center;
    }
    .card {
        background-color: #1E293B;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 15px;
        text-align: center;
    }
    /* Estilo para integrar el botón de Bokeh sin fondos blancos */
    .bk-root {
        display: flex;
        justify-content: center;
    }
    .bk-btn {
        background-color: #38BDF8 !important;
        color: #0F172A !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
    }
    .bk-btn:hover {
        background-color: #0EA5E9 !important;
    }
    </style>
""", unsafe_allow_html=True)

def on_publish(client, userdata, result):                     
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("ClienteJuana")
client1.on_message = on_message

# Encabezado estético de la interfaz multimodal
st.markdown("""
    <div class="main-header">
        <h1 style="color: #FFFFFF; margin: 0; font-size: 26px;">🚪 Control de Puerta por Voz</h1>
        <p style="color: #94A3B8; margin: 5px 0 0 0;">Interfaz Multimodal conectada con Wokwi vía MQTT</p>
    </div>
""", unsafe_allow_html=True)

# Contenedor y visualización de imagen centrada
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        image = Image.open('voice_ctrl.jpg')
        st.image(image, use_column_width=True)
    except Exception:
        pass

# Tarjeta principal para la interacción de voz
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎙️ Asistente de Acceso")
st.write("Di un comando como **'cerrar puerta'** para enviar la orden al simulador.")

# Botón de Bokeh
stt_button = Button(label="🎙️ Hablar para Cerrar Puerta", width=280)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        spoken_text = result.get("GET_TEXT")
        st.success(f"Comando reconocido: **{spoken_text}**")
        
        # Lógica de conexión y publicación MQTT intacta
        client1.on_publish = on_publish                                     
        client1.connect(broker, port)  
        message = json.dumps({"Act1": spoken_text.strip()})
        ret = client1.publish("voicejuana", message)

st.markdown('</div>', unsafe_allow_html=True)

try:
    os.mkdir("temp")
except:
    pass
