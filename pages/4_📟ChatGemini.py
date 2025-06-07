import streamlit as st
import google.generativeai as genai
import datetime

st.set_page_config(page_title="Agente Escolar 📘", page_icon="📎", layout="wide")

# Configurar clave API de Gemini
genai.configure(api_key="AIzaSyB0vSd-noKAywWSb5fhCf6BakbO-Y9T0po")  # 🔒 Sustituye con tu clave real si la cambias

st.title("📘 Agente de Apoyo Escolar")
st.markdown("Este agente puede generar **resúmenes para estudiantes ausentes** o **planes de mejoramiento para docentes**.\n\n"
            "💡 *Recuerda especificar el curso para obtener una respuesta útil.*")

# Selección del tipo de solicitud
tipo = st.radio("¿Qué deseas generar?", ["📄 Resumen para estudiante ausente", "📋 Plan de mejoramiento para el profesor"])

# Entrada de la solicitud
pregunta = st.text_area(
    "✏️ Escribe tu solicitud (incluye el curso):",
    placeholder="Ej. ¿Qué se hizo hoy en clase de Matemáticas de 9°?, o Necesito plan de mejoramiento para Química 10°."
)

def contiene_curso(texto):
    palabras_clave = ["grado", "clase", "curso", "matemáticas", "español", "química", "física", "biología",
                      "sociales", "historia", "geografía", "inglés", "ética", "educación física", "tecnología"]
    return any(palabra.lower() in texto.lower() for palabra in palabras_clave)

if st.button("✨ Generar contenido") and pregunta:
    if not contiene_curso(pregunta):
        st.warning("⚠️ Por favor, especifica el curso o asignatura en tu solicitud.")
    else:
        with st.spinner("✍️ Generando contenido..."):

            # Contexto según el tipo
            if tipo == "📄 Resumen para estudiante ausente":
                contexto = (
                    "Actúa como un asistente escolar que redacta un resumen para un estudiante que no asistió a clase. "
                    "El resumen debe estar bien estructurado e incluir:\n"
                    "- ✅ Lo realizado en clase\n"
                    "- 📚 Tareas o trabajos pendientes\n"
                    "- 📌 Información importante\n"
                    "- 💡 Recomendaciones adicionales\n"
                    "Usa un tono formal y claro, como una nota enviada por el docente."
                )
            else:
                contexto = (
                    "Actúa como un asistente educativo que genera un plan de mejoramiento para un profesor. "
                    "El plan debe incluir:\n"
                    "- 🧪 Temas no comprendidos\n"
                    "- 📖 Recomendaciones de refuerzo\n"
                    "- 🎯 Actividades sugeridas\n"
                    "- 📝 Evaluación alternativa\n"
                    "Escribe de forma profesional y pedagógica, dirigido a un docente."
                )

            prompt = contexto + "\n\n" + pregunta
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            texto_generado = response.text

            st.subheader("📋 Vista previa del contenido:")
            st.markdown(texto_generado)

else:
    st.info("✉️ Por favor, escribe una solicitud que incluya el curso o asignatura.")
