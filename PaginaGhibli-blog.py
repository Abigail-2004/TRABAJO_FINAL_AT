#Primero ejecutamos la página
# Para eso creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PaginaGhibli-blog.py
#  your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import matplotlib.pyplot as plt
import streamlit as st 
import pandas as pd
import random # Para el boton musical que crearemos a continuacion




# usamos pd. para cargar el archivo
df = pd.read_excel("Ghibli-tabla.xlsx")




paginas = ["Inicio", "Explora", "Alcance", "Géneros", "Curiosidades"]
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)
# La función "if" permite que si escogemos "Inicio" nos encontraremos en la primera página   
if pagina_seleccionada == "Inicio":
    #st.image("logo.png", width=700)
    # La función st.markdown permite establecer ciertos parámetros en texto sen Streamlit
    #st.markdown("<h1 style='text-align: center;'><em>ANATOMÍA DE UN ÍCONO:</em><br>Explorando la discografía de <br><span style='color: #d8a7b1;'>Taylor Swift</span></h1>", unsafe_allow_html=True)
    #
    st.markdown(""" 
    <div style='font-size: 30px;'>
    <p>¡Bienvenido/a al mundo encantado de Studio Ghibli! ✨ Este proyecto nace con la intención de reunir, en un solo lugar, la esencia y belleza de las películas del estudio. Aquí podrás descubrir datos, curiosidades y elementos clave que hacen únicas a estas obras.</p>
    <p> </p>
    <p>Nuestro objetivo es ofrecerte un espacio entretenido, informativo y fácil de navegar, para que puedas explorar, aprender y maravillarte con la magia que Ghibli ha compartido con el mundo.
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3) #Usamos esta función para centrar la imagen que deseamos usar, verse más ordenado
    with col1: #Esto se usa para agregar contenido a una columna
        st.write(" ") #Aquí se escribe el contenido que quieres introducir en la columna
    with col2:
    #Con esta función, introducimos una imagen para rellenar el espacio
        st.image('https://i.pinimg.com/originals/8c/ac/ec/8cacec3c6545e952341c2a5b90f047b0.gif')
    with col3:
        st.write(" ")
elif pagina_seleccionada == "Explora":
    st.markdown("<h1 style='text-align: center;'><em>EXPLORA</em></h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezadp del apartado
    st.markdown("""
    <div style='text-align: center; font-size: 20px;'>
    <p>¡Explora a tu criterio El Universo Ghibli!</p>
    """, unsafe_allow_html=True)
    # Prepararemos una búsqueda por filtros
    st.markdown("<h2 style='text-align: center;'>POR GÉNERO</h2>", unsafe_allow_html=True)

    # BÚSQUEDA POR GÉNERO

    #Para esto, crearemos una lista con los géneros que hay en las películas del estudio
    generos_encontrados= [] # Se crea una lista vacia que almacenará los generos
    # Se usarán los bucles "for" y ".iterrows()" para recorrer todas las filas del dataframe
    for i, fila in df.iterrows():
        t_genero = str(fila["Género"])  # Obtenemos todo el contenido de la columna "Genero" como un texto y lo guardamos en la variable texto_genero
        l_genero = t_genero.split(",")  # "split()" Separa el texto al encontrar una coma, eso facilitará el recorrido
    # Se crea un bucle "for" esto para quitar espacios de cada fila de genero y depurar la lista
        for genero in l_genero:
            l_genero_depurado = genero.strip().lower()
            generos_encontrados.append(l_genero_depurado) # Se agrega la lusta depurada a la lista principal
    gen_lista = sorted(set(generos_encontrados)) # Esto evita que los géneros no se repitan: "Set()"
   
    # INTERFAZ DE BÚSQUEDA POR GÉNERO
   
    # Para esto, usaremos la función "st.multiselect" la cuál permite crear menús desplegables o "droop"
    generos_seleccionados = st.multiselect(
            "",
            gen_lista,  # De esta lista sacará los generos a mostrarse en el desplegable
            max_selections=2, # La selección maxima será 2 géneros
            accept_new_options=False  # Desactivamos la opcion de agregar nuevas opciones
        )
    st.markdown(f"Géneros seleccionados: {generos_seleccionados}") # Esto mostrará los géneros que seleccionó el usuario

    # BUSCADOR
    encontrado = False   # Verifica si se hallaron resultados o no
    
elif pagina_seleccionada == "Alcance":
    st.markdown("Contenido")
elif pagina_seleccionada == "Géneros":
    st.markdown("Espacio")
else:
    st.markdown("Contenido")
