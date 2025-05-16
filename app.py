import streamlit as st
import pandas as pd
import numpy as np


st.markdown("Proyecto Intregador")


#DataFrame
st.subheader("DataFrame")
archivo_csv = 'static/datasets/tecnologia_registros.csv'
dataframe_csv = pd.read_csv(archivo_csv)
st.dataframe(dataframe_csv)