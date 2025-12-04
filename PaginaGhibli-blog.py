# python -m streamlit run PaginaGhibli-blog.py
#  your_script.py

# Primero se importan las librerias que vamos a usar
import matplotlib.pyplot as plt # matplotlib para los gráficos  de barras
import streamlit as st # streamlit para poder sostener la página web en streamlit
import pandas as pd # pandas para cargar, limpiar, transformar y visualizar la tabla de datos de Excel
import random # Para actividades en la sección de curiosidades o más
import numpy as np # numpy para crear y operar estadísticas, usará junto a los gráficos
import matplotlib.patches as mpatches # Para algunos graficos que se se veran en el apartado técnico




# usamos pd. o pandas para cargar la base de datos a usar
df = pd.read_excel("Ghibli-tabla.xlsx") # Renombramos el archivo abierto a "df"


# Para crear páginas, creamos una lista con los nombres que estas tendrán y las guardamos con el nombre paginas
paginas = ["Inicio", "Explora", "Apartado Técnico", "Apartado Artistico", "Curiosidades"]

# Creamos la barra lateral con st.sidebar, y agregamos los botones de navegación con la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# El uso de los condicionales hará que nos muestren la página  
if pagina_seleccionada == "Inicio": # Por ejemplo, la función "if" permite que si escogemos "Inicio" nos encontraremos en la primera página 
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
        clas_pelicula = df.loc[i, "Clasificación"] # Accede al valor de la columna "Clasificación" de la primera fila del dataframe.
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
                    st.markdown(f"Clasificación: {clas_pelicula}") # Mostramos la clasificación de la película seleccionada
                        #st.markdown(f"<a href='{mv_cancion}' target='_blank'><button>🎬 Ver MV</button></a></div>", unsafe_allow_html=True) # Si sí tiene, mostramos el botón para ver el video musical.
                    encontrado = True # Activa la variable booleana para marcar que sí hubo un resultado
    if not encontrado: # Si ninguna canción pasó los filtros de género y duración:
        st.warning("No se encontraron películas de ese género")
elif pagina_seleccionada == "Apartado Técnico":
    st.markdown("<h1 style='text-align: center;'>APARTADO TÉCNICO</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezadp del apartado
    st.markdown("¡Conoce acerca de datos de las películas del estudio! Datos como críticas, premios ganados, nominaciones, presupuestos, recaudaciones, popularidad y más (˶°ㅁ°)!! ")
    st.markdown("---")
    
    #  CONTROL DE SESIÓN 
    if "pelicula_elegida" not in st.session_state:
        st.session_state.pelicula_elegida = None
    #  LISTA DE PELÍCULAS Y PORTADAS 
    lista_peliculas = df["Título"].tolist()

    # Diccionario: { título : url_portada } para que se muestre el título de la película junto con la portada
    portadas1 = { df.loc[i,"Título"]: df.loc[i,"Portada"] for i in range(len(df)) }


    #  SI NO SE HA ELEGIDO PELÍCULA: MOSTRAR MENÚ DE PORTADAS 
    if st.session_state.pelicula_elegida is None:

        st.markdown("<h3 style='text-align: left;'> Selecciona una película para conocer más detalles de esta:</h3>", unsafe_allow_html=True)
        cols = st.columns(4)  # Se mostrará la lista de películas en 4 columnas

        for i, titulo in enumerate(lista_peliculas):
            col = cols[i % 4]

            with col:
                st.image(portadas1[titulo], use_container_width=True)
                if st.button(titulo, key=titulo):
                    st.session_state.pelicula_elegida = titulo
                    st.rerun()

    #  SI YA SE SELECCIONÓ UNA PELÍCULA: Se mostrará la tarjeta técnica 
    else:
        titulo = st.session_state.pelicula_elegida
        datos = df[df["Título"] == titulo].iloc[0]

        st.markdown(f"## 🎬 Detalles técnicos de **{titulo}**")
        col1, col2, col3= st.columns(3)
        
        with col1:
            st.image(datos["Portada"], width=200)

        with col2:
            st.markdown(f"**Dirigido por:** {datos['Director']}")
            st.markdown(f"**Presupuesto:** {datos['Presupuesto']} USD")
            st.markdown(f"**Recaudación Mundial:** {datos['Recaudación_mundial']} USD")
            st.markdown(f"**Fecha de estreno:** {datos['Fecha_estreno']}")
            st.markdown(f"**Tipo de estreno:** {datos['Estreno']}")
            st.markdown(f"**Estudio/s a cargo:** {datos['Estudio']}")
            st.markdown(f"**Distribuido por:** {datos['Distribuidora']}")

        with col3:
            st.markdown(f"**Premios Ganados**")
            st.markdown(f"*{datos['Premios_ganados']}* | {datos['Premios_nom']}")
            st.markdown(f"**Nominaciones**")
            st.markdown(f"*{datos['Nominaciones']}* | {datos['Nomi_nom']}")
            st.markdown(f"**Reseña del público japonés:** {datos['Opinión_Japón']}")
            st.markdown(f"**Puntuación (IMDb):** {datos['Crítica_IMDb']}")

            

        st.markdown("---")
        # BOTÓN PARA VOLVER
        if st.button("Llevame de regreso al menú"):
            st.session_state.pelicula_elegida = None
            st.rerun()

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

    #==============================================
    #       CONTEO DE PREMIOS Y NOMINACIONES
    #==============================================
    # Calcular totales
    total_nominaciones = df["Nominaciones"].sum()
    total_premios = df["Premios_ganados"].sum()
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")"


    # Crear dataframe para graficar
    df_premios = pd.DataFrame({
        "Categoria": ["Nominaciones", "Premios ganados"],
        "Cantidad": [total_nominaciones, total_premios]
    })

    # Gráfico de barras
    st.markdown("## Nominaciones y Premios Totales del Estudio")

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(df_premios["Categoria"], df_premios["Cantidad"], color= "#CEC917")
    ax.set_ylabel("Cantidad Total")
    ax.set_title("Total de Nominaciones y Premios Ganados")

    st.pyplot(fig)

    with st.expander("Ver películas según premios y nominaciones"):

        col1, col2, col3, col4 = st.columns(4)

        # Subconjuntos
        con_premios = df[df["Premios_ganados"] > 0]["Titulo_Año"].tolist()
        sin_premios = df[df["Premios_ganados"] == 0]["Titulo_Año"].tolist()

        con_nominaciones = df[df["Nominaciones"] > 0]["Titulo_Año"].tolist()
        sin_nominaciones = df[df["Nominaciones"] == 0]["Titulo_Año"].tolist()

        #  Columna 1: Con Premios 
        with col1:
            st.markdown("### 🏆 Con Premios")
            if con_premios:
                for t in con_premios:
                    st.markdown(f"- {t}")
            else:
                st.write("Ninguna")

        #  Columna 2: Sin Premios 
        with col2:
            st.markdown("### ❌ Sin Premios")
            if sin_premios:
                for t in sin_premios:
                    st.markdown(f"- {t}")
            else:
                st.write("Ninguna")

        #  Columna 3: Con Nominaciones 
        with col3:
            st.markdown("### 🎬 Con Nominaciones")
            if con_nominaciones:
                for t in con_nominaciones:
                    st.markdown(f"- {t}")
            else:
                st.write("Ninguna")

        #  Columna 4: Sin Nominaciones 
        with col4:
            st.markdown("### ❌ Sin Nominaciones")
            if sin_nominaciones:
                for t in sin_nominaciones:
                    st.markdown(f"- {t}")
            else:
                st.write("Ninguna")


    #  AGRUPACIÓN DE PELÍCULAS POR RANGOS IMDb

    st.markdown("## Agrupación de películas por rangos de puntuación IMDb")

    # Crear los rangos (bins)
    bins = [0, 6, 7, 8, 9, 10]
    labels = ["0–6", "6–7", "7–8", "8–9", "9–10"]

    df["IMDb_rango"] = pd.cut(df["Crítica_IMDb"], bins=bins, labels=labels, include_lowest=True)

    # Contar cuántas películas hay por rango
    tabla_rangos = df.groupby("IMDb_rango")["Título"].count().reset_index()
    tabla_rangos.columns = ["Rango IMDb", "Cantidad de Películas"]
    
    #======================================
    #  GRÁFICO DE BARRAS POR RANGOS IMDb
    # =====================================
    st.markdown("### Gráfico: Cantidad de películas por rango IMDb")

    # Crear figura
    fig, ax = plt.subplots(figsize=(7, 3))

    ax.bar(
        tabla_rangos["Rango IMDb"],
        tabla_rangos["Cantidad de Películas"],
        color="#58A449",   # verde ghibli
        alpha=0.9
    )

        # Etiquetas
    ax.set_xlabel("Rango de Puntuación IMDb")
    ax.set_ylabel("Cantidad de Películas")
    ax.set_title("Distribución de películas según su puntuación IMDb")

        # Mostrar conteo encima de cada barra
    for i, val in enumerate(tabla_rangos["Cantidad de Películas"]):
        ax.text(i, val + 0.1, str(val), ha='center')

    plt.tight_layout()
    st.pyplot(fig)

    # Muestran los títulos dentro de cada rango
    with st.expander("Ver títulos por rango"): # .expander creará una especie de etiqueta desplegable...

        # En la cuál se crean 4 columnas
        col1, col2, col3, col4, col5 = st.columns(5) # Cinco columnas para los cinco rangos de puntuación

        columnas = [col1, col2, col3, col4, col5]    # Se agruparan en forma de lista en 'columnas'

        # Por cada columna, secorre los rangos y se asignan a cada columna
        for col, rango in zip(columnas, labels):
            with col:
                st.markdown(f"### {rango}")          # En cada columna irá el titulo del rango que pertenencen
                subset = df[df["IMDb_rango"] == rango]["Titulo_Año"].tolist()

                if len(subset) > 0:                  # Si la puntuación corresponde a mayor que cero, entonces...
                    for titulo in subset:            # Para cada titulo que encuentren...
                        st.markdown(f"<p style='font-size:14px'>{titulo}</p>", unsafe_allow_html=True) # Se ejecutará el nombre de la película que corresponda en la columna 
                else:                                 # De lo contrario, se ejecutará el mensaje 
                    st.markdown("Sin películas")        # "Sin películas"

elif pagina_seleccionada == "Apartado Artistico":                             # Si el usuario selecciona la opción Apartado Artistico
    st.markdown("<h1 style='text-align: center;'>APARTADO ARTISTICO</h1>", unsafe_allow_html=True) # Agrega otro st. markdown para el encabezado del apartado
    st.markdown("¡Conoce un poco más del arte de las películas del estudio!") # Entonces mostrará un mensaje que le da la bienvenida 
    
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
            st.markdown("### Técnica y Estilo")
            st.markdown(f"**Técnica de animación:** {datos['Técnica_usada']}")
            st.markdown(f"**Paleta de colores:** {datos['Paleta_de_colores']}")
            st.markdown(f"**Estilo visual:** {datos['Estilo_visual']}")
            st.markdown("### Ambientación")
            st.markdown(f"{datos['Ambientación']}")

        with col3:
            
            banda = datos["Banda_sonora"]
            banda_link = datos["Banda_link"]
            link_banda = datos["link_banda_sonora"]

            st.markdown("### Frase conocida")
            st.markdown(f"*{datos['Frase']}*")
            st.markdown("### Banda sonora")
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
    st.markdown("<h1 style='text-align: center;'>CURIOSIDADES Y MÁS</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezado del apartado
    # Escribimos un mensaje de Bienvenida y que explique de que trata el apartado
    st.markdown("""
    <div style='font-size: 20px;'> <p>¡Bienvenido/a a la sección de curiosidades y más!</p>
    <p> Aquí podrás divertirte un rato mientras pones a prueba tu conocimiento acerca de la filmografía de este estudio.</p> 
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")"

    st.markdown("""<h2 div style='text-align: center;'>Datos Curiosos</div></h2>""", unsafe_allow_html=True)
    st.markdown("Dale click al botón de 'Dame un dato curioso' para obtener un dato curioso de alguna película del estudio.")

    if st.button("Dame un dato curioso 🤓"):
        fila = df.sample(1).iloc[0]

        plantillas = [
            f"La película **{fila['Titulo_Año']}** tiene una calificación de **{fila['Crítica_IMDb']} en IMDb**.",
            f"¿Sabías que **{fila['Titulo_Año']}** ganó **{fila['Premios_ganados']} premios**?",
            f"**{fila['Titulo_Año']}** fue nominada a **{fila['Nominaciones']} premios**.",
            f"En Japón, la popularidad de **{fila['Titulo_Año']}** fue considerada **{fila['Popularidad_Japón']}**.",
            f"La recaudación mundial de **{fila['Titulo_Año']}** alcanzó los **${fila['Recaudación_mundial']:,}**.",
            "La película mejor puntuada en IMDb fue: " + df.loc[df["Crítica_IMDb"].idxmax(), "Titulo_Año"],
            "El presupuesto más alto fue de ${:,}.".format(df["Presupuesto"].max()),

        ]

        st.info(random.choice(plantillas))

    st.markdown("---")

    #============================= JUEGO DE ADIVINA LA PELÍCULA POR LA ESCENA
    st.title("🎬 Juego: ¿A qué película pertenece esta imagen?")       # Crea un encabezado nuevo

    # Inicializar variables en session_state
    if "pelicula_objetivo" not in st.session_state:
        st.session_state.pelicula_objetivo = None
    if "intentos" not in st.session_state:
        st.session_state.intentos = 0
    if "juego_terminado" not in st.session_state:
        st.session_state.juego_terminado = False

    #=========================================
    #  GENERAR UNA NUEVA PELÍCULA ALEATORIA 
    #=========================================

    def nueva_ronda():
        st.session_state.pelicula_objetivo = df.sample(1).iloc[0] # df.sample(1) selecciona una película aleatoria del repertorio
        st.session_state.intentos = 0
        st.session_state.juego_terminado = False

    # Si es la primera vez, generar película
    if st.session_state.pelicula_objetivo is None:
        nueva_ronda()


    pelicula = st.session_state.pelicula_objetivo

    # Mostrar la imagen al usuario desde la columna 'Portada'
    st.image(pelicula["foto_escena"], width=300, caption="¿Qué película es?")


    #===========================
    #  SISTEMA DE INTENTOS 
    #===========================
    if not st.session_state.juego_terminado:                               # Se usa st.session para que la película no cambie cada vez que se presione un botón.
        respuesta = st.text_input("Escribe el nombre de la película:")
    
        if st.button("Adivinar"):
            if respuesta.strip().lower() == pelicula["Título"].lower():
                st.success("🎉 ¡Correcto! Has adivinado la película.")
                st.markdown(f"**Descripción de la escena:** {pelicula['Escena_icónica']}")
                st.session_state.juego_terminado = True
            else:
                st.session_state.intentos += 1
                intentos_restantes = 3 - st.session_state.intentos         # Permite tres intentos, al equivocarse resta uno.
            
                if intentos_restantes > 0:
                    st.warning(f"❌ Incorrecto. Te quedan **{intentos_restantes}** intentos.")
                else:
                    st.error("💥 Se acabaron los intentos.")
                    st.info(f"La respuesta correcta era: **{pelicula['Titulo']}**")
                    st.session_state.juego_terminado = True


     #  BOTÓN PARA NUEVA RONDA 
    if st.session_state.juego_terminado:                   # Si l juego ha terminado, 
        if st.button("Jugar otra vez 🔄"):                 # Sera posible que el botón 'Jugar otra vez' aparezca
            nueva_ronda()                                  # Y se inicia una nueva partida

    st.markdown("---")
    # =============================
    #  JUEGO de ADIVINA EL DIRECTOR
    # =============================
    def iniciar_juego(df):
        pelicula = df.sample(1).iloc[0]
        st.session_state["portada"] = pelicula["Portada"]
        st.session_state["director_correcto"] = pelicula["Director"].lower()  # normalización simple
        st.session_state["foto_director"] = pelicula["foto_director"]
        st.session_state["intentos"] = 0
        st.session_state["mensaje"] = ""
        st.session_state["juego_activo"] = True

    # --------------------------
    #        INTERFAZ
    # --------------------------
    st.title("🎬 Adivina el Director")

    # Botón para iniciar el juego
    if st.button("🎲 Nueva película"):
        iniciar_juego(df)

    # Mostrar interfaz solo si hay juego activo
    if st.session_state.get("juego_activo", False):

        st.image(st.session_state["portada"], width=300)
        st.write("¿Quién es el director de esta película?")

        respuesta_2 = st.text_input("Escribe el nombre del director:")

        if st.button("Enviar respuesta"):
            if respuesta_2.strip() == "":
                st.warning("Ingresa un nombre.")
            else:
                st.session_state["intentos"] += 1

                if respuesta_2.lower().strip() == st.session_state["director_correcto"]:
                    st.success("🎉 ¡Correcto!")
                    st.write(f"El director es **{st.session_state['director_correcto'].title()}**")
                    st.image(st.session_state["foto_director"], width=200)
                    st.session_state["juego_activo"] = False

                else:
                    intentos_restantes_2 = 3 - st.session_state["intentos"]

                    if intentos_restantes_2 > 0:
                        st.error(f"❌ Incorrecto. Te quedan {intentos_restantes_2} intentos.")
                    else:
                        st.error("❌ Te quedaste sin intentos.")
                        st.info(f"El director era **{st.session_state['director_correcto'].title()}**")
                        st.image(st.session_state["foto_director"], width=200)
                        st.session_state["juego_activo"] = False