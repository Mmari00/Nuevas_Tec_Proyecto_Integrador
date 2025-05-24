import streamlit as st
import pandas as pd

st.set_page_config(   
    page_icon="📎",
    layout="wide"
)

import streamlit as st
import pandas as pd
from datetime import date

# Título de la aplicación
st.title("📚 Sistema de Toma de Asistencias")

# Fecha actual o seleccionada
fecha = st.date_input("📅 Selecciona la fecha de asistencia", value=date.today())

# Simulación de lista de estudiantes
estudiantes = ["Andrea Gómez", "Carlos Pérez", "Daniela Ramírez", "Juan Torres", "Lucía Fernández"]

# Diccionario inicial
asistencia = {nombre: False for nombre in estudiantes}

# Mostrar formulario de asistencia
st.subheader("✅ Marcar Asistencia")
for estudiante in estudiantes:
    asistencia[estudiante] = st.checkbox(estudiante)

# Convertir a DataFrame para mostrar
df_asistencia = pd.DataFrame({
    "Estudiante": list(asistencia.keys()),
    "Presente": list(asistencia.values()),
    "Fecha": fecha
})

# Mostrar tabla de resultados
st.subheader("📊 Resultado del Registro")
st.dataframe(df_asistencia)

# Botón para generar informe (exportar CSV)
if st.button("📥 Descargar informe"):
    df_asistencia.to_csv("informe_asistencia.csv", index=False)
    st.success("¡Informe generado exitosamente! Se guardó como 'informe_asistencia.csv'.")

