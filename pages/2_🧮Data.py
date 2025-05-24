import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_icon="📎",
    layout="wide"
)

# Sidebar: filtros sin selector de tema
st.sidebar.title("🔧 Configuración")

# Cargar datos
archivo_csv = 'static/datasets/tecnologia_registros.csv'
df = pd.read_csv(archivo_csv)

# Sidebar: filtros
st.sidebar.header("🎯 Filtros Interactivos")

nombre = st.sidebar.text_input("🔍 Buscar por Nombre:")

especialidad = st.sidebar.selectbox(
    "👨‍💻 Especialidad Tecnológica:",
    ["Todos"] + sorted(df["Especialidad tecnológica"].dropna().unique())
)

lenguaje = st.sidebar.selectbox(
    "💻 Lenguaje Favorito:",
    ["Todos"] + sorted(df["Lenguaje favorito"].dropna().unique())
)

certificacion = st.sidebar.selectbox(
    "📜 Certificación:",
    ["Todos"] + sorted(df["Certificación principal"].dropna().unique())
)

experiencia = st.sidebar.slider(
    "⚡ Años de Experiencia:",
    int(df["Años de experiencia"].min()),
    int(df["Años de experiencia"].max()),
    (int(df["Años de experiencia"].min()), int(df["Años de experiencia"].max()))
)

salario = st.sidebar.slider(
    "💰 Rango Salarial (USD):",
    int(df["Salario actual (USD)"].min()),
    int(df["Salario actual (USD)"].max()),
    (int(df["Salario actual (USD)"].min()), int(df["Salario actual (USD)"].max()))
)

certificaciones = st.sidebar.slider(
    "🏆 Número de Certificaciones:",
    int(df["Número de certificaciones técnicas"].min()),
    int(df["Número de certificaciones técnicas"].max()),
    (int(df["Número de certificaciones técnicas"].min()), int(df["Número de certificaciones técnicas"].max()))
)

repositorios = st.sidebar.slider(
    "📦 Repositorios en GitHub:",
    int(df["Repositorios en GitHub"].min()),
    int(df["Repositorios en GitHub"].max()),
    (int(df["Repositorios en GitHub"].min()), int(df["Repositorios en GitHub"].max()))
)

# Aplicar filtros
df_filtrado = df[
    (df["Años de experiencia"] >= experiencia[0]) & (df["Años de experiencia"] <= experiencia[1]) &
    (df["Salario actual (USD)"] >= salario[0]) & (df["Salario actual (USD)"] <= salario[1]) &
    (df["Número de certificaciones técnicas"] >= certificaciones[0]) & (df["Número de certificaciones técnicas"] <= certificaciones[1]) &
    (df["Repositorios en GitHub"] >= repositorios[0]) & (df["Repositorios en GitHub"] <= repositorios[1])
]

if nombre:
    df_filtrado = df_filtrado[df_filtrado["Nombre"].str.contains(nombre, case=False)]

if especialidad != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Especialidad tecnológica"] == especialidad]

if lenguaje != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Lenguaje favorito"] == lenguaje]

if certificacion != "Todos":
    df_filtrado = df_filtrado[df_filtrado["Certificación principal"] == certificacion]

# Encabezado elegante
st.markdown("""
<div style="background: linear-gradient(90deg, #374785, #24305E); 
            padding:10px; 
            border-radius:10px; 
            text-align:center;">
    <h1 style="color:white;">📊 Dashboard de Tecnología 📊</h1>
</div>
""", unsafe_allow_html=True)

# Mostrar DataFrame filtrado
st.markdown("<h2 style='text-align: center;'>📁 Resultados Filtrados</h2>", unsafe_allow_html=True)
st.dataframe(df_filtrado, use_container_width=True)

# Gráficos
st.markdown("<h2 style='text-align: center;'>📈 Análisis Visual</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

# Gráfico barras
fig_bar = px.bar(df_filtrado, x="Lenguaje favorito", y="Número de certificaciones técnicas", color="Especialidad tecnológica",
                 title="Certificaciones Técnicas por Lenguaje")
col1.plotly_chart(fig_bar, use_container_width=True)

# Histograma
fig_hist = px.histogram(df_filtrado, x="Años de experiencia", nbins=20, color="Especialidad tecnológica",
                        title="Histograma de Años de Experiencia")
col2.plotly_chart(fig_hist, use_container_width=True)

# Densidad (KDE)
fig_kde = px.histogram(df_filtrado, x="Salario actual (USD)", color="Especialidad tecnológica",
                       histnorm='density', marginal="rug", nbins=30,
                       title="Distribución de Salarios (Densidad)")
st.plotly_chart(fig_kde, use_container_width=True)

# Pie chart
fig_pie = px.pie(df_filtrado, names="Especialidad tecnológica", values="Número de certificaciones técnicas",
                 title="Distribución de Especialidades")
st.plotly_chart(fig_pie, use_container_width=True)

# Mapa de calor correlación
corr = df_filtrado[[
    "Años de experiencia", "Salario actual (USD)", "Número de certificaciones técnicas", "Repositorios en GitHub"
]].corr()

fig_heat = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', title="Mapa de Calor: Correlación Variables")
st.plotly_chart(fig_heat, use_container_width=True)

# Waterfall
fig_waterfall = go.Figure(go.Waterfall(
    name="Waterfall",
    orientation="v",
    measure=["relative", "relative", "total"],
    x=["Certificaciones Técnicas", "Repositorios GitHub", "Total"],
    text=["+", "+", ""],
    y=[
        df_filtrado["Número de certificaciones técnicas"].sum(),
        df_filtrado["Repositorios en GitHub"].sum(),
        0
    ],
    connector={"line":{"color":"rgb(63, 63, 63)"}}
))
fig_waterfall.update_layout(title="Gráfico Waterfall: Certificaciones y Repositorios")
st.plotly_chart(fig_waterfall, use_container_width=True)

# Pareto
df_pareto = df_filtrado.groupby("Especialidad tecnológica")["Número de certificaciones técnicas"].sum().sort_values(ascending=False)
df_pareto = df_pareto.reset_index()
df_pareto["Porcentaje"] = 100 * df_pareto["Número de certificaciones técnicas"] / df_pareto["Número de certificaciones técnicas"].sum()
df_pareto["Porcentaje acumulado"] = df_pareto["Porcentaje"].cumsum()

fig_pareto = go.Figure()
fig_pareto.add_trace(go.Bar(
    x=df_pareto["Especialidad tecnológica"],
    y=df_pareto["Número de certificaciones técnicas"],
    name="Certificaciones Técnicas"
))
fig_pareto.add_trace(go.Scatter(
    x=df_pareto["Especialidad tecnológica"],
    y=df_pareto["Porcentaje acumulado"],
    name="Porcentaje acumulado",
    yaxis="y2",
    mode="lines+markers"
))
fig_pareto.update_layout(
    title="Gráfico Pareto: Certificaciones Técnicas por Especialidad",
    yaxis=dict(title="Número de Certificaciones"),
    yaxis2=dict(title="Porcentaje acumulado", overlaying="y", side="right", range=[0, 110]),
    legend=dict(x=0.8, y=1.1)
)
st.plotly_chart(fig_pareto, use_container_width=True)
