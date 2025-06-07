import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 

st.set_page_config(
    page_title="Página Web Streamlit",
    page_icon="💻",
    layout="wide"
)

# Título principal,
st.title("🎓 Proyecto Integrador - Sistema de Toma de Asistencias")

# Descripción general,
st.markdown("""
Bienvenidos a nuestra aplicación web para el registro de asistencias académicas.
Este sistema permite a los profesores marcar la asistencia diaria de los estudiantes de forma ágil, y a los administradores generar informes claros y detallados.

Nuestro objetivo es modernizar el control escolar usando tecnologías web eficientes y amigables.

---
""")

# Tecnologías utilizadas,
st.subheader("🛠️ Tecnologías de Desarrollo")
st.markdown("""
        - ⚛️ React – Interfaz de usuario moderna.,
        - ⚡ Vite – Entorno de desarrollo rápido.,
        - 📦 NPM – Gestor de dependencias.,
        - 🐍 Python + Streamlit – Backend y visualización rápida.,
""")

st.markdown(""" """)

# Cómo ejecutar el proyecto,
st.subheader("🚀 ¿Cómo ejecutar el proyecto?")
st.markdown("""
        - Clona este repositorio.,
        - Ejecuta en la terminal: npm i,
        - Luego corre el proyecto con: npm run dev,
""")

st.markdown(""" """)

st.markdown("---")

# Sección de información del estudiante con diseño de dos columnas
col1, col2 = st.columns([1, 2])

# Columna izquierda: Foto del estudiante
with col1:
    st.image("assets\image.png", width=450, caption="Chikes", output_format="JPEG")

# Columna derecha: Información del estudiante
with col2:
    st.markdown('<h3 margin-top: 50px;">👩‍💻 Integrantes del Proyecto 👩‍💻</h3>', unsafe_allow_html=True)
    st.markdown(""" """)
    st.markdown('<p font-size: 30px>🗿 Skarlet Castillo  <span style="color: #0066cc; font-weight: bold; "> 📧genessisskarlet@gmail.com</span></p>', unsafe_allow_html=True)
    st.markdown(""" """)
    st.markdown('<p>🗿 Mariana Maruland  <span style="color: #0066cc; font-weight: bold;"> 📧1software.files1@gmail.com</p>', unsafe_allow_html=True)
    st.markdown(""" """)
    st.markdown('<p>🗿 Sheyla Rodelo  <span style="color: #0066cc; font-weight: bold;"> 📧rodelosheyla8@gamil.com</span></p>', unsafe_allow_html=True)
    st.markdown(""" """)
    st.markdown(""" """)
    st.markdown(""" """)
    st.caption("❤️ Proyecto realizado con amor y dedicación ❤️")

st.markdown("---")
