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
⚛️ React – Interfaz de usuario moderna.,
⚡ Vite – Entorno de desarrollo rápido.,
📦 NPM – Gestor de dependencias.,
🐍 Python + Streamlit – Backend y visualización rápida.,
""")

# Cómo ejecutar el proyecto,
st.subheader("🚀 ¿Cómo ejecutar el proyecto?")
st.markdown("""
Clona este repositorio.,
Ejecuta en la terminal: npm i,
Luego corre el proyecto con: npm run dev,
""")

# Integrantes del equipo,
st.subheader("👩‍💻 Integrantes del Proyecto")
st.markdown("""
Mariana Marulanda
🆔 1018234921
📧 1software.files1@gmail.com,

Sheyla Rodelo
🆔 1025891870
📧 rodelosheyla8@gamil.com,

Skarlet Castillo
🆔 1036691265
📧 genessisskarlet@gmail.com,
""")
# Pie de página,
st.markdown("---")
st.caption("Proyecto realizado con dedicación y aprendizaje ❤️")