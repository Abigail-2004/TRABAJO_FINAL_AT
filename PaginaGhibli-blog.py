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
import numpy as np
import matplotlib.patches as mpatches # Para algunos graficos que se se veran en el apartado técnico




# usamos pd. para cargar el archivo
df = pd.read_excel("Ghibli-tabla.xlsx")




paginas = ["Inicio", "Explora", "Apartado Técnico", "Apartado Artistico", "Curiosidades"]
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)
# La función "if" permite que si escogemos "Inicio" nos encontraremos en la primera página   
if pagina_seleccionada == "Inicio":
    #st.image("logo.png", width=700)
    # La función st.markdown establece parámetros de texto en Streamlit.
    # Para centrar texto se usa 'text-align: center;'
    st.markdown("<h1 style='text-align: center;'>¡Bienvenido/a al mundo encantado de Studio Ghibli! ✨</h1>", unsafe_allow_html=True)
    
    st.markdown(""" 
    <div style='font-size: 30px;'>
    <p>Este proyecto nace con la intención de reunir, en un solo lugar, la esencia y belleza de las películas del estudio. Aquí podrás descubrir datos, curiosidades y elementos clave que hacen únicas a estas obras.</p>
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
    st.markdown("<h1 style='text-align: center;'>EXPLORA</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezadp del apartado
    st.markdown("""
    <div style='text-align: center; font-size: 20px;'>
    <p>¡Explora a tu criterio El Universo Ghibli! ◝(ᵔᗜᵔ)◜ El estudio cuenta con diversos géneros que pueden ser de tu agrado, o interés.</p>
    """, unsafe_allow_html=True)
    # Prepararemos una búsqueda por filtros
    
    # st.markdown("<h2 style='text-align: center;'>POR GÉNERO</h2>", unsafe_allow_html=True)

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
            generos_encontrados.append(l_genero_depurado) # Se agrega la lista depurada a la lista principal
    
    gen_lista = sorted(set(generos_encontrados)) # Esto evita que los géneros no se repitan: "Set()"
   
    # INTERFAZ DE BÚSQUEDA POR GÉNERO
   
    # Para esto, usaremos la función "st.multiselect" la cuál permite crear menús desplegables o "droop"
    
    generos_seleccionados = st.multiselect(
        "¿Cuáles son los géneros de tu preferencia?:",
        gen_lista,                # De esta lista sacará los generos a mostrarse en el desplegable
        max_selections=2,         # La selección maxima será 2 géneros
        accept_new_options=False  # Desactivamos la opcion de agregar nuevas opciones
    )
    st.markdown(f"Géneros seleccionados: {generos_seleccionados}") # Esto mostrará los géneros que seleccionó el usuario

    # BUSCADOR
    
    encontrado = False   # Verifica si se hallaron resultados o no
    
    for i in range(len(df)):                       # Un bucle que recorre cada fila del DataFrame "range(len(name.xslx))"
        titulo_pelicula = df.loc[i, "Título"]      # Accede al valor de la columna "titulo" en la primera fila o "fila i" del DataFrame.
        portada_pelicula = df.loc[i, "Portada"]    # Accede al link de la imagen de portada correspondiente al nombre "titulo_pelicula" a la fila i.
        generos= df.loc[i, "Género"]               # Accede a los géneros, es el más importante del buscador.
        director_pelicula = df.loc[i, "Director"]  # Accede al valor de la columna "Director" en la primera fila o "fila i" del dataframe
        ano_pelicula = df.loc[i, "Año"]            # Accede al valor de la columna "Año" de la primera fila (fila i) en el Dataframe.
        duracion_pelicula = df.loc[i, "Duración"]  # Accede al valor de la columna "Duración" de la primera fila (fila i) en el dataframe.
        idioma_pelicula = df.loc[i, "Idioma"]      # Aaccede al valor de la columna "Idioma" de la primera fila del dataframe.
    # SISTEMA DE FILTRO
        
        coincide_genero = True # El uso de la variable boleana ayudará a filtrar la película que corresponde con los generos seleccionados por el usuario.
        for genero in generos_seleccionados: # Iteramos por cada género que el usuario haya seleccionado en el filtro de géneros.
            if genero not in str(generos).lower(): # Si ese género seleccionado no está  en los géneros de la canción actual...
                coincide_genero= False # la varible booleana coincide_generos será False
                break # y es bucle se rompe.
        if coincide_genero:  # Si la película sí coincide con los géneros seleccionados entonces se mostrará 
            col1, col2 = st.columns([1, 2])  # Se crean columnas, para mejor orden y visualización de los resultados
            with col1: # En la columna izquierda se muestra la imagen de la portada de la película.
                    st.image(portada_pelicula, width=200)
            with col2: # En la columna derecha se muestra la información como el título, año, director de la película y más
                    st.markdown(f"## {titulo_pelicula} (*{ano_pelicula}*)") # Mostramos el título de la película, con el año entre parentesis y cursiva                   
                    st.markdown(f"Director: {director_pelicula}") # Mostramos el nombre del director de la película
                    st.markdown(f"Duración: {duracion_pelicula} minutos") # Mostramos la duración de la película en minutos
                    st.markdown(f"Idioma: {idioma_pelicula}") # Mostramos el idioma de la película seleccionada
                    #if df_discografia.loc[i, "Video Musical"] == "True": # Verificamos si esa canción tiene video musical ( si la columna "Video Musical" dice "True").
                        #st.markdown(f"<a href='{mv_cancion}' target='_blank'><button>🎬 Ver MV</button></a></div>", unsafe_allow_html=True) # Si sí tiene, mostramos el botón para ver el video musical.
                    encontrado = True # Activa la variable booleana para marcar que sí hubo un resultado
    if not encontrado: # Si ninguna canción pasó los filtros de género y duración:
        st.warning("No se encontraron películas de ese género")
elif pagina_seleccionada == "Apartado Técnico":
    st.markdown("<h1 style='text-align: center;'>APARTADO TÉCNICO</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezadp del apartado
    st.markdown("¡Conoce acerca de datos de las películas del estudio! Datos como críticas, premios ganados, nominaciones, presupuestos, recaudaciones, popularidad y más (˶°ㅁ°)!! ")
    st.markdown("---")
    st.markdown("## Tabla general de Presupuesto vs Recaudación mundial por película")

    #  LIMPIEZA DE DATOS 
    # Se convierten los valores eliminando símbolos y comas
    df["Presupuesto"] = (
        df["Presupuesto"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    df["Recaudación_mundial"] = (
        df["Recaudación_mundial"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    df_sorted = df.sort_values("Recaudación_mundial", ascending=False)

    #  GRÁFICO DE PRESUPUESTO Y RECAUDACIÓN MUNDIAL
    fig, ax = plt.subplots(figsize=(10, 7))
    y = df_sorted["Título"]
    presupuesto = df_sorted["Presupuesto"]
    recaudacion = df_sorted["Recaudación_mundial"]

    y_pos = np.arange(len(y))
    height = 0.35  # separación entre barras

    # Barras horizontales lado a lado
    ax.barh(y_pos - height/2, presupuesto, height=height, label="Presupuesto", alpha=0.7, color="#CEC917")
    ax.barh(y_pos + height/2, recaudacion, height=height, label="Recaudación", alpha=0.7, color="#58A449")

    # Estética
    ax.set_yticks(y_pos)
    ax.set_yticklabels(y, fontsize=9)
    ax.set_xlabel("Monto (USD)")
    ax.set_title("Presupuesto vs Recaudación – Studio Ghibli")
    ax.legend()

    plt.tight_layout()
    st.pyplot(fig)

    #  SECCIÓN DE COMPARACIÓN DE PRESUPUESTO Y RECAUDACIÓN 
    
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")"
    
    st.markdown("## Comparación de Presupuesto y Recaudación entre Películas")

    # Selección de dos películas
    peliculas = df["Titulo_Año"].unique()

    seleccion = st.multiselect(
        "Selecciona dos películas:",
        peliculas,
        max_selections=2,
        key="presupuesto_comp"
    )

    if len(seleccion) != 2:
        st.info("Selecciona exactamente **dos** películas para comparar.")
    else:

    # Recuperar los títulos limpios sin año
        peli1_titulo = seleccion[0].split(" (")[0]
        peli2_titulo = seleccion[1].split(" (")[0]

        # Filtrar dataframe
        df_comp = df[df["Título"].isin([peli1_titulo, peli2_titulo])]

        # Obtener valores
        pelis_con_ano = df_comp["Titulo_Año"].tolist()
        presupuesto = df_comp["Presupuesto"].tolist()
        recaudacion = df_comp["Recaudación_mundial"].tolist()

        # Crear gráfico horizontal como el general
        fig, ax = plt.subplots(figsize=(8, 5))

        y_pos = np.arange(len(pelis_con_ano))
        height = 0.35

        ax.barh(y_pos - height/2, presupuesto, height=height, label="Presupuesto", alpha=0.7, color="#CEC917")
        ax.barh(y_pos + height/2, recaudacion, height=height, label="Recaudación", alpha=0.7, color="#58A449")

        # Etiquetas y estética
        ax.set_yticks(y_pos)
        ax.set_yticklabels(pelis_con_ano, fontsize=10)
        ax.set_xlabel("Monto (USD)")
        ax.set_title("Comparación de Presupuesto y Recaudación")
        ax.legend()

        plt.tight_layout()
        st.pyplot(fig)

        # Mostrar valores numéricos (opcional)
        colA, colB = st.columns(2)

        with colA:
            st.write(f"### {pelis_con_ano[0]}")
            st.write(f"**Presupuesto:** ${presupuesto[0]:,}")
            st.write(f"**Recaudación:** ${recaudacion[0]:,}")

        with colB:
            st.write(f"### {pelis_con_ano[1]}")
            st.write(f"**Presupuesto:** ${presupuesto[1]:,}")
            st.write(f"**Recaudación:** ${recaudacion[1]:,}")


    st.markdown("---")

    # GRÁFICO DE FECHAS DE ESTRENO
    st.markdown("## Línea de tiempo cronológica de fechas de estreno de películas Ghibli")
    # Conversión de fechas
    df["Fecha_estreno"] = pd.to_datetime(df["Fecha_estreno"], errors="coerce")

    # Función para asignar colores según tipo de estreno
    def asignar_color(estreno):
        estreno = str(estreno)
        if "Festival" in estreno:
            return "#CEC917"
        elif "Streaming" in estreno:
            return "#58A449"
        elif "Internacional" in estreno:
            return "#2C715F"
        else:
            return "gray"

    df["Color"] = df["Estreno"].apply(asignar_color)

    # Ordenar por fecha de estreno
    df = df.sort_values("Fecha_estreno").reset_index(drop=True)

    # --- Crear el gráfico ---
    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot: fecha en x, índice en y
    ax.scatter(df["Fecha_estreno"], df.index, s=120, c=df["Color"])

    # Etiquetas en eje y con los títulos
    ax.set_yticks(df.index)
    ax.set_yticklabels(df["Título"], fontsize=9)

    # Mejoras visuales
    ax.set_xlabel("Fecha de Estreno")
    ax.set_title("Timeline cronológico de estrenos - Studio Ghibli")
    ax.grid(axis="x", linestyle="--", alpha=0.4)

    legend_patches = [
        mpatches.Patch(color="#2C715F", label="Internacional"),
        mpatches.Patch(color="#58A449", label="Streaming"),
        mpatches.Patch(color="#CEC917", label="Festival"),
        mpatches.Patch(color="gray", label="Otro / No clasificado")
    ]

    ax.legend(handles=legend_patches, title="Tipo de estreno", loc="upper left")

    plt.tight_layout()
    # Mostrar en Streamlit
    st.pyplot(fig)

    st.markdown("---")

    # HERRAMIENTA DE COMPARACIÓN DE PREMIOS Y NOMINACIONES
    # Crearemos una herramienta en la cuál el usuario podrá elegir dos películas y comparar el número de premios y nominaciones que ambas obtuvieron.
    st.markdown("## Comparación de Premios y Nominaciones por cada película")
    st.markdown("""
    ¿Deseas saber cuántos premios y/o nominaciones obtuvo una película? Selecciona dos películas al azar y obtén los resultados de cada una.
                """)
    
    peliculas = df["Titulo_Año"].unique()

    # SELECCIÓN MÚLTIPLE 
    seleccion = st.multiselect(
        "Selecciona dos películas:",
        peliculas,
        max_selections=2
    )

    # Si no hay exactamente dos, no continuar
    if len(seleccion) != 2:
        st.info("Por favor selecciona **exactamente dos** películas para realizar la comparación.")
    else:

        peli1, peli2 = seleccion

        # EXTRAER SOLO EL TÍTULO REAL (sin el año)
        titulo1 = peli1.split(" (")[0]
        titulo2 = peli2.split(" (")[0]

        # EXTRAER LA FILA CORRECTA DEL DATAFRAME
        data1 = df[df["Título"] == titulo1].iloc[0]
        data2 = df[df["Título"] == titulo2].iloc[0]

        # MOSTRAR LAS DOS PELÍCULAS LADO A LADO
        col1, col2 = st.columns(2)

        with col1:
            st.header(peli1)
            st.image(data1["Portada"], width=250)
            st.markdown(f"**Premios ganados:** {data1['Premios_ganados']}")
            st.markdown(f"**Nominaciones:** {data1['Nominaciones']}")

        with col2:
            st.header(peli2)
            st.image(data2["Portada"], width=250)
            st.markdown(f"**Premios ganados:** {data2['Premios_ganados']}")
            st.markdown(f"**Nominaciones:** {data2['Nominaciones']}")

        # GRÁFICO COMPARATIVO
        fig, ax = plt.subplots(figsize=(7, 4))

        ax.bar(
            [peli1, peli2],
            [data1["Premios_ganados"], data2["Premios_ganados"]],
            label="Premios ganados",
            color="#CEC917"
        )
        ax.bar(
            [peli1, peli2],
            [data1["Nominaciones"], data2["Nominaciones"]],
            bottom=[data1["Premios_ganados"], data2["Premios_ganados"]],
            label="Nominaciones",
            color="#58A449"
        )

        ax.set_ylabel("Cantidad total")
        ax.set_title("Comparación de Premios y Nominaciones")
        ax.legend()

        st.pyplot(fig)

        # DETALLE DE PREMIOS Y NOMINACIONES
        st.subheader("Detalle de Premios y Nominaciones")

        colL, colR = st.columns(2)

        with colL:
            st.write(f"### {peli1}")
            st.write("**Premios:**")
            if data1["Premios_nom"]:
                for p in data1["Premios_nom"].split(","):
                    st.write("- " + p.strip())
            else:
                st.write("No disponible")

            st.write("**Nominaciones:**")
            if data1["Nomi_nom"]:
                for n in data1["Nomi_nom"].split(","):
                    st.write("- " + n.strip())
            else:
                st.write("No disponible")

        with colR:
            st.write(f"### {peli2}")
            st.write("**Premios:**")
            if data2["Premios_nom"]:
                for p in data2["Premios_nom"].split(","):
                    st.write("- " + p.strip())
            else:
                st.write("No disponible")

            st.write("**Nominaciones:**")
            if data2["Nomi_nom"]:
                for n in data2["Nomi_nom"].split(","):
                    st.write("- " + n.strip())
            else:
                st.write("No disponible")

elif pagina_seleccionada == "Apartado Artistico":                             # Si el usuario selecciona la opción Apartado Artistico
    st.markdown("<h1 style='text-align: center;'>APARTADO ARTISTICO</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezado del apartado
    st.markdown("¡Conoce un poco más del arte de las películas del estudio!") # Entonces mostrará un mensaje que le da la bienvenida 
    
    #for i in range(len(df)): # Un bucle que recorre cada fila del DataFrame "range(len(name.xslx))"
        #titulo_pelicula = df.loc[i, "Título"] # Accede al valor de la columna "titulo" en la primera fila o "fila i" del DataFrame.
        #portada_pelicula = df.loc[i, "Portada"] # Accede al link de la imagen de portada correspondiente al nombre "titulo_pelicula" a la fila i.
        #tecnica_art = df.loc[i, "Técnica_usada"]
        #paleta_art = df.loc[i, "Paleta_de_colores"] 
        #estilo_art =df.loc[i, "Estilo_visual"]
        #ambientacion_art = df.loc[i, "Ambientación"]
        #with st.expander(f"🎨 Análisis artístico de {titulo_pelicula}"):
            #st.markdown(f"**Técnica de animación:** {tecnica_art}")
            #st.markdown(f"**Paleta de colores:** {paleta_art}")
            #st.markdown(f"**Estilo visual:** {estilo_art}")
            #st.markdown(f"**Ambientación:** {ambientacion_art}")
    #  CONTROL DE SESIÓN 
    if "pelicula_elegida" not in st.session_state:
        st.session_state.pelicula_elegida = None
    #  LISTA DE PELÍCULAS Y PORTADAS 
    lista_peliculas = df["Título"].tolist()

    # Diccionario: { título : url_portada } para que se muestre el título de la película junto con la portada
    portadas = { df.loc[i,"Título"]: df.loc[i,"Portada"] for i in range(len(df)) }


    #  SI NO SE HA ELEGIDO PELÍCULA: MOSTRAR MENÚ DE PORTADAS 
    if st.session_state.pelicula_elegida is None:

        st.markdown("<h3 style='text-align: left;'> 🎨 Selecciona una película para ver su análisis artístico:</h3>", unsafe_allow_html=True)
        cols = st.columns(4)  # Se mostrará la lista de películas en 4 columnas

        for i, titulo in enumerate(lista_peliculas):
            col = cols[i % 4]

            with col:
                st.image(portadas[titulo], use_container_width=True)
                if st.button(titulo, key=titulo):
                    st.session_state.pelicula_elegida = titulo
                    st.rerun()

    #  SI YA SE SELECCIONÓ UNA PELÍCULA: Se mostrará la tarjeta artistica 
    else:
        titulo = st.session_state.pelicula_elegida
        datos = df[df["Título"] == titulo].iloc[0]

        st.markdown(f"## 🎬 Análisis artístico de **{titulo}**")
        col1, col2, col3= st.columns(3)
        
        with col1:
            st.image(datos["Portada"], width=200)

        with col2:
            st.markdown("### 🎨 Técnica y Estilo")
            st.markdown(f"**Técnica de animación:** {datos['Técnica_usada']}")
            st.markdown(f"**Paleta de colores:** {datos['Paleta_de_colores']}")
            st.markdown(f"**Estilo visual:** {datos['Estilo_visual']}")
            st.markdown("### 🌄 Ambientación")
            st.markdown(f"{datos['Ambientación']}")

        with col3:
            
            banda = datos["Banda_sonora"]
            banda_link = datos["Banda_link"]
            link_banda = datos["link_banda_sonora"]

            st.markdown("### 🎼 Banda sonora")
            st.markdown(f"**Compositor:** {banda}")

            if str(banda_link).lower() == "true" and pd.notna(link_banda):
                st.markdown(f"[🎵 Escuchar banda sonora]({link_banda})")
            else:
                st.markdown("_No disponible en línea_")

        st.markdown("---")
        # BOTÓN PARA VOLVER
        if st.button("Llevame de regreso al menú"):
            st.session_state.pelicula_elegida = None
            st.rerun()
    st.markdown("---")
    
    #Ahora, prepararemos gráficos de frecuencias con variables como paleta de colores, tecnicas usadas, tipo de animación y ambientación
    #  PREPARACIÓN DE DATOS (FRECUENCIA DE PALETAS)
    # Se convierte todas las paletas a lista y se limpian
    lista_colores = []

    for paleta in df["Paleta_de_colores"]:
        if pd.notna(paleta):
            colores = [c.strip().lower() for c in paleta.split(",")]
            lista_colores.extend(colores)

    # Se cuenta la frecuencia de colores con counts()
    conteo_colores = pd.Series(lista_colores).value_counts()

    #  GRÁFICO (FRECUENCIA DE PALETAS)
    st.markdown("## Frecuencia de colores más usados en las películas de Studio Ghibli")

    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(conteo_colores.index, conteo_colores.values, color="#2C715F")
    ax.set_xlabel("Colores y Tonos")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Comparativa de paletas de color en Studio Ghibli")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    # GRÁFICO DE TIPO DE ANIMACIÓN

    st.markdown("## Tipo de animación más usado en las películas de Studio Ghibli")

    conteo_animacion = df["Tipo_de_animación"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(
        conteo_animacion.index,
        conteo_animacion.values,
        color="#2C715F"
    )

    ax.set_xlabel("Tipo de animación")
    ax.set_ylabel("Cantidad de películas")
    ax.set_title("Distribución de tipos de animación en Studio Ghibli")
    plt.xticks(rotation=360)

    st.pyplot(fig)

    #GRÁFICOS DE TÉCNICA USADAS

    st.markdown("## Técnicas más usadas en las películas de Studio Ghibli")

    conteo_tecnica = df["Técnica_usada"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(
        conteo_tecnica.index,
        conteo_tecnica.values,
        color="#2C715F"
    )

    ax.set_xlabel("Técnica de animación")
    ax.set_ylabel("Cantidad de películas")
    ax.set_title("Frecuencia de técnicas utilizadas")
    plt.xticks(rotation=45)

    st.pyplot(fig)

    # GRÁFICOS DE ESTILO VISUAL

    st.markdown("## Frecuencia de estilo visual en las películas de Studio Ghibli")

    estilos_expandidos = (
    df["Estilo_visual"]
    .str.lower()               # Convierte todo a minusculas
    .str.split(",")            # separa por coma
    .explode()                 # crea una fila por cada estilo
    .str.strip()               # elimina espacios
    )
    conteo_estilo = estilos_expandidos.value_counts()

    plt.figure(figsize=(10,6))
    conteo_estilo.plot(kind="bar", color="#2C715F")   # color personalizado
    plt.title("Frecuencia de estilos visuales en Studio Ghibli")
    plt.xlabel("Estilo visual")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(plt)
else:
    st.markdown("Contenido")
