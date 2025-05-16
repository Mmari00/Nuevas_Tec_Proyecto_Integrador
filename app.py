import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Proyecto Intregador")


#DataFrame
st.subheader("DataFrame: ")
archivo_csv = 'static/datasets/tecnologia_registros.csv'
dataframe_csv = pd.read_csv(archivo_csv)
st.dataframe(dataframe_csv)


st.subheader("Filtro por lenguaje: ")
lenguaje = st.selectbox("Selecciona un lenguaje", dataframe_csv["Lenguaje favorito"].unique())
df_lenguaje = dataframe_csv[dataframe_csv["Lenguaje favorito"] == lenguaje]
st.write("Datos filtrados: ")
st.dataframe(df_lenguaje)



st.title("Análisis de Datos Tecnológicos")

opcion = st.selectbox("Seleccione una variable para visualizar", ["Edad", "Años de experiencia", "Salario actual (USD)"])

fig, ax = plt.subplots()
sns.histplot(dataframe_csv[opcion], bins=20, kde=True, ax=ax)
ax.set_title(f"Distribución de {opcion}")
ax.set_xlabel(opcion)
ax.set_ylabel("Frecuencia")
st.pyplot(fig)
