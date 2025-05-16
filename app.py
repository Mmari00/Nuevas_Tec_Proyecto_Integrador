import streamlit as st
import pandas as pd
import numpy as np


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



