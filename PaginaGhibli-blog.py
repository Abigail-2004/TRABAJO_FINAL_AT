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
    for i in range(len(df)): # Un bucle que recorre cada fila del DataFrame "range(len(name.xslx))"
        titulo_pelicula = df.loc[i, "Título"] # Accede al valor de la columna "titulo" en la primera fila o "fila i" del DataFrame.
        portada_pelicula = df.loc[i, "Portada"] # Accede al link de la imagen de portada correspondiente al nombre "titulo_pelicula" a la fila i.
        generos= df.loc[i, "Género"] # Accede a los géneros, es el más importante del buscador.
        col1,col2 = st.columns([1, 2])
        with col1: st.markdown(f"""
                <h4><i><b>{titulo_pelicula}</b></i></h4>
                <ul>
                    <li>Género: {generos}</li>
                </ul>
                """, unsafe_allow_html=True)
        with col2: st.image(portada_pelicula, width=200)
    # SISTEMA DE FILTRO
    coincide_genero= True # El uso de la variable boleana ayudará a filtrar la película que corresponde con los generos seleccionados por el usuario.
    for genero in generos_seleccionados: # Iteramos por cada género que el usuario haya seleccionado en el filtro de géneros.
        if genero not in str(generos).lower(): # Si ese género seleccionado no está  en los géneros de la canción actual...
            coincide_genero= False # la varible booleana coincide_generos será False
            break # y es bucle se rompe.
        if coincide_genero:  # Si la canción sí coincide con los géneros seleccionados…
            st.markdown(f"## {titulo_pelicula}") # Mostramos el título de la canción en formato grande (##).
            st.markdown(f"Álbum: *{album_cancion}* ({año_cancion})") # Mostramos el nombre del álbum en cursiva y el año entre paréntesis.
                col1, col2 = st.columns([1, 2])  # Creamos dos columnas: la primera más pequeña para la portada y la segunda más grande para los botones de enlaces.
                with col1: # En la columna izquierda mostramos la imagen de la canción. Se fija el ancho a 300 píxeles.
                    st.image(portada_pelicula, width=300)
                with col2: # En la otra columna...
                    st.markdown(f"<a href='{link_spotify}' target='_blank'><button>🎧 Escuchar en Spotify</button></a>", unsafe_allow_html=True) # Se crea un botón HTML que lleva al link de Spotify en una nueva pestaña.                    
                    st.markdown(f"<a href='{letras_cancion}' target='_blank'><button>📜 Ver Letra</button></a>", unsafe_allow_html=True) # Botón que abre la página con la letra de la canción.
                    if df_discografia.loc[i, "Video Musical"] == "True": # Verificamos si esa canción tiene video musical ( si la columna "Video Musical" dice "True").
                        st.markdown(f"<a href='{mv_cancion}' target='_blank'><button>🎬 Ver MV</button></a></div>", unsafe_allow_html=True) # Si sí tiene, mostramos el botón para ver el video musical.
                    encontrado = True # Activa la variable booleana para marcar que sí hubo un resultado
    
elif pagina_seleccionada == "Alcance":
    st.markdown("Contenido")
elif pagina_seleccionada == "Géneros":
    st.markdown("Espacio")
else:
    st.markdown("Contenido")
