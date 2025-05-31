from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st

# Configuración de conexión a MySQL
username = "root"
password = "Genessiskarlet31510:"
host = "localhost"
database = "api_pi"

# Crear motor de conexión
engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")

st.title("Análisis de datos de la base")

# Obtener lista de tablas
with engine.connect() as conn:
    result = conn.execute(text("SHOW TABLES"))
    tablas = [fila[0] for fila in result]

# Mostrar tablas disponibles
if tablas:
    tabla_seleccionada = st.selectbox("Selecciona una tabla", tablas)

    # Leer tabla seleccionada como DataFrame
    df = pd.read_sql(f"SELECT * FROM {tabla_seleccionada}", con=engine)
    st.subheader(f"Datos de la tabla: {tabla_seleccionada}")
    st.dataframe(df)

    # Aquí ya puedes aplicar tus filtros y análisis:
    st.subheader("Análisis básico:")
    st.write("Número de registros:", len(df))
    st.write("Columnas:", df.columns.tolist())
    st.write("Resumen estadístico:")
    st.write(df.describe())

else:
    st.warning("No hay tablas disponibles en la base de datos.")





# import streamlit as st
# import pandas as pd
# from datetime import date

# st.set_page_config(
#     page_icon="📎",
#     layout="wide"
# )


# # Título de la aplicación,
# st.title("📚 Sistema de Toma de Asistencias")

# # Fecha actual o seleccionada,
# fecha = st.date_input("📅 Selecciona la fecha de asistencia", value=date.today())

# # Simulación de lista de estudiantes,
# estudiantes = ["Andrea Gómez", "Carlos Pérez", "Daniela Ramírez", "Juan Torres", "Lucía Fernández"]

# # Diccionario inicial,
# asistencia = {nombre: False for nombre in estudiantes}

# # Mostrar formulario de asistencia,
# st.subheader("✅ Marcar Asistencia")
# for estudiante in estudiantes:
#     asistencia[estudiante] = st.checkbox(estudiante)

#  # Convertir a DataFrame para mostrar,
# df_asistencia = pd.DataFrame({
#     "Estudiante": list(asistencia.keys()),
#     "Presente": list(asistencia.values()),
#     "Fecha": fecha
# })

# # Mostrar tabla de resultados,
# st.subheader("📊 Resultado del Registro")
# st.dataframe(df_asistencia)

# # Botón para generar informe (exportar CSV),
# if st.button("📥 Descargar informe"):
#     df_asistencia.to_csv("informe_asistencia.csv", index=False)
#     st.success("¡Informe generado exitosamente! Se guardó como 'informe_asistencia.csv'.")
