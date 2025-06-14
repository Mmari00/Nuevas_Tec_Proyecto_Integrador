import streamlit as st

st.set_page_config(page_title="Explicación del Dashboard", page_icon="💡", layout="centered")

# Encabezado elegante
st.markdown("""
<div style="background: linear-gradient(90deg, #24305E, #374785); padding: 20px; border-radius: 12px; text-align: center;">
    <h1 style="color: white;">📊 Dashboard de Tecnología</h1>
</div>
""", unsafe_allow_html=True)

st.markdown(""" """)
st.markdown("## 🗂 ¿Qué contiene esta base de datos?")
st.markdown("""
La base de datos contiene información sobre **profesionales del área tecnológica**, con los siguientes campos:

- 👤 **Nombre**
- 🛠️ **Especialidad tecnológica**
- 💻 **Lenguaje de programación favorito**
- 📜 **Certificación principal**
- ⚡ **Años de experiencia**
- 💰 **Salario actual (USD)**
- 🏆 **Número de certificaciones técnicas**
- 📦 **Repositorios en GitHub**
""")

st.markdown("---")

st.markdown("## 🎛️ ¿Qué filtros se pueden aplicar?")
st.markdown("""
Desde la barra lateral puedes aplicar estos filtros interactivos:

- 🔍 Buscar por nombre
- 👨‍💻 Especialidad tecnológica
- 💻 Lenguaje de programación favorito
- 📜 Certificación principal
- ⚡ Años de experiencia (rango)
- 💰 Salario actual (rango)
- 🏆 Número de certificaciones técnicas (rango)
- 📦 Repositorios en GitHub (rango)
""")


st.markdown("---")

st.markdown("## 📈 ¿Qué análisis visual se presenta?")
st.markdown("""
El dashboard genera visualizaciones como:

- 📊 **Gráfico de barras**: Certificaciones por lenguaje favorito.
- 📉 **Histograma**: Años de experiencia.
- 📈 **Gráfico de densidad**: Distribución de salarios.
- 🥧 **Gráfico de pastel**: Distribución de especialidades.
- 🌡️ **Mapa de calor**: Correlación entre variables.
- 💧 **Gráfico Waterfall**: Impacto acumulado de certificaciones y repositorios.
- 📐 **Gráfico de Pareto**: Especialidades con más certificaciones.
""")

st.markdown("---")

st.markdown("## ✅ ¿Para qué sirve este dashboard?")
st.markdown("""
Esta herramienta permite:

🔎 Explorar perfiles tecnológicos por distintos criterios.  
📊 Visualizar y comparar experiencia, salarios y certificaciones.  
🧠 Detectar especialidades más competitivas.  
📈 Entender relaciones entre variables clave del sector tech.
""")
