import streamlit as st
import streamlit.components.v1 as components
import random
import time

st.set_page_config(page_title="Trivia OTT", page_icon="🎡")

# -------------------------------------------------
# PREGUNTAS (10 POR CATEGORIA)
# -------------------------------------------------

preguntas = {

"Cultura":[
{"p":"Capital de Venezuela","o":["Caracas","Maracaibo","Valencia","Coro"],"c":"Caracas"},
{"p":"Autor Mona Lisa","o":["Da Vinci","Picasso","Dali","Van Gogh"],"c":"Da Vinci"},
{"p":"Pais tango","o":["Argentina","Chile","Mexico","España"],"c":"Argentina"},
{"p":"Idioma mas hablado","o":["Chino","Ingles","Español","Arabe"],"c":"Chino"},
{"p":"Ciudad luz","o":["Paris","Roma","Madrid","Londres"],"c":"Paris"},
{"p":"Pirámides famosas","o":["Egipto","Mexico","Peru","India"],"c":"Egipto"},
{"p":"Autor Quijote","o":["Cervantes","Borges","Lorca","Neruda"],"c":"Cervantes"},
{"p":"Continente mayor","o":["Asia","Africa","Europa","America"],"c":"Asia"},
{"p":"Moneda Japon","o":["Yen","Won","Yuan","Peso"],"c":"Yen"},
{"p":"Rio mas largo","o":["Amazonas","Nilo","Yangtse","Misisipi"],"c":"Amazonas"}
],

"Tecnologia":[
{"p":"Bits en un byte","o":["8","16","4","32"],"c":"8"},
{"p":"Mascota Linux","o":["Pinguino","Gato","Perro","Elefante"],"c":"Pinguino"},
{"p":"Lenguaje app","o":["Python","Java","C++","PHP"],"c":"Python"},
{"p":"Empresa Windows","o":["Microsoft","Apple","IBM","Google"],"c":"Microsoft"},
{"p":"Creador Linux","o":["Torvalds","Jobs","Gates","Page"],"c":"Torvalds"},
{"p":"Sistema Google","o":["Android","iOS","Windows","Symbian"],"c":"Android"},
{"p":"Memoria rápida","o":["Cache","RAM","SSD","ROM"],"c":"Cache"},
{"p":"Protocolo Internet","o":["TCP/IP","HTTP","FTP","SMTP"],"c":"TCP/IP"},
{"p":"Lenguaje web","o":["HTML","C","Java","Python"],"c":"HTML"},
{"p":"Unidad digital","o":["Byte","Volt","Ampere","Hertz"],"c":"Byte"}
],

"TDA":[
{"p":"Norma TDA Venezuela","o":["ISDB-Tb","ATSC","DVB","PAL"],"c":"ISDB-Tb"},
{"p":"Middleware interactivo","o":["Ginga","Flash","Java","HTML"],"c":"Ginga"},
{"p":"OTT significa","o":["Over The Top","Online TV","Open Transfer","Optic TV"],"c":"Over The Top"},
{"p":"Tipo transmisión","o":["RF","FM","AM","Bluetooth"],"c":"RF"},
{"p":"Compresión video","o":["MPEG","PNG","GIF","TXT"],"c":"MPEG"},
{"p":"Resolución HD","o":["1280x720","640x480","320x240","800x600"],"c":"1280x720"},
{"p":"Audio digital","o":["MP3","DOC","ZIP","TXT"],"c":"MP3"},
{"p":"Frecuencia VHF","o":["30-300MHz","1GHz","5GHz","10MHz"],"c":"30-300MHz"},
{"p":"Frecuencia UHF","o":["300MHz-3GHz","10MHz","5GHz","1MHz"],"c":"300MHz-3GHz"},
{"p":"TV digital usa","o":["Bits","Voltios","Ondas AM","Ondas FM"],"c":"Bits"}
],

"Ciencia":[
{"p":"Planeta rojo","o":["Marte","Venus","Jupiter","Saturno"],"c":"Marte"},
{"p":"Año llegada luna","o":["1969","1972","1965","1980"],"c":"1969"},
{"p":"Elemento O","o":["Oxigeno","Oro","Osmio","Hierro"],"c":"Oxigeno"},
{"p":"Velocidad luz","o":["300000km/s","1000","5000","100"],"c":"300000km/s"},
{"p":"Planeta grande","o":["Jupiter","Saturno","Neptuno","Tierra"],"c":"Jupiter"},
{"p":"Ley gravedad","o":["Newton","Tesla","Einstein","Curie"],"c":"Newton"},
{"p":"Centro atomo","o":["Nucleo","Electron","Proton","Neutron"],"c":"Nucleo"},
{"p":"Gas respiramos","o":["Oxigeno","Helio","CO2","Hidrogeno"],"c":"Oxigeno"},
{"p":"Planetas sistema solar","o":["8","9","7","10"],"c":"8"},
{"p":"Mas cercano sol","o":["Mercurio","Venus","Tierra","Marte"],"c":"Mercurio"}
],

"Videojuegos":[
{"p":"Consola mas vendida","o":["PS2","Xbox360","Switch","PS4"],"c":"PS2"},
{"p":"Protagonista Zelda","o":["Link","Mario","Zelda","Ganon"],"c":"Link"},
{"p":"Empresa Mario","o":["Nintendo","Sony","Microsoft","Sega"],"c":"Nintendo"},
{"p":"Juego mas vendido","o":["Minecraft","GTA","Mario","Tetris"],"c":"Minecraft"},
{"p":"Personaje Sega","o":["Sonic","Tails","Shadow","Knuckles"],"c":"Sonic"},
{"p":"Battle royale","o":["Fortnite","Halo","Doom","Portal"],"c":"Fortnite"},
{"p":"Juego Kratos","o":["God of War","Halo","Zelda","Metroid"],"c":"God of War"},
{"p":"Juego bloques","o":["Minecraft","Roblox","Terraria","Tetris"],"c":"Minecraft"},
{"p":"Consola Sony","o":["PlayStation","Xbox","Switch","GameCube"],"c":"PlayStation"},
{"p":"Mascota Nintendo","o":["Mario","Luigi","Peach","Toad"],"c":"Mario"}
]

}

categorias=list(preguntas.keys())

# -------------------------------------------------
# ESTADOS
# -------------------------------------------------

if "fase" not in st.session_state:
    st.session_state.fase="ruleta"

if "tema" not in st.session_state:
    st.session_state.tema=None

if "indice" not in st.session_state:
    st.session_state.indice=0

if "puntos" not in st.session_state:
    st.session_state.puntos=0

# -------------------------------------------------
# RULETA CASINO
# -------------------------------------------------

def ruleta_casino():

    html="""
    <style>

    .container{
        text-align:center;
    }

    .wheel{
        width:400px;
        height:400px;
        border-radius:50%;
        border:8px solid black;
        margin:auto;
        background:
        conic-gradient(
        red 0deg 72deg,
        blue 72deg 144deg,
        green 144deg 216deg,
        yellow 216deg 288deg,
        purple 288deg 360deg);
        transition: transform 4s cubic-bezier(.17,.67,.83,.67);
    }

    .pointer{
        width:0;
        height:0;
        border-left:20px solid transparent;
        border-right:20px solid transparent;
        border-bottom:40px solid black;
        margin:auto;
    }

    </style>

    <div class="container">

    <div class="pointer"></div>
    <div id="wheel" class="wheel"></div>

    <script>

    function spin(){

    var wheel=document.getElementById("wheel")

    var deg=3600+Math.random()*360

    wheel.style.transform="rotate("+deg+"deg)"

    }

    </script>

    </div>
    """

    components.html(html,height=450)

# -------------------------------------------------
# PANTALLA RULETA
# -------------------------------------------------

if st.session_state.fase=="ruleta":

    st.title("🎡 RULETA DE CATEGORÍAS")

    ruleta_casino()

    if st.button("GIRAR RULETA"):

        tema=random.choice(categorias)

        st.session_state.tema=tema

        random.shuffle(preguntas[tema])

        st.session_state.fase="juego"

        st.rerun()

# -------------------------------------------------
# JUEGO
# -------------------------------------------------

elif st.session_state.fase=="juego":

    st.title("🧠 Trivia")

    st.write("Categoría:",st.session_state.tema)

    pregunta=preguntas[st.session_state.tema][st.session_state.indice]

    st.subheader(pregunta["p"])

    for op in pregunta["o"]:

        if st.button(op):

            if op==pregunta["c"]:
                st.success("Correcto")
                st.session_state.puntos+=1
            else:
                st.error("Incorrecto")

            time.sleep(1)

            st.session_state.indice+=1

            if st.session_state.indice>=10:
                st.session_state.fase="final"

            st.rerun()

# -------------------------------------------------
# FINAL
# -------------------------------------------------

elif st.session_state.fase=="final":

    st.title("🏁 Fin del juego")

    st.metric("Puntuación",st.session_state.puntos)

    if st.button("Jugar otra vez"):

        st.session_state.fase="ruleta"
        st.session_state.tema=None
        st.session_state.indice=0
        st.session_state.puntos=0

        st.rerun()
