import streamlit as st
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Trivia Master IUT - TDA", page_icon="📺")

# --- 1. BASE DE DATOS DE 10 PREGUNTAS ---
if 'pool_preguntas' not in st.session_state:
    st.session_state.pool_preguntas = [
        {"p": "¿Cuál es la capital de Venezuela?",
         "o": ["Maracaibo", "Caracas", "Valencia", "Coro"],
         "c": "Caracas",
         "f": "Caracas es la capital y ciudad más poblada de Venezuela."},

        {"p": "¿Qué planeta es conocido como el Planeta Rojo?",
         "o": ["Venus", "Marte", "Júpiter", "Saturno"],
         "c": "Marte",
         "f": "Marte es conocido como el Planeta Rojo por su color debido al óxido de hierro."},

        {"p": "¿Cuántos bits tiene un byte?",
         "o": ["4", "16", "32", "8"],
         "c": "8",
         "f": "Un byte consta de 8 bits, la unidad básica de información en computación."},

        {"p": "¿Quién pintó la Mona Lisa?",
         "o": ["Dali", "Picasso", "Da Vinci", "Van Gogh"],
         "c": "Da Vinci",
         "f": "Leonardo Da Vinci pintó la Mona Lisa entre 1503 y 1506."},

        {"p": "¿Cuál es el metal más caro del mundo?",
         "o": ["Oro", "Platino", "Rodio", "Cobre"],
         "c": "Rodio",
         "f": "El rodio es extremadamente raro y se usa en catalizadores y joyería."},

        {"p": "¿Qué middleware permite interactividad en TDA?",
         "o": ["Ginga", "HTML5", "Flash", "JavaFX"],
         "c": "Ginga",
         "f": "Ginga permite aplicaciones interactivas en la TDA."},

        {"p": "¿Qué significa OTT en televisión digital?",
         "o": ["Over The Top", "Open TV Transmission", "Online TV Technology", "Optical Transfer Type"],
         "c": "Over The Top",
         "f": "OTT es contenido transmitido por Internet sin intermediarios tradicionales."},

        {"p": "¿Qué componente es esencial para recibir TDA?",
         "o": ["Decodificador", "Antena satelital", "Router", "Monitor"],
         "c": "Decodificador",
         "f": "El decodificador permite recibir y decodificar la señal de TDA."},

        {"p": "¿En qué año llegó el hombre a la Luna?",
         "o": ["1965", "1972", "1969", "1980"],
         "c": "1969",
         "f": "Neil Armstrong y Buzz Aldrin caminaron en la Luna en 1969."},

        {"p": "¿Cuál es el lenguaje de programación de esta App?",
         "o": ["Java", "C++", "Python", "PHP"],
         "c": "Python",
         "f": "Esta app está desarrollada en Python usando Streamlit."}
    ]
    random.shuffle(st.session_state.pool_preguntas)

# --- 2. ESTADO DEL JUEGO ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.juego_terminado = False
    st.session_state.historial = []

# --- 3. INTERFAZ ---
st.title("📺 ¿Quién quiere ser Ingeniero TDA?")
st.divider()

# Barra de progreso
total_preguntas = 5  # Número de preguntas por ronda
st.progress(st.session_state.indice / total_preguntas)

if not st.session_state.juego_terminado:

    pregunta_actual = st.session_state.pool_preguntas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1}:")
    st.write(f"### {pregunta_actual['p']}")

    opciones = pregunta_actual['o'].copy()
    random.shuffle(opciones)

    # --- FORMULARIO CON RADIO BUTTONS ÚNICOS ---
    with st.form(key=f"form_respuesta_{st.session_state.indice}"):
        seleccion = st.radio(
            "Selecciona tu respuesta:", 
            opciones, 
            key=f"radio_{st.session_state.indice}"  # clave única evita selección automática
        )
        enviar = st.form_submit_button("Confirmar")
        if enviar:
            correcto = seleccion == pregunta_actual['c']
            if correcto:
                st.success(f"¡CORRECTO! 🌟\n{pregunta_actual['f']}")
                st.session_state.puntos += 2
            else:
                st.error(f"INCORRECTO ❌ La respuesta correcta era: {pregunta_actual['c']}\n{pregunta_actual['f']}")

            # Guardar historial
            st.session_state.historial.append({
                "pregunta": pregunta_actual['p'],
                "seleccion": seleccion,
                "correcta": pregunta_actual['c'],
                "correcto": correcto
            })

            # Pasar a la siguiente pregunta
            st.session_state.indice += 1
            if st.session_state.indice >= total_preguntas:
                st.session_state.juego_terminado = True

else:
    st.header("🏁 ¡Fin del Juego!")
    st.metric("PUNTUACIÓN FINAL", f"{st.session_state.puntos} / {total_preguntas*2}")

    if st.session_state.puntos >= 8:
        st.balloons()
        st.success("¡Eres un experto en TDA! 🎓")
    else:
        st.warning("Sigue estudiando la norma ISDB-Tb 📡")

    st.subheader("📋 Resumen de tus respuestas:")
    for h in st.session_state.historial:
        color = "green" if h['correcto'] else "red"
        st.markdown(
            f"- **Pregunta:** {h['pregunta']}\n"
            f"  - **Tu respuesta:** <span style='color:{color}'>{h['seleccion']}</span>\n"
            f"  - **Correcta:** {h['correcta']}",
            unsafe_allow_html=True
        )

    if st.button("Reintentar"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        st.session_state.historial = []
        random.shuffle(st.session_state.pool_preguntas)
