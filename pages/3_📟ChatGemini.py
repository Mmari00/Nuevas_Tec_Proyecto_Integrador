import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
import datetime

st.set_page_config(
    page_icon="📎",
    layout="wide"
)


# Configura tu clave API de Gemini
genai.configure(api_key="AIzaSyB0vSd-noKAywWSb5fhCf6BakbO-Y9T0po")  # 🔒 Cámbiala por la real

# Configuración general de la página
st.title("🎓 Agente de Apoyo para Clases")
st.markdown("Haz preguntas sobre lo visto en clase y el agente puede generar un resumen en PDF para los estudiantes que faltaron.")

# Pregunta inicial
pregunta = st.text_input(
    "¿Qué deseas consultar hoy sobre la clase?",
    placeholder="Ej. ¿Qué hicimos hoy en clase de Programación?"
)

# Botón para continuar
if st.button("Generar Cronograma para Ausente") and pregunta:
    with st.spinner("Consultando al agente..."):

        contexto = (
            "Actúa como un asistente escolar. Alguien te pregunta qué se hizo hoy en clase. "
            "Tu trabajo es preguntar si quieres generar un resumen completo en PDF con la siguiente estructura:\n"
            "- Lo realizado en clase\n"
            "- Tareas o trabajos pendientes\n"
            "- Información importante\n"
            "- Recomendaciones adicionales\n\n"
            "Tu respuesta debe estar lista para ser convertida a un PDF informativo y profesional. "
            "Asegúrate de responder con estructura clara y formal, como si fuera una nota para enviar al estudiante ausente.\n\n"
        )

        prompt_final = contexto + pregunta

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_final)
        texto_pdf = response.text

        st.subheader("Vista previa del contenido:")
        st.markdown(texto_pdf)

        # Función para generar PDF
        def generar_pdf(texto):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for linea in texto.split('\n'):
                pdf.multi_cell(0, 10, linea)
            nombre_archivo = f"Resumen_Clase_{datetime.date.today()}.pdf"
            ruta = f"/mnt/data/{nombre_archivo}"
            pdf.output(ruta)
            return ruta

        if st.button("📄 Descargar resumen en PDF"):
            ruta_pdf = generar_pdf(texto_pdf)
            st.success("PDF generado con éxito. Puedes descargarlo a continuación:")
            st.download_button("⬇ Descargar PDF", file_name="ResumenClase.pdf", data=open(ruta_pdf, "rb"), mime="application/pdf")

else:
    st.info("Ingresa una pregunta para generar el resumen de clase.")
