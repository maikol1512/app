import streamlit as st
from sympy.physics.continuum_mechanics.cable import Cable
st.set_page_config(
    page_title="Análisis de Vigas",  # Título en el navegador
    page_icon="🔧",  # Icono en el navegador
    layout="wide",  # Diseño amplio
    )

def cable_app():
    st.title("Análisis de Cables en Ingeniería")
    st.write("""
    Los cables son elementos estructurales utilizados para soportar cargas mediante tensión. 
    Son comunes en puentes colgantes, líneas de transmisión y diversas aplicaciones de ingeniería.
    """)

    # Ejemplo 1: Análisis de cable con cargas puntuales
    st.subheader("Ejemplo 1: Cargas Puntuales")
    st.write("""
    Un cable se admite en los puntos (0, 10) y (10, 10). 
    Dos cargas puntuales actúan verticalmente hacia abajo:
    - Carga 1: 3 kN a 2 metros del soporte izquierdo, y 3 metros por debajo del mismo.
    - Carga 2: 2 kN a 6 metros del soporte izquierdo, y 6 metros por debajo del mismo.
    """)

    # Crear el cable y aplicar cargas puntuales (con ángulo especificado y etiquetas únicas)
    cable1 = Cable(('A', 0, 10), ('B', 10, 10))
    cable1.apply_load(-1, ('Y1', 2, 7, 3, 270))  # Carga puntual 1 con magnitud 3 y ángulo 270 grados
    cable1.apply_load(-1, ('Y2', 6, 4, 2, 270))  # Carga puntual 2 con magnitud 2 y ángulo 270 grados
    
    # Resolver el cable
    cable1.solve()
    
    # Mostrar resultados
    st.subheader("Resultados para Ejemplo 1:")
    st.write("Tensiones en el cable:")
    tension_str = [str(t) for t in cable1.tension]
    st.write(tension_str)

    st.write("Cargas de reacción:")
    reaction_loads_str = [str(load) for load in cable1.reaction_loads]
    st.write(reaction_loads_str)

    st.write("Longitud del cable:")
    st.write(str(cable1.length))

    # Ejemplo 2: Longitud de cable ajustada
    st.subheader("Ejemplo 2: Longitud Ajustada del Cable")
    st.write("""
    Se ajusta la longitud del cable a 20 unidades.
    """)

    # Crear nuevo cable con longitud especificada
    cable2 = Cable(('A', 0, 10), ('B', 10, 10))
    cable2.apply_length(20)
    
    st.write("Nueva longitud del cable:")
    st.write(cable2.length)

    # Ejemplo 3: Carga distribuida
    st.subheader("Ejemplo 3: Carga Uniformemente Distribuida")
    st.write("""Se aplica una carga distribuida de 9 unidades a lo largo del cable.""")

    cable3 = Cable(('A', 0, 10), ('B', 10, 10))
    cable3.apply_load(0, ('D1', 0, 0, 9, 270))  # Carga distribuida (orden 0) con etiqueta 'D1' y ángulo 270 grados

    # Proporcionar el punto más bajo del cable para resolver
    x_lowest = 5  # Posición x estimada del punto más bajo
    y_lowest = 5  # Posición y estimada del punto más bajo
    cable3.solve(x_lowest, y_lowest)

    # Mostrar resultados
    st.write("Tensiones bajo carga distribuida:")
    tension_str = [str(t) for t in cable3.tension]
    st.write(tension_str)

    st.write("Cargas de reacción:")
    reaction_loads_str = [str(load) for load in cable3.reaction_loads]
    st.write(reaction_loads_str)

    # Ejemplo 4: Cambio de soporte
    st.subheader("Ejemplo 4: Cambio de Soporte")
    st.write("""
    Se cambia el soporte derecho del cable del punto B al punto C (5, 6).
    """)

    cable4 = Cable(('A', 0, 10), ('B', 10, 10))
    cable4.change_support('B', ('C', 5, 6))
    cable4.solve()
    
    st.write("Nuevos soportes:")
    st.write(cable4.supports)

if __name__ == "__main__":
    cable_app()
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://image.slidesdocs.com/responsive-images/background/abstract-scene-with-geometric-elements-in-blue-cyberpunk-style-for-advertising-3d-render-powerpoint-background_9380a653f1__960_540.jpg
    }
    </style>
    """,
    unsafe_allow_html=True
)


