# python -m streamlit run PaginaGhibli-blog.py
#  your_script.py

# Primero se importan las librerias que vamos a usar
import matplotlib.pyplot as plt # matplotlib para los gráficos  de barras
import streamlit as st # streamlit para poder sostener la página web en streamlit
import pandas as pd # pandas para cargar, limpiar, transformar y visualizar la tabla de datos de Excel
import random # Para actividades en la sección de curiosidades o más
import numpy as np # numpy para crear y operar estadísticas, usará junto a los gráficos
import matplotlib.patches as mpatches # Para los rotulos de algunos graficos que se se veran en el apartado técnico
from wordcloud import WordCloud



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
    # Para centrar texto se usa 'text-align: center;' h1 es uno de los títulos más grandes que streamlit permite, unsafe_allow_html=True permite el uso de HTML y estilos CSS en streamlit.
    st.markdown("<h1 style='text-align: center;'>¡Bienvenido/a al mundo encantado de Studio Ghibli! ✨</h1>", unsafe_allow_html=True)
    
    st.markdown(""" 
    <div style='font-size: 30px;'>
    <p>Este proyecto nace con la intención de reunir, en un solo lugar, la esencia y belleza de las películas del estudio. Aquí podrás descubrir datos, curiosidades y elementos clave que hacen únicas a estas obras.</p>
    <p> </p>
    <p>Nuestro objetivo es ofrecerte un espacio entretenido, informativo y fácil de navegar, para que puedas explorar, aprender y maravillarte con la magia que Ghibli ha compartido con el mundo.
    </div>
    """, unsafe_allow_html=True) # Escribimos un texto de bienvenida, y una breve explicación de la página.
    col1, col2, col3 = st.columns(3) #Usamos esta función para crear columnas, de esta manera  la imagen que deseamos usar, verse más ordenado
    with col1: #Esto se usa para agregar contenido a una columna
        st.write(" ") #Aquí se escribe el contenido que quieres introducir en la columna
    with col2:
    #Con esta función, introducimos una imagen para rellenar el espacio
        st.image('https://i.pinimg.com/originals/8c/ac/ec/8cacec3c6545e952341c2a5b90f047b0.gif')
    with col3:
        st.write(" ")
elif pagina_seleccionada == "Explora": # Si escogemos "Explora" de los botones de navegación, nos encontraremos en la segunda página
    st.markdown("<h1 style='text-align: center;'>EXPLORA</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezadp del apartado
    st.markdown("""
    <div style='text-align: center; font-size: 20px;'>
    <p>¡Explora a tu criterio El Universo Ghibli! ◝(ᵔᗜᵔ)◜ El estudio cuenta con diversos géneros que pueden ser de tu agrado, o interés.</p>
    """, unsafe_allow_html=True) # Añadimos una breve descripción y bienvenida al apartado

    # Prepararemos una búsqueda por filtros de manera que el usuario se familiarice con la interfaz y conozca películas de su interés.
    # ===== BÚSQUEDA POR GÉNERO =====

    #Para esto, crearemos una lista con los géneros que hay en las películas del estudio
    generos_encontrados= [] # Se crea una lista vacia que almacenará los géneros, asignamos el nombre generos_encontrados
    
    # Se usarán los bucles "for" y ".iterrows()" para recorrer todas las filas del dataframe
    for i, fila in df.iterrows():
        t_genero = str(fila["Género"])  # Obtenemos todo el contenido de la columna "Genero" como un texto string (str) y lo guardamos en la variable texto_genero
        l_genero = t_genero.split(",")  # "split(",")" Separa el texto al encontrar una coma, eso facilitará el recorrido
        # Se crea un bucle "for" esto para quitar espacios de cada fila de genero y depurar la lista
        for genero in l_genero:
            l_genero_depurado = genero.strip().lower() # genero.strip() Elimina espacios en blanco al inicio y al final del texto. .lower() convierte el texto en minúsculas. Se asigna el nombre de l_genero_depurado
            generos_encontrados.append(l_genero_depurado) # Se agrega la lista depurada a la lista principal generos_encontrados
    
    gen_lista = sorted(set(generos_encontrados)) # Esto evita que los géneros no se repitan: "Set()" ya que los convierte en un set
    # .sorted toma todo el conjunto y lo ordena alfabeticamente, se guarda todas estas configuraciones en una lista: gen_lista 
   
    # === INTERFAZ DE BÚSQUEDA POR GÉNERO ===
    # Ahora crearemos la interfaz del buscador. Para esto, usaremos la función "st.multiselect" la cuál permite crear menús desplegables o "droop"
    # Llamaremos a este menú multiselección generos_seleccionados
    generos_seleccionados = st.multiselect(
        "¿Cuáles son los géneros de tu preferencia?:",
        gen_lista,                # De esta lista sacará los generos a mostrarse en el desplegable
        max_selections=2,         # La selección maxima será 2 géneros
        accept_new_options=False  # Desactivamos la opcion de agregar nuevas opciones
    )
    st.markdown(f"Géneros seleccionados: {generos_seleccionados}") # Esto mostrará los géneros que seleccionó el usuario

    # === BUSCADOR ====
    
    encontrado = False   # Creamos una variable de control que verifica si se hallaron resultados o no a base de resultados booleanos
    
    for i in range(len(df)):                       # Un bucle que recorre todos los índices de las filas del DataFrame.
        titulo_pelicula = df.loc[i, "Título"]      # Accede al valor de la columna "titulo" en la primera fila o "fila i" del DataFrame.
        portada_pelicula = df.loc[i, "Portada"]    # Accede al link de la imagen de portada correspondiente al nombre "titulo_pelicula" a la fila i.
        generos= df.loc[i, "Género"]               # Accede a los géneros, es el más importante del buscador.
        director_pelicula = df.loc[i, "Director"]  # Accede al valor de la columna "Director" en la primera fila o "fila i" del dataframe
        ano_pelicula = df.loc[i, "Año"]            # Accede al valor de la columna "Año" de la primera fila (fila i) en el Dataframe.
        duracion_pelicula = df.loc[i, "Duración"]  # Accede al valor de la columna "Duración" de la primera fila (fila i) en el dataframe.
        idioma_pelicula = df.loc[i, "Idioma"]      # Aaccede al valor de la columna "Idioma" de la primera fila del dataframe.
        clas_pelicula = df.loc[i, "Clasificación"] # Accede al valor de la columna "Clasificación" de la primera fila del dataframe.
    
    # ===SISTEMA DE FILTRO===
        
        coincide_genero = True # El uso de la variable boleana ayudará a filtrar la película que corresponde con los generos seleccionados por el usuario.
        for genero in generos_seleccionados: # Iteramos por cada género que el usuario haya seleccionado en el filtro de géneros.
            if genero not in str(generos).lower(): # Verifica si el valor de genero no está contenido en la lista normalizada a minusculas de generos
                coincide_genero= False # Si el genero no está en la lista, la variable será False,
                break # y el bucle se rompe.
        if coincide_genero:  # Si la película sí coincide con los géneros seleccionados entonces se mostrará lo siguiente: 
            col1, col2 = st.columns([1, 2])  # Se crean columnas, para mejor orden y visualización de los resultados
            with col1: # En la columna izquierda se muestra la imagen de la portada de la película.
                    st.image(portada_pelicula, width=200)
            with col2: # En la columna derecha se muestra la información como el título, año, director de la película y más
                    st.markdown(f"## {titulo_pelicula} (*{ano_pelicula}*)") # Mostramos el título de la película, con el año entre parentesis y cursiva                   
                    st.markdown(f"Director: {director_pelicula}") # Mostramos el nombre del director de la película
                    st.markdown(f"Duración: {duracion_pelicula} minutos") # Mostramos la duración de la película en minutos
                    st.markdown(f"Idioma: {idioma_pelicula}") # Mostramos el idioma de la película seleccionada
                    st.markdown(f"Clasificación: {clas_pelicula}") # Mostramos la clasificación de la película seleccionada
                    encontrado = True # Activa la variable booleana para marcar que sí hubo un resultado
    if not encontrado: # Si ninguna película pasó los filtros de género y duración:
        st.warning("No se encontraron películas de ese género") # Ejecutará un mensaje.
elif pagina_seleccionada == "Apartado Técnico": # Si escogemos "Apartado Técnico" de los botones de navegación, nos encontraremos en la tercera página
    st.markdown("<h1 style='text-align: center;'>APARTADO TÉCNICO</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezado del apartado
    st.markdown("¡Conoce acerca de datos de las películas del estudio! Datos como críticas, premios ganados, nominaciones, presupuestos, recaudaciones, popularidad y más (˶°ㅁ°)!! ")
    st.markdown("---") # Generamos un separador
    
    #Generaremos unas tarjetas para cada una de las películas que contendran información técnica acerca de estas
    #  CONTROL DE SESIÓN 
    if "pelicula_elegida" not in st.session_state:      # Crear la variable en session_state si aún no existe y evita errores por variables inexistentes.
        st.session_state.pelicula_elegida = None        # Si no existe, se crea y se inicializa con None.
    
    #  LISTA DE PELÍCULAS Y PORTADAS 
    lista_peliculas = df["Título"].tolist() # Convertimos la columna "Título" de la base de datos en una lista.

    # Creamos Diccionario que relaciona cada título de película con su portada respectiva en la base de datos (df)
    portadas1 = { df.loc[i,"Título"]: df.loc[i,"Portada"] for i in range(len(df)) }


    #  SI NO SE HA ELEGIDO PELÍCULA: MOSTRAR MENÚ DE PORTADAS 
    if st.session_state.pelicula_elegida is None:

        st.markdown("<h3 style='text-align: left;'> Selecciona una película para conocer más detalles de esta:</h3>", unsafe_allow_html=True)
        cols = st.columns(4)  # Se mostrará la lista de películas en 4 columnas

        # enumerate() devuelve pares de (índice, valor) de la lista, 
        for i, titulo in enumerate(lista_peliculas): # Se recorrerá la lista y tomará el índice disponible de la lista pareada de lista_peliculas
            col = cols[i % 4] # Se seleccionará un elemento de la lista cols de manera cíclica usando el índice

            with col: # Todo lo que este dentro se mostrará en una columna 
                st.image(portadas1[titulo], use_container_width=True) # Se muestra la imagen de portada correspondiente a "titulo" en el diccionario "portadas1". use_container_width=True hace que la imagen ocupe todo el ancho de la columna.
                if st.button(titulo, key=titulo): # Crea un botón con el texto del título de la película. key=titulo asegura que cada botón tenga una identidad única en Streamlit.
                    # Se cumple la condición una vez se hace click en el botón
                    st.session_state.pelicula_elegida = titulo  # Guarda el título de la película elegida en session_state. Esto permite se recuerde qué película seleccionó el usuario aunque la página se recargue o interactúe con otros botones.
                    st.rerun() # Fuerza a Streamlit a volver a ejecutar todo el script desde el inicio.

    #  SI YA SE SELECCIONÓ UNA PELÍCULA: Se mostrará la tarjeta técnica 
    else:
        # Recupera el título de la película que el usuario seleccionó previamente
        titulo = st.session_state.pelicula_elegida
    
        # Filtra el DataFrame para obtener los datos de la película seleccionada
        # .iloc[0] toma la primera fila resultante (ya que el filtro devuelve un DataFrame)
        datos = df[df["Título"] == titulo].iloc[0]

        # Creamos un encabezado con el título de la película en Streamlit
        st.markdown(f"## 🎬 Detalles técnicos de **{titulo}**")
    
        # Creamos 3 columnas para organizar la información visualmente
        col1, col2, col3 = st.columns(3)
    
        # Columna 1: Muestra la imagen de la portada
        with col1:
            st.image(datos["Portada"], width=200) # Muestra la portada de la película con ancho fijo de 200 píxeles

        # Columna 2: Muestra la información técnica
        with col2:
            # Muestra el director de la película en negrita
            st.markdown(f"**Dirigido por:** {datos['Director']}")
            # Muestra el presupuesto de la película
            st.markdown(f"**Presupuesto:** {datos['Presupuesto']} USD")
            # Muestra la recaudación mundial
            st.markdown(f"**Recaudación Mundial:** {datos['Recaudación_mundial']} USD")
            # Muestra la fecha de estreno
            st.markdown(f"**Fecha de estreno:** {datos['Fecha_estreno']}")
            # Muestra el tipo de estreno (cine, streaming, etc.)
            st.markdown(f"**Tipo de estreno:** {datos['Estreno']}")
            # Muestra el estudio o estudios a cargo
            st.markdown(f"**Estudio/s a cargo:** {datos['Estudio']}")
            # Muestra la distribuidora de la película
            st.markdown(f"**Distribuido por:** {datos['Distribuidora']}")
            # Muestra la fuente o adaptación de la película (libro, manga, etc.)
            st.markdown(f"**Adaptación de:**")
            st.markdown(f"{datos['Adaptaciones']}")

        # Columna 3: Muestra premios, nominaciones y otros datos
        with col3:
            # Muestra la sección de premios ganados
            st.markdown(f"**Premios Ganados**")
            st.markdown(f"*{datos['Premios_ganados']}* | {datos['Premios_nom']}")
            # Muestra la sección de nominaciones
            st.markdown(f"**Nominaciones**")
            st.markdown(f"*{datos['Nominaciones']}* | {datos['Nomi_nom']}")
            # Muestra la reseña de público japonés
            st.markdown(f"**Reseña del público japonés:** {datos['Opinión_Japón']}")
            # Muestra la puntuación de IMDb
            st.markdown(f"**Puntuación (IMDb):** {datos['Crítica_IMDb']}")
            

        st.markdown("---") # Se genera un separador para ordenar.

        # BOTÓN PARA VOLVER
        if st.button("Llevame de regreso al menú"): # Si el botón recibe un click,
            st.session_state.pelicula_elegida = None # Se resetea la variable de sesión que almacena la película seleccionada
            st.rerun() # Por lo que fuerza a Streamlit a volver a ejecutar todo el script desde el inicio,
            # Lo que nos devuelve al menú principal.

    
    # ====== GRÁFICO GENERAL DE PRESUPUESTO VS RECAUDACIÓN======
    # Creamos un gráfico general de presupuestos y recaudaciones de las películas de Studio Ghibli
    st.markdown("## Gráfico general de Presupuesto vs Recaudación mundial por película") # Asignamos un título, 
    # Extraemos los valores de las columnas "Título" y "Año" de la base de datos para crear una nueva variable mixta
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")"  

    #  LIMPIEZA DE DATOS 
    # Se convierten los valores eliminando símbolos y comas con .str 
    # Limpieza y conversión de la columna "Presupuesto" de la df
    df["Presupuesto"] = (
        df["Presupuesto"]      # Selecciona la columna "Presupuesto" de la base de datos
        .astype(str)           # Convierte todos los valores a texto (string)
        .str.replace(",", "")  # <---- Elimina tanto comas como espacios de la columna "Presupuesto"
        .astype(float)         # Convierte nuevamente los valores a tipo float para poder hacer cálculos.
    )

    # Limpieza y conversión de la columna "Recaudación_mundial" de la df
    df["Recaudación_mundial"] = (
        df["Recaudación_mundial"]   # Selecciona la columna "Recaudación_mundial" de la base de datos
        .astype(str)                # Convierte todos los valores a texto (string)
        .str.replace(",", "") # <---- Elimina comas y espacios de la columna "Recaudación_mundial"
        .astype(float)              # Convierte nuevamente los valores a tipo float para poder hacer cálculos.
    )

    # Se ordena la base de datos (df) según la columna "Recaudación_mundial" de mayor a menor.
    df_sorted = df.sort_values("Recaudación_mundial", ascending=False) 

    #  GRÁFICO DE PRESUPUESTO Y RECAUDACIÓN MUNDIAL
    
    # Se crea la figura y los ejes del gráfico.
    fig, ax = plt.subplots(figsize=(10, 7)) # figsize hace posible modificar el tamaño y formato de los gráficos
    y = df_sorted["Titulo_Año"]             # Se grafican los nombres de las películas en el eje Y
    presupuesto = df_sorted["Presupuesto"]  # Le asignamos el nombre de presupuesto a la lista filtrada de "Presupuesto" de la df para graficarlos
    recaudacion = df_sorted["Recaudación_mundial"] # Le asignamos el nombre de recaudación a la lista filtrada de "Recaudación_mundial" de la df y la graficamos

    # Posiciones en el eje Y para ubicar las barras
    y_pos = np.arange(len(y))           # np.arange genera una secuencia de números del 0 al número de películas -1
    height = 0.35  # Define la altura y separación de las barras

    # az.barh son las barras horizontales lado a lado que se mostraran en el gráfico, podemos editar el color de estas con "color"
    ax.barh(y_pos - height/2, presupuesto, height=height, label="Presupuesto", alpha=0.7, color="#BFBC6F") # Barra de presupuestos, posicion del eje, longitud de barra, altura de la barra, etiqueta, transparencia y color.
    ax.barh(y_pos + height/2, recaudacion, height=height, label="Recaudación", alpha=0.7, color="#5B8254") # Barra de recaudaciones, posicion del eje, longitud, altura, etiqueta, transparencia y color de la barra.

    # Estética
    ax.set_yticks(y_pos)                                        # Ubica las posiciones de las etiquetas en el eje Y
    ax.set_yticklabels(y, fontsize=9)                           # Asigna los nombres de las películas y tamaño de letra
    ax.set_xlabel("Monto en millones (USD)")                    # label establece las etiquetas o rótulos del eje correspondiente, en este caso el eje x
    ax.set_title("Presupuesto vs Recaudación – Studio Ghibli")  # Establece el encabezado del gráfico
    ax.legend()                                                 # Muestra la leyenda para identificar barras de Presupuesto y Recaudación

    plt.tight_layout()                                     # Ajusta el espaciado para que no se corten etiquetas ni título
    st.pyplot(fig)                                          # Muestra el gráfico en Streamlit


    # === GRÁFICO DE FECHAS DE ESTRENO ===
    # Creamos un gráfico para las fechas de estreno

    st.markdown("## Línea de tiempo cronológica de fechas de estreno de películas Ghibli") # Creamos un titulo para el gráfico

    # Convertimos la columna "Fecha_estreno" a tipo datetime
    # errors="coerce" convierte valores no válidos en NaT (not a time)
    df["Fecha_estreno"] = pd.to_datetime(df["Fecha_estreno"], errors="coerce")

    # Asignamos colores según el tipo de estreno
    def asignar_color(estreno):
        estreno = str(estreno)  # Asegura que el valor sea un string
        if "Festival" in estreno:    # Si contiene "Festival", devuelve amarillo
            return "#CEC917"
        elif "Streaming" in estreno: # Si contiene "Streaming", devuelve verde claro
            return "#58A449"
        elif "Internacional" in estreno: # Si contiene "Internacional", devuelve verde oscuro
            return "#2C715F"
        else:                         # Para cualquier otro tipo, devuelve gris
            return "gray"

    # Aplicamos la función a la columna "Estreno" para crear una nueva columna "Color"
    df["Color"] = df["Estreno"].apply(asignar_color)

    # Ordenamos las películas por fecha de estreno
    df = df.sort_values("Fecha_estreno").reset_index(drop=True)  
    # reset_index(drop=True) asegura que el índice sea consecutivo después de ordenar

    # Creamos del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Crea la figura y eje con un tamaño personalizado

    # Scatter plot: eje X = fecha de estreno, eje Y = índice de la fila
    # s=120 define el tamaño de los puntos, c=df["Color"]  defien el color de cada punto según tipo de estreno
    ax.scatter(df["Fecha_estreno"], df.index, s=120, c=df["Color"])

    # Etiquetas del eje Y
    ax.set_yticks(df.index)                     # Define las posiciones de los puntos en el eje Y
    ax.set_yticklabels(df["Título"], fontsize=9)  # Define los nombres de las películas y tamaño de fuente
    ax.set_xlabel("Fecha de Estreno")           # Define la etiqueta del eje X
    ax.set_title("Timeline cronológico de estrenos - Studio Ghibli")  # Asigna el encabezado del gráfico
    ax.grid(axis="x", linestyle="--", alpha=0.4)  # Muestra líneas de cuadrícula solo en X, con transparencia

    # Creamos una leyenda personalizada para mejor lectura del gráfico
    legend_patches = [
        mpatches.Patch(color="#2C715F", label="Internacional"),   # Asigna el color verde oscuro para estrenos internacionales
        mpatches.Patch(color="#58A449", label="Streaming"),       # Verde claro para streaming
        mpatches.Patch(color="#CEC917", label="Festival"),        # Amarillo para festivales
        mpatches.Patch(color="gray", label="Otro / No clasificado") # Y gris para los demás
    ]

    # Agregamos la leyenda al gráfico
    ax.legend(handles=legend_patches, title="Tipo de estreno", loc="upper left")
    plt.tight_layout()    # Ajustamos los márgenes
    st.pyplot(fig) # Mostramos el gráfico en Streamlit
    plt.close(fig) # Cerramos la figura para liberar memoria


    # ====== CONTEO DE PREMIOS Y NOMINACIONES=====
    # Crearemos un conteo de premios y nominaciones
    st.markdown(" ")
    st.markdown("## Nominaciones y Premios Totales del Estudio") # Agregamos el encabezado del gráfico
    
    # Creamos una columna combinada "Título (Año)" a partir de las columanas "Título" y "Año" de la df para usar en etiquetas o gráficos
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")"

    # Creamos contadores de premios para el gráfico de premios
    con_premios = 0 # Contador para películas que ganaron premios
    sin_premios = 0 # Contador para películas sin premios

    # for itera sobre cada fila del DataFrame
    for index, row in df.iterrows():
        plt.figure(1) # Selecciona la figura 1
        if row["Premios_ganados"] > 0: # Si la película tiene más de un premio
            con_premios += 1  # la porción de "con premios" incrementa
        else:                  # De lo contrario
            sin_premios += 1    # Incrementa la porción de "sin premios"

    # Establecemos la configuración del pie chart de premios
    labels = ["Películas con premios", "Películas sin premios"] # Labels asigna etiquetas de cada porción
    sizes = [con_premios, sin_premios]  # El tamaño de cada porción
    colors = ['#c6c983', "#A57745"]  # Asigna colores diferenciados para el gráfico
    explode = (0.03, 0.05)  # Explode es usado para separar las porciones

    # creación de la figura del pie chart
    plt.figure(figsize=(4, 4), dpi=100)
    plt.pie(
        sizes,              # Asigna el tamaño de cada porción
        explode=explode,    # Define la separación de porciones
        labels=labels,      # Define las etiquetas
        colors=colors,      # Define los colores
        autopct='%1.1f%%',  # Muestra el porcentaje en cada porción
        shadow=True,        # Muestra la sombra detrás del gráfico
        startangle=50       # Define el ángulo de inicio del gráfico
    )

    plt.title("Distribución de premiaciones del Studio Ghibli") # Asignamos el encabezado al gráfico
    plt.axis("equal") # equal permite mantener el aspecto circular perfecto
    plt.savefig("Premiaciones_graf.png") # Savefig permite guardar el gráfico como imagen
    plt.close() # Cierra la figura para liberar memoria

    st.markdown(" ")

    # Gráfico de distribución de nominaciones
    # Creamos los contadores de nominaciones

    con_nominaciones = 0
    sin_nominaciones = 0

    for index, row in df.iterrows():
        plt.figure(2)
        if row["Nominaciones"] > 0:
            con_nominaciones += 1
        else:
            sin_nominaciones += 1

    labels = ["Películas con nominaciones", "Sin nominaciones"]
    sizes = [con_nominaciones, sin_nominaciones]
    colors = ['#c6c983', "#A57745"]  # Nuevos colores para el gráfico de nominaciones
    explode = (0.05, 0.03)

    plt.figure(figsize=(4, 4), dpi=100)
    plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=100
    )

    plt.title("Distribución de nominaciones del Studio Ghibli")
    plt.axis("equal")
    plt.savefig("Nominaciones_graf.png")
    st.pyplot(plt)
    plt.close()


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
        color="#58A449",  
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

    # ==== GRÁFICO DE BARRAS DE ADAPTACIONES POR EL STUDIO GHIBLI ====
    st.markdown("## Tabla General de tipos de obras adaptadas por Studio Ghibli") # Agregamos un título para el gráfico

    # Agrupamos por tipo de adaptación con groupby y lo nombramos conteo_adaptaciones
    conteo_adaptaciones = df["Adaptaciones"].groupby(df["Adaptaciones"]).count() # Extraemos los valores de la columna "Adaptaciones" de la base de datos

    # Creamos el gráfico de barras horizontal
    fig, ax = plt.subplots(figsize=(10, 6)) 
    ax.barh(conteo_adaptaciones.index, conteo_adaptaciones.values, color="#8C4A92")

    #Establecemos las etiquetas correspondientes
    ax.set_xlabel("Cantidad de películas")  # La cantidad de películas (número) se mostrará en dirección horizontal...
    ax.set_ylabel("Tipo de adaptación")     # Mientras que el tipo de adaptación (nombres) se mostrará de forma vertical
    ax.set_title("Distribución de tipos de obras adaptadas por Studio Ghibli") # ax.set_title define el encabezado del gráfico
    #Mostramos el gráfico 
    plt.tight_layout()
    st.pyplot(fig)

elif pagina_seleccionada == "Apartado Artistico":  # Si el usuario selecciona la opción "Apartado Artistico" de los botones de navegación, nos encontraremos en la cuarta página.
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
            st.markdown("### Personajes")
            st.markdown(f"**Protagonista:** {datos['Protagonista']}")

        with col3:
            
            antagonista = datos["presencia_anta"]
            nom_anta = datos["Antagonista"]
            if str(antagonista).lower() == "true" and pd.notna(nom_anta):
                st.markdown(f"**Antagonista:** {nom_anta}")
            else:
                st.markdown("**Antagonista:** _No hay antagonista en esta película_")

            criatura_f = datos["presencia_criat"]
            nom_criat = datos["Criaturas_fantásticas"]
            if str(criatura_f).lower() == "true" and pd.notna(nom_criat):
                st.markdown(f"**Criatura/s fantástica/s:** {nom_criat}")
            else:
                st.markdown("**Criatura/s fantástica/s:** _No hay criaturas fantasticas en esta película_")
            
            banda = datos["Banda_sonora"]
            banda_link = datos["Banda_link"]
            link_banda = datos["link_banda_sonora"]

            st.markdown("### Temas")
            st.markdown(f"{datos['Temas_principales']}")
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
    
    # ====GRÁFICO DE REPRESENTACIONES====
    # Crearemos un gráfico de barras acerca de la representación de niños y mujeres en las películas del Studio Ghibli
    st.markdown("## Gráfico de barras General de representación en las películas de Studio Ghibli") # Asignamos un título al gráfico
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")"  # Usamos para mostrar tanto el título de la película junto al año de estreno en el gráfico
    # Se crea un diccionario que se llamará mapeo, en la cuál asignamos valores númericos a los valores ...
    
    mapeo = {
        "Baja": 1,      # baja recibirá el valor de 1
        "Media": 2,     # media recibirá el valor de 2
        "Alta": 3,      # alta recibirá el valor de 3
        "Muy alta": 4   # muy alta recibirá el valor de 4
    }

    # Anexamos el diccionario de mapeo a las columnas extraídas de la base de datos (df) y renombramos
    df["Representación_infantil_num"] = df["Representación_infantil"].map(mapeo)
    df["Representación_femenina_num"] = df["Representación_femenina"].map(mapeo)
    
    # Agrupamos esos datos de representación por película-año con group.by 
    df_grouped = df.groupby("Titulo_Año")[["Representación_infantil_num", "Representación_femenina_num"]].mean()

    # Creamos el gráfico de barras agrupadas horizontales, usando figsize para configurar el tamaño y proporciones de esta
    ax = df_grouped.plot(kind="barh", figsize=(10, 6))

    #Graficamos
    fig, ax = plt.subplots(figsize=(14,9))
    df_grouped.plot(kind="barh", ax=ax, color= ["#BFBC6F","#5B8254"]) # Asignamos colores a las barras para diferenciarlas
    ax.set_xlabel("Nivel de representación") # Agregamos etiquetas al eje x, nivel de representación
    ax.set_ylabel("Película")                # La etiqueta del eje y es el nombre de las películas
    ax.set_title("Representación infantil y femenina por película")
    ax.legend(["Representación infantil", "Representación femenina"], title="Indicadores") # Agregamos una leyenda para mejor lectura del gráfico con ax.legend
    plt.tight_layout()
    # Mostrar en Streamlit
    st.pyplot(fig)
    # Agregamos un texto explicativo para aún mejor lectura del gráfico
    st.markdown("**Escala de representación:** 1 = Baja • 2 = Media • 3 = Alta • 4 = Muy alta")
    st.markdown(" ")
    
    
    
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
    ax.barh(conteo_colores.index, conteo_colores.values, color="#2C715F")
    ax.set_ylabel("Colores y Tonos") # Asignamos las etiquetas del eje y
    ax.set_xlabel("Frecuencia")       # Así como las etiquetas del eje x
    ax.set_title("Comparativa de paletas de color en Studio Ghibli") # Asignamos el encabezado al gráfico con ax.set_title
    plt.xticks(rotation=45)

    st.pyplot(fig) # Mostramos el gráfico

    # ====GRÁFICO DE TIPO DE ANIMACIÓN====

    st.markdown("## Tipo de animación más usado en las películas de Studio Ghibli") # Agregamos un título para el gráfico
    # Contamos la frecuencia de cada valor en la columna "Tipo_de_animación" de la base de datos (df)
    conteo_animacion = df["Tipo_de_animación"].value_counts() # Para eso, usamos .value_counts() y lo nombramos conteo_animación

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(
        conteo_animacion.index,
        conteo_animacion.values,
        color="#2C715F"             # Asignamos un color a las barras
    )

    ax.set_xlabel("Tipo de animación") # Asignamos una etiqueta al eje x, en este caso, el tipo de animación (nombres)
    ax.set_ylabel("Cantidad de películas") # Y al eje y, la cantidad de películas (osea, números)
    ax.set_title("Distribución de tipos de animación en Studio Ghibli") # Asignamos un encabezado para el gráfico
    plt.xticks(rotation=360) # plt.xticks modifica la rotación de las etiquetas o nombres

    st.pyplot(fig) # Mostramos el gráfico

    #====GRÁFICOS DE TÉCNICA USADAS====

    st.markdown("## Técnicas más usadas en las películas de Studio Ghibli") #  Asignamos otro título para el gráfico

    # Contamos la frecuencia de los valores en la columna "Técnica_usada" de la base de datos con .value_counts
    conteo_tecnica = df["Técnica_usada"].value_counts() # Y le asignamos el nombre de conteo_tecnica

    fig, ax = plt.subplots(figsize=(10, 5)) # Ajustamos el tamaño y proporción del gráfico con figsize
    
    # Para realizar un gráfico horizontal se usa ax.barh en lugar de ax.bar 
    ax.barh(
        conteo_tecnica.index, 
        conteo_tecnica.values,
        color="#2C715F" # Asignamos colores a las barras con color
    )

    # Asignamos las respectivas etiquetas en cada eje, así como el encabezado del gráfico
    ax.set_ylabel("Técnica de animación") 
    ax.set_xlabel("Cantidad de películas")
    ax.set_title("Frecuencia de técnicas utilizadas")
    plt.xticks(rotation=45) # Ajustamos la rotación de las etiquetas

    st.pyplot(fig) # Mostramos el gráfico


    # === GRÁFICO PIE DE ELEMENTOS MÁGICOS EN LAS PELÍCULAS DE ESTUDIO GHIBLI ===
    st.markdown("## Presencia de elementos mágicos en las películas de Studio Ghibli") # Agregamos un título para el gráfico

    # Agrupamos usando groupby y contamos cuántas películas tienen y no tienen elementos mágicos
    df_grouped_magia = df.groupby("Elementos_mágicos")["Título"].count() # Extraemos los valores de las columnas "Elementos_mágicos" y "Título" de la df
    # Y lo nombramos df_grouped_magia

    # Asignamos etiquetas (labels) para el gráfico
    labels = df_grouped_magia.index.tolist()
    sizes = df_grouped_magia.values.tolist() # El tamaño será proporcional a los datos encontrados en grouped_magia
    colors = ['#7FB3D5', '#C39BD3']  # Colores diferenciados para cada porción
    explode = (0.05, 0.05)  # Explode se usa para la separación visual de las porciones

    # Crear figura, edita el tamaño y proporción de esta
    fig, ax = plt.subplots(figsize=(3, 3), dpi=100)

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        explode=explode,
        shadow=True,
        startangle=90
    )

    ax.set_title("Presencia de elementos mágicos en las películas") # Asignamos un encabezado al gráfico

    st.pyplot(fig) # Mostramos el gráfico
    plt.close()
   
    #==== GRÁFICOS DE ESTILO VISUAL ====

    st.markdown("## Nube de palabras: Estilo visual más usado en las películas de Studio Ghibli") # Agregamos un título para el gráfico

    # Generamos el conteo de los estilos visuales hallados en la base de datos, columna "Estilo_visual"
    estilos_expandidos = (
        df["Estilo_visual"]
        .str.lower()               # .lower convierte todo a minusculas
        .str.split(",")            # .split separa por coma
        .explode()                 # .explode crea una fila por cada estilo
        .str.strip()               # .strip elimina espacios
    )
    
    conteo_estilo = estilos_expandidos.value_counts() # Contamos la frecuencia de los valores hallados en la lista de estilos_expandidos con value_counts

    wc_estilos = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="viridis"  # cambiamos el color del gráfico
    ).generate_from_frequencies(conteo_estilo.to_dict())

    # Mostrar en Streamlit
    plt.figure(figsize=(10, 6)) # Asignamos el tamaño del gráfico
    plt.imshow(wc_estilos, interpolation="bilinear")
    plt.axis("off") # Los ejes están desactivados "off"

    st.pyplot(plt) # Mostramos el gráfico
    plt.close()

    st.markdown(" ")

    # === NUBE DE ANIMALES ===
    st.markdown("## Nube de Palabras: Animales recurrentes en Studio Ghibli") # Asignamos un título para el siguiente gr+afico
    # Ahora crearemos una wordcloud para la recurrencia de animales en las películas del estudio
    # Extraemos los datos de la columna "Animales" en una lista de palabras separadas con .split
    lista_animales = df["Animales"].dropna().str.split(",").sum() # Y le asignamos el nombre de lista_animales

    # Convertimos a minúsculas y limpiamos espacios con .strip y reducimos a minusculas con .lower
    lista_animales = [a.strip().lower() for a in lista_animales]

    # Creamos diccionario de frecuencias
    frecuencias_animales = {}

    for animal in lista_animales:                               # For hace que para cada animal en lista de animales
        frecuencias_animales[animal] = frecuencias_animales.get(animal, 0) + 1

    # Generamos la nube de palabras y le asignamos el nombre "wv_animales"
    wc_animales = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate_from_frequencies(frecuencias_animales)

    # Mostramos el gráfico
    plt.figure(figsize=(8, 8))
    plt.imshow(wc_animales, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
    plt.close()

    # ==== Wordcloud de transportes recurrentes en Studio Ghibli
    st.markdown("## Nube de Palabras: Transportes recurrentes en Studio Ghibli") # Asignamos un titulo al gráfico

    # Crearemos otra wordcloud para la recurrencia de transportes en las películas del estudio
    # Convertimos la columna "Transporte" en una lista de palabras separadas por comas como en la otra nube
    # Le asignamos el nombre lista_transportes
    lista_transportes = df["Transporte"].dropna().str.split(",").sum()

    # Limpiamos y pasamos a minusculas la lista
    lista_transportes = [t.strip().lower() for t in lista_transportes]

    # Creamos diccionario de frecuencias y lo guardamos como "frecuencias_transportes"
    frecuencias_transportes = {}
    for t in lista_transportes:
        frecuencias_transportes[t] = frecuencias_transportes.get(t, 0) + 1

    # Generamos la nube de palabras y le asignamos el nombre "wc_transportes"
    wc_transportes = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate_from_frequencies(frecuencias_transportes)

    # Editamos el tamañoy proporciones y mostramos el gráfico
    plt.figure(figsize=(8, 8))
    plt.imshow(wc_transportes, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
    plt.close()

else: # Sino se eligió ninguna de las páginas anteriores entonces se mostrará la de "Curiosidades"
    st.markdown("<h1 style='text-align: center;'>CURIOSIDADES Y MÁS</h1>", unsafe_allow_html=True) #Agregamos otro st. markdown para el encabezado del apartado
    # Escribimos un mensaje de Bienvenida y que explique de que trata el apartado
    st.markdown("""
    <div style='font-size: 20px;'> <p>¡Bienvenido/a a la sección de curiosidades y más!</p>
    <p> Aquí podrás divertirte un rato mientras pones a prueba tu conocimiento acerca de la filmografía de este estudio.</p> 
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---") # Agregamos un separador

    # ===== JUEGO DE ¿SABÍAS QUÉ? =====
    # Generaremos un botón al cuál al usuario darle clic, recibirá un dato random o curiosidad del Studio, usando random
    df["Titulo_Año"] = df["Título"] + " (" + df["Año"].astype(str) + ")" # Agrupamos las columnas "Título" y "Año" de nuevo para mejor visualización

    # Agregamos un encabezado y pequeñas instrucciones para el juego
    st.markdown("""<h2 div style='text-align: center;'>Datos Curiosos</div></h2>""", unsafe_allow_html=True)
    st.markdown("Dale click al botón de 'Dame un dato curioso' para obtener un dato curioso de alguna película del estudio.")

    # Generamos el botón con la función de st.button
    if st.button("Dame un dato curioso 🤓"): # con IF si se le da clic al botón...
        fila = df.sample(1).iloc[0]             # Toma 1 fila al azar de la base de datos "df" y extrae la primera (y única) fila de esta

        personas_importantes = []               # Generamos una lista vacía en la cuál se agregaran los nombres de las personas que participaron en las películas

        if fila["Participación_Hayao_M"]:                   # Si la columna "Participación_Hayao_M" es verdadera,
            personas_importantes.append("Hayao Miyazaki")   # Se agregará "Hayao Miyazaki" a la lusta
        if fila["Participación_Isao_T"]:                    # Si la columna "Participación_Isao_T" es verdadera
            personas_importantes.append("Isao Takahata")    # Se agregará "Isao Takahata" a la lista
        if fila["Participación_Joe_H"]:                     # Si la columna "Participación_Joe_H" es verdadera
            personas_importantes.append("Joe Hisaishi (Compositor)")   # Se agregará "Joe Hisaishi (Compositor)" a la lista

        # Convertimos la lista en un texto 
        if len(personas_importantes) == 1:      # Si solo hay un nombre, se crea una frase usando ese único nombre.
            texto_personas_importantes = f"fue realizado por **{personas_importantes[0]}**"
        elif len(personas_importantes) == 2:    # Si hay dos nombres, se crea una frase usando esos dos nombres.
            texto_personas_importantes = f"fue realizado por **{personas_importantes[0]}** y **{personas_importantes[1]}**"
        elif len(personas_importantes) == 3:     # Si hay tres nombres, se crea una frase con los tres nombres completos.
            texto_personas_importantes = "contó con la participación de **Miyazaki, Takahata y Hisaishi**"
        else:                                    # De lo contrario, se mostrará el siguiente mensaje
            texto_personas_importantes = "tiene un equipo creativo único en el estudio"

        # Creamos la lista con las frases que tendrá el ¿Sabías qué?, y le asignaremos el nombre de plantilla
        # Algunas frases usan datos de la fila aleatoria seleccionada.
        # Otras usan datos globales del DataFrame: como... {fila['Nominaciones']} por ejemplo
        # df["Crítica_IMDb"].idxmax() → obtiene el índice de la película con mejor nota con .idxmax
        # df["Presupuesto"].max() → muestra el mayor presupuesto de todas las películas con .max
        # El formato ${:,} agrega comas a los números grandes:

        plantillas = [
            f"La película **{fila['Titulo_Año']}** tiene una calificación de **{fila['Crítica_IMDb']} en IMDb**.",
            f"¿Sabías que **{fila['Titulo_Año']}** ganó **{fila['Premios_ganados']} premios**?",
            f"**{fila['Titulo_Año']}** fue nominada a **{fila['Nominaciones']} premios**.",
            f"En Japón, la popularidad de **{fila['Titulo_Año']}** fue considerada **{fila['Popularidad_Japón']}**.",
            f"Fuera de Japón, la popularidad de **{fila['Titulo_Año']}** fue considera **{fila['Popularidad_internacional']}**",
            f"La recaudación mundial de **{fila['Titulo_Año']}** alcanzó los **${fila['Recaudación_mundial']:,}**.",
            f"La película **{fila['Titulo_Año']}** {texto_personas_importantes}.",
            "La película mejor puntuada en IMDb fue: " + df.loc[df["Crítica_IMDb"].idxmax(), "Titulo_Año"],
            "El presupuesto más alto fue de ${:,}.".format(df["Presupuesto"].max()),
            f"La película **{fila['Titulo_Año']}** es **{fila['Valor_cultural']}**.",

        ]

        st.info(random.choice(plantillas)) # Random.choice elige una frase al azar de la plantilla, y la muestra en un recuadro informativo de streamlit

    st.markdown("---") # Generamos un separador 

    # ============================================
    #  JUEGO DE ADIVINA LA PELÍCULA POR LA ESCENA
    # ============================================
    # Realizaremos un juego de adivinanzas con imagenes, también usando random.choice
    st.title("🎬 Juego: ¿A qué película pertenece esta imagen?")       # Crea un encabezado nuevo

    # Inicializar variables en session_state, este permite guardar valores entre ejecuciones.
    if "pelicula_objetivo" not in st.session_state:         # la película que el jugador debe adivinar
        st.session_state.pelicula_objetivo = None
    if "intentos" not in st.session_state:                  # Conteo de intentos del jugador
        st.session_state.intentos = 0
    if "juego_terminado" not in st.session_state:           # Indica si la ronda terminó
        st.session_state.juego_terminado = False

    #=========================================
    #  GENERAR UNA NUEVA PELÍCULA ALEATORIA 
    #=========================================

    def nueva_ronda(): # Para iniciar una nueva ronda...
        st.session_state.pelicula_objetivo = df.sample(1).iloc[0] # df.sample(1) selecciona una película aleatoria del repertorio y iloc. la convierte en una serie para fácil acceso
        st.session_state.intentos = 0                             # esta línea se encarga de reiniciar los intentos
        st.session_state.juego_terminado = False                   # Indica si el juego está activo o no

    # Si es la primera vez, generar película
    if st.session_state.pelicula_objetivo is None:
        nueva_ronda()                                               # Si no hay película guardada todavía, se crea una usando nueva_ronda()


    pelicula = st.session_state.pelicula_objetivo           # Guarda la película actual en una variable "pelicula"

    # Mostrar la imagen al usuario desde la columna 'Portada'
    st.image(pelicula["foto_escena"], width=300, caption="¿Qué película es?") # Se agrega una pequeña descripción a la imagen con caption


    #===========================
    #  SISTEMA DE INTENTOS 
    #===========================
    if not st.session_state.juego_terminado:                               # Se usa st.session para que la película no cambie cada vez que se presione un botón.
        respuesta = st.text_input("Escribe el nombre de la película:")      # Crea una caja de texto donde el usuario escribe su respuesta.
    
        if st.button("Adivinar"):                                           # Detecta el clic en el botón "Adivinar" y revisa si la respuesta concuerda
            if respuesta.strip().lower() == pelicula["Título"].lower():     # .strip() elimina espacios antes o después .lower() convierte todo a minúsculas. Se compara con el título real en minúsculas
                st.success("🎉 ¡Correcto! Has adivinado la película.")      # Si la respuesta es correcta, muestra un mensaje positivo
                st.markdown(f"**Descripción de la escena:** {pelicula['Escena_icónica']}") # Un texto descriptivo de la escena y la columna Escena_icónica
                st.session_state.juego_terminado = True                      # Marca el juego como terminado.
            else:                           # En caso la respuesta sea incorrecta
                st.session_state.intentos += 1                             # Aumenta el contador de intentos y calcula cuantos quedan
                intentos_restantes = 3 - st.session_state.intentos         # Permite tres intentos, al equivocarse resta uno.
            
                if intentos_restantes > 0:                                 # Si aún tiene intentos disponibles
                    st.warning(f"❌ Incorrecto. Te quedan **{intentos_restantes}** intentos.")  # Muestra una advertencia y permite seguir jugando.
                else:                                   # De lo contrario, si se acabaron todos los intentos
                    st.error("💥 Se acabaron los intentos.")                        # Mostrará un mensaje de fallo definitivo
                    st.info(f"La respuesta correcta era: **{pelicula['Título']}**")     # Mostrará el título correcto
                    st.session_state.juego_terminado = True                              # Y terminará la ronda


     #  BOTÓN PARA NUEVA RONDA 
    if st.session_state.juego_terminado:                   # Si el juego ha terminado, 
        if st.button("Jugar otra vez 🔄"):                 # Sera posible que el botón 'Jugar otra vez' aparezca
            nueva_ronda()                                  # Y se inicia una nueva partida

    st.markdown("---") # Generamos otro separador
    # =============================
    #  JUEGO de ADIVINA EL DIRECTOR
    # =============================
    # Crearemos otro juego, en el cuál el usuario tendrá que adivinar al director de la película que se le asigne
    
    def iniciar_juego(df): # Crea la función para iniciar un nuevo juego
        pelicula = df.sample(1).iloc[0] # Selecciona una película aleatoria de la base de datos (df) y la convierte en serie con .iloc
        st.session_state["portada"] = pelicula["Portada"] # Guarda la imagen (portada) de la película seleccionada y la muestra en pantalla
        st.session_state["director_correcto"] = pelicula["Director"].lower()  # Guarda el nombre del director, en minúsculas, para comparaciones sin errores de mayúsculas
        st.session_state["foto_director"] = pelicula["foto_director"] # ✔ Guarda la foto del director que se mostrará si el usuario gana o pierde la ronda
        st.session_state["intentos"] = 0    # Reinicia el contador de intentos para la partida
        st.session_state["mensaje"] = ""    
        st.session_state["juego_activo"] = True # Indica que el juego está en curso

    # --------------------------
    #        INTERFAZ
    # --------------------------
    st.title("🎬 Adivina el Director") # Agregamos un título para el juego

    # Botón para iniciar el juego       
    if st.button("🎲 Nueva película"):  # Cuando el usuario presione el botón de Nueva película
        iniciar_juego(df)                # se activa la función iniciar_juego y se selecciona una película y se reinicia todo

    # Mostrar interfaz solo si hay juego activo
    if st.session_state.get("juego_activo", False): # Si no hay un juego activo, la interfaz no se muestra.

        st.image(st.session_state["portada"], width=300) # Muestra la portada de la película actual extraída de la columna "Portada" del df
        st.write("¿Quién es el director de esta película?") # Muestra las instrucciones para el jugador

        respuesta_2 = st.text_input("Escribe el nombre del director:") # Se crea una entrada para la respuesta escrita del jugador (.input) y se guarda en la variable respuesta_2.

        if st.button("Enviar respuesta"):           # Si el botón etecta el clic, procesa la respuesta.
            if respuesta_2.strip() == "":           # Si la respuesta está vacía, muestra una advertencia.
                st.warning("Ingresa un nombre.")    
            else:                                   # De lo contrario,
                st.session_state["intentos"] += 1   # Se suma un intento.

                if respuesta_2.lower().strip() == st.session_state["director_correcto"]:        # Se compara la respuesta en minúsculas y sin espacios con los datos guardados en "director_correcto"
                    st.success("🎉 ¡Correcto!")         # SI el resultado es correcto, muestra un mensaje de éxito
                    st.write(f"El director es **{st.session_state['director_correcto'].title()}**") # Muestra el nombre del director con .title()
                    st.image(st.session_state["foto_director"], width=200)  # Muestra la foto del director extraída de la columna "foto_director" de la base de datos
                    st.session_state["juego_activo"] = False                # Termina la partida.

                else:               # De lo contrario, calcula cuantos intentos ("intentos") quedan
                    intentos_restantes_2 = 3 - st.session_state["intentos"]

                    if intentos_restantes_2 > 0:    # Si aún quedan intentos, muestra mensaje de error y permite seguir jugando
                        st.error(f"❌ Incorrecto. Te quedan {intentos_restantes_2} intentos.")
                    else:                                           # Si ya no quedan intentos,
                        st.error("❌ Te quedaste sin intentos.")    # Muestra un mensaje de error
                        st.info(f"El director era **{st.session_state['director_correcto'].title()}**") # Muestra el nombre correcto del director.
                        st.image(st.session_state["foto_director"], width=200)                          # Muesta la imagen del director extraída de "foto_director"
                        st.session_state["juego_activo"] = False                                        # Y marca el juego como terminado.

