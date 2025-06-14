from sqlalchemy import create_engine, text
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import time

username = "root"
password = "marimysql"
host = "localhost"
database = "api_pi"
NOMBRE_TABLA_ASISTENCIA = "assistance"


engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")


# st.title("Análisis de datos de la base")


# with engine.connect() as conn:
#     result = conn.execute(text("SHOW TABLES"))
#     tablas = [fila[0] for fila in result]


# if tablas:
#     tabla_seleccionada = st.selectbox("Selecciona una tabla", tablas)

    
#     df = pd.read_sql(f"SELECT * FROM {tabla_seleccionada}", con=engine)
#     st.subheader(f"Datos de la tabla: {tabla_seleccionada}")
#     st.dataframe(df)

    
#     st.subheader("Análisis básico:")
#     st.write("Número de registros:", len(df))
#     st.write("Columnas:", df.columns.tolist())
#     # st.write("Resumen estadístico:")
#     # st.write(df.describe())


    
# else:
#     st.warning("No hay tablas disponibles en la base de datos.")

# st.title("🚀 ¡Potencia Tu Análisis! Panel Dinámico de Asistencia 📊")
# st.markdown("---")

# st.markdown(f"### ✨ Descubre Insights Clave: Visualización Activa para la Tabla: `{NOMBRE_TABLA_ASISTENCIA}`")
# activar_visualizacion = st.checkbox("✅ **¡Haz Clic Aquí para Revelar el Análisis de Datos de Asistencia!**")

# if activar_visualizacion:
#     df_asistencia = pd.DataFrame()
#     try:
#         df_asistencia = pd.read_sql(f"SELECT id, estado, fecha, hora FROM {NOMBRE_TABLA_ASISTENCIA}", con=engine)
#     except Exception as e:
#         st.error(f"🚫 **¡Fallo al Cargar Datos de la Tabla '{NOMBRE_TABLA_ASISTENCIA}'!** Esto puede deberse a que la tabla no existe o que faltan columnas cruciales como 'id', 'estado', 'fecha' o 'hora'. Por favor, **verifique la estructura de su tabla**. Detalles: {e}")
#         st.stop()

#     if not df_asistencia.empty:
#         if 'fecha' not in df_asistencia.columns:
#             st.warning("⚠️ **¡Alerta de Datos!** La columna 'fecha' es indispensable y no fue encontrada en la tabla. El análisis cronológico no podrá realizarse.")
#             st.stop()
#         if 'estado' not in df_asistencia.columns:
#             st.warning("⚠️ **¡Alerta de Datos!** La columna 'estado' es fundamental para la clasificación de asistencia y no se ha detectado. El análisis de estados no será posible.")
#             st.stop()

#         df_asistencia['fecha'] = pd.to_datetime(df_asistencia['fecha'])

#         df_conteo_estado = df_asistencia.groupby(['fecha', 'estado']).size().reset_index(name='conteo')

#         fig_agrupado = px.bar(
#             df_conteo_estado,
#             x='fecha',
#             y='conteo',
#             color='estado',
#             barmode='group',
#             title=f'📈 **Tendencias Diarias Detalladas:** Conteo de Asistencia por Estado en "{NOMBRE_TABLA_ASISTENCIA}"',
#             labels={'conteo': 'Cantidad de Registros', 'fecha': 'Fecha de Registro', 'estado': 'Estado de Asistencia'},
#             category_orders={"estado": sorted(df_conteo_estado['estado'].unique().tolist())}
#         )

#         df_estado_general = df_asistencia['estado'].value_counts().reset_index()
#         df_estado_general.columns = ['estado', 'conteo']
#         fig_pie = px.pie(
#             df_estado_general,
#             names='estado',
#             values='conteo',
#             title='🥧 **Radiografía de Asistencia:** Distribución General de Estados',
#         )

#         st.markdown("---")
#         st.markdown("### 🔑 **¡Resultados Visuales Impresionantes Aquí!**")

#         st.plotly_chart(fig_agrupado, use_container_width=True)
#         st.plotly_chart(fig_pie, use_container_width=True)

#     else:
#         st.info(f"ℹ️ **¡Información Importante!** La tabla '{NOMBRE_TABLA_ASISTENCIA}' no contiene datos. No hay información disponible para generar gráficos visuales.")

# else:
#     st.info("👆 **¡Inicia tu Análisis Ahora!** Por favor, activa la casilla de verificación para cargar los datos y visualizar el rendimiento de asistencia.")


st.title("🚀 Panel Dinámico de Datos 📊")
st.markdown("---")

st.markdown("### 🔍 **Tablas de Base de Datos**")
st.write("Selecciona cualquier tabla de tu base de datos para ver su contenido y un resumen rápido.")

tablas = []
with st.spinner('Cargando la lista de tablas disponibles... 🌐'):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SHOW TABLES"))
            tablas = [fila[0] for fila in result]
        time.sleep(0.5)
    except Exception as e:
        st.error(f"🚫 **¡Fallo al Listar Tablas!** No pudimos recuperar las tablas de tu base de datos. Detalles: {e}")

if tablas:
    tabla_seleccionada = st.selectbox("🎯 **Elige una tabla para comenzar la aventura de datos:**", tablas)

    with st.spinner(f'Cargando todos los registros de la tabla `{tabla_seleccionada}`... ⚡'):
        try:
            df = pd.read_sql(f"SELECT * FROM {tabla_seleccionada}", con=engine)
            time.sleep(1)
        except Exception as e:
            st.error(f"🚫 **¡Error al Cargar Datos!** No pudimos obtener los datos de `{tabla_seleccionada}`. ¿Podría ser un problema de permisos o estructura? Detalles: {e}")
            df = pd.DataFrame()

    if not df.empty:
        st.success(f"🎉 **¡Datos de la tabla `{tabla_seleccionada}` cargados con éxito!**")
        st.markdown(f"#### Contenido Completo de `{tabla_seleccionada}`:")
        st.dataframe(df)

        st.markdown("---")
        st.markdown("#### 📈 **Análisis Básico al Instante:**")
        st.write(f"🔢 **Número Total de Registros:** `{len(df)}` filas vibrantes esperan tu análisis.")
        st.write(f"📋 **Columnas Disponibles:** `{', '.join(df.columns.tolist())}`.")
        
        
    else:
        st.info(f"ℹ️ **¡Atención!** La tabla `{tabla_seleccionada}` parece estar vacía. No hay registros para mostrar o analizar.")

else:
    st.warning("⚠️ **¡No se Encontraron Tablas!** Tu base de datos no contiene tablas o hubo un problema al listarlas.")

st.markdown("---")
st.title("🚀 Panel Dinámico de Asistencia 📊")
st.markdown("---")

st.markdown(f"### ✨ Descubre Insights Clave: Visualización Activa para la Tabla: `{NOMBRE_TABLA_ASISTENCIA}`")
activar_visualizacion = st.checkbox("✅ **¡Haz Clic Aquí para Revelar el Análisis de Datos de Asistencia!**")

if activar_visualizacion:
    df_asistencia = pd.DataFrame()
    with st.spinner('Cargando tus datos de asistencia... ¡Un momento por favor! ⏳'):
        try:
            df_asistencia = pd.read_sql(f"SELECT id, estado, fecha, hora FROM {NOMBRE_TABLA_ASISTENCIA}", con=engine)
            time.sleep(1)
        except Exception as e:
            st.error(f"🚫 **¡Fallo al Cargar Datos de la Tabla '{NOMBRE_TABLA_ASISTENCIA}'!** Esto puede deberse a que la tabla no existe o que faltan columnas cruciales como 'id', 'estado', 'fecha' o 'hora'. Por favor, **verifique la estructura de su tabla**. Detalles: {e}")
            st.stop()

    if not df_asistencia.empty:
        st.success("🎉 ¡Datos cargados con éxito! Preparando tus visualizaciones... 🎉")

        if 'fecha' not in df_asistencia.columns:
            st.warning("⚠️ **¡Alerta de Datos!** La columna 'fecha' es indispensable y no fue encontrada en la tabla. El análisis cronológico no podrá realizarse.")
            st.stop()
        if 'estado' not in df_asistencia.columns:
            st.warning("⚠️ **¡Alerta de Datos!** La columna 'estado' es fundamental para la clasificación de asistencia y no se ha detectado. El análisis de estados no será posible.")
            st.stop()

        df_asistencia['fecha'] = pd.to_datetime(df_asistencia['fecha'])

        df_conteo_estado = df_asistencia.groupby(['fecha', 'estado']).size().reset_index(name='conteo')

        fig_agrupado = px.bar(
            df_conteo_estado,
            x='fecha',
            y='conteo',
            color='estado',
            barmode='group',
            title=f'📈 **Tendencias Diarias Detalladas:** Conteo de Asistencia por Estado en "{NOMBRE_TABLA_ASISTENCIA}"',
            labels={'conteo': 'Cantidad de Registros', 'fecha': 'Fecha de Registro', 'estado': 'Estado de Asistencia'},
            category_orders={"estado": sorted(df_conteo_estado['estado'].unique().tolist())}
        )

        df_estado_general = df_asistencia['estado'].value_counts().reset_index()
        df_estado_general.columns = ['estado', 'conteo']
        fig_pie = px.pie(
            df_estado_general,
            names='estado',
            values='conteo',
            title='🥧 **Radiografía de Asistencia:** Distribución General de Estados',
        )

        st.markdown("---")
        st.markdown("### 🔑 **¡Resultados Visuales Impresionantes Aquí!**")

        st.plotly_chart(fig_agrupado, use_container_width=True)
        st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("---")
        st.balloons()

    else:
        st.info(f"ℹ️ **¡Información Importante!** La tabla '{NOMBRE_TABLA_ASISTENCIA}' no contiene datos. No hay información disponible para generar gráficos visuales.")

else:
    st.info("👆 **¡Inicia tu Análisis Ahora!** Por favor, activa la casilla de verificación para cargar los datos y visualizar el rendimiento de asistencia.")