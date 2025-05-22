import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(   
    page_icon="📎",
    layout="wide"
)
#DataFrame

archivo_csv = 'static/datasets/tecnologia_registros.csv'
dataframe_csv = pd.read_csv(archivo_csv)


st.markdown("""
<div style="background: linear-gradient(90deg, #FF007F, #8E44AD); 
            padding:5px; 
            border-radius:10px; 
            text-align:center;">
    <h2 style="color:white;">⚡ ¡DATAFRAME! ⚡</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3]) 

with col1:  
    st.subheader("🔗 FILTROS GENERALES 🔗" )
    nombre = st.text_input("🔍 Buscar por Nombre:")
    especialidad = st.selectbox("👨‍💻 Especialidad Tecnológica:", ["Todos"] + list(dataframe_csv["Especialidad tecnológica"].unique()))
    lenguaje = st.selectbox("💻 Lenguaje Favorito:", ["Todos"] + list(dataframe_csv["Lenguaje favorito"].unique()))
    certificacion = st.selectbox("📜 Certificación:", ["Todos"] + list(dataframe_csv["Certificación principal"].unique()))

with col2:  
    st.subheader("📊 FILTROS DE BARRA 📊")
    experiencia = st.slider("⚡ Años de Experiencia:", int(dataframe_csv["Años de experiencia"].min()), int(dataframe_csv["Años de experiencia"].max()),
                            (dataframe_csv["Años de experiencia"].min(), dataframe_csv["Años de experiencia"].max()))

    salario = st.slider("💰 Rango Salarial (USD):", int(dataframe_csv["Salario actual (USD)"].min()), int(dataframe_csv["Salario actual (USD)"].max()),
                        (dataframe_csv["Salario actual (USD)"].min(), dataframe_csv["Salario actual (USD)"].max()))

    certificaciones = st.slider("🏆 Número de Certificaciones:", int(dataframe_csv["Número de certificaciones técnicas"].min()),
                                int(dataframe_csv["Número de certificaciones técnicas"].max()),
                                (dataframe_csv["Número de certificaciones técnicas"].min(), dataframe_csv["Número de certificaciones técnicas"].max()))

    repositorios = st.slider("📦 Repositorios en GitHub:", int(dataframe_csv["Repositorios en GitHub"].min()),
                            int(dataframe_csv["Repositorios en GitHub"].max()),
                            (dataframe_csv["Repositorios en GitHub"].min(), dataframe_csv["Repositorios en GitHub"].max()))


dataframe_csv_filtered = dataframe_csv[
    (dataframe_csv["Años de experiencia"] >= experiencia[0]) & (dataframe_csv["Años de experiencia"] <= experiencia[1]) &
    (dataframe_csv["Salario actual (USD)"] >= salario[0]) & (dataframe_csv["Salario actual (USD)"] <= salario[1]) &
    (dataframe_csv["Número de certificaciones técnicas"] >= certificaciones[0]) & (dataframe_csv["Número de certificaciones técnicas"] <= certificaciones[1]) &
    (dataframe_csv["Repositorios en GitHub"] >= repositorios[0]) & (dataframe_csv["Repositorios en GitHub"] <= repositorios[1])
]

if nombre:
    dataframe_csv_filtered = dataframe_csv_filtered[dataframe_csv_filtered["Nombre"].str.contains(nombre, case=False)]
if especialidad != "Todos":
    dataframe_csv_filtered = dataframe_csv_filtered[dataframe_csv_filtered["Especialidad tecnológica"] == especialidad]
if lenguaje != "Todos":
    dataframe_csv_filtered = dataframe_csv_filtered[dataframe_csv_filtered["Lenguaje favorito"] == lenguaje]
if certificacion != "Todos":
    dataframe_csv_filtered = dataframe_csv_filtered[dataframe_csv_filtered["Certificación principal"] == certificacion]

st.markdown("<h2 style='text-align: center;'>⚙️ DATAFRAME FILTRADO ⚙️</h2>", unsafe_allow_html=True)
st.dataframe(dataframe_csv_filtered)




st.markdown("""
<div style="background: linear-gradient(90deg, #00F5FF, #FF1493); 
            padding:5px; 
            border-radius:10px; 
            text-align:center;">
    <h2 style="color:white;">🌐 ¡GRÁFICOS! 🌐</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)



# col12, col13 = st.columns([1,1])

# # Gráfico de torta: Distribución de Especialidades Tecnológicas
# fig1 = px.pie(dataframe_csv_filtered, values=dataframe_csv_filtered["Número de certificaciones técnicas"],
#               names=dataframe_csv_filtered["Especialidad tecnológica"], title="Distribución de Especialidades Tecnológicas",
#               color=dataframe_csv_filtered["Especialidad tecnológica"], color_discrete_sequence=px.colors.qualitative.Set3)
# col12.plotly_chart(fig1, use_container_width=True)

# # Gráfico de barras agrupadas: Comparación de certificaciones según lenguaje
# fig2 = px.bar(dataframe_csv_filtered, x="Lenguaje favorito", y="Número de certificaciones técnicas",
#               color="Especialidad tecnológica", title="Certificaciones según Lenguaje de Programación",
#               barmode="group", hover_name="Especialidad tecnológica")
# col13.plotly_chart(fig2, use_container_width=True)

# col14 = st.columns([1])[0]

# # Gráfico de dispersión con hover mejorado: Relación entre experiencia y salario
# fig3 = px.scatter(dataframe_csv_filtered, x="Años de experiencia", y="Salario actual (USD)", 
#                   color="Especialidad tecnológica", size="Número de certificaciones técnicas",
#                   hover_data=["Nombre", "Lenguaje favorito"],
#                   title="Experiencia vs. Salario con Certificaciones")
# col14.plotly_chart(fig3, use_container_width=True)


col1, col2 = st.columns([1,1])

# Gráfico de líneas: Tendencia de salario por años de experiencia
fig_line = px.line(dataframe_csv_filtered, x="Años de experiencia", y="Salario actual (USD)", 
                   title="Tendencia de Salario por Años de Experiencia", 
                   markers=True, color="Especialidad tecnológica")
col1.plotly_chart(fig_line, use_container_width=True)

# Gráfico de área: Certificaciones acumuladas por lenguaje
fig_area = px.area(dataframe_csv_filtered, x="Lenguaje favorito", y="Número de certificaciones técnicas", 
                   color="Especialidad tecnológica", title="Certificaciones Acumuladas por Lenguaje")
col2.plotly_chart(fig_area, use_container_width=True)

col3 = st.columns([1])[0]

# Gráfico de barras horizontales: Certificaciones por especialidad
fig_barras = px.bar(dataframe_csv_filtered, y="Especialidad tecnológica", x="Número de certificaciones técnicas", 
                    color="Lenguaje favorito", title="Certificaciones según Especialidad", orientation="h")
col3.plotly_chart(fig_barras, use_container_width=True)







st.sidebar.markdown("🎨 **Personaliza la página:**")
tema = st.sidebar.radio("Selecciona un tema de color:", ["Claro", "Oscuro"])

if tema == "Oscuro":
    st.markdown("""
    <style>
        .stApp {
            background-color: #2e3b4e;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

elif tema == "Claro":
    st.markdown("""
    <style>
        .stApp {
            background-color: #ffffff;
            color: black;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: black !important;
        }
    </style>
    """, unsafe_allow_html=True)
