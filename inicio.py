import streamlit as st
st.set_page_config(
    page_title="Análisis de Vigas",  # Título en el navegador
    page_icon="🔧",  # Icono en el navegador
    layout="wide",  # Diseño amplio
    )


def main():
    st.title("Bienvenido a la Aplicación de Mecánica de Medios Continuos")
    st.header("Introducción")
    st.write("""
       La mecánica de medios continuos es una rama de la física y la ingeniería que estudia el comportamiento de materiales sólidos y fluidos cuando están sujetos a fuerzas externas o internas. Este campo es esencial para entender cómo los cuerpos deformables responden a las cargas aplicadas, y tiene aplicaciones en diseño estructural, análisis de materiales y más.

En esta aplicación, exploraremos tres conceptos clave de la mecánica de medios continuos mediante ejemplos prácticos:

Beam (Viga): Analizamos cómo las vigas soportan cargas, calculamos reacciones y diagramas de esfuerzo cortante y momento flector.
Truss (Cercha): Estudiamos estructuras formadas por barras conectadas, con énfasis en las fuerzas internas de sus elementos.
Cable: Examinamos el comportamiento de los cables sometidos a cargas distribuidas o puntuales.
    """)

    st.sidebar.title("Tabla de Contenidos")
    st.sidebar.write("Selecciona una página:")
    st.sidebar.markdown("[Viga (Beam)](pages/beam.py)")
    st.sidebar.markdown("[Cercha (Truss)](pages/truss.py)")
    st.sidebar.markdown("[Cable](pages/cable.py)")

if __name__ == "__main__":
    main()

    st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.google.com/imgres?q=fondos%20llamativos&imgurl=https%3A%2F%2Fimage.slidesdocs.com%2Fresponsive-images%2Fbackground%2Fabstract-scene-with-geometric-elements-in-blue-cyberpunk-style-for-advertising-3d-render-powerpoint-background_9380a653f1__960_540.jpg&imgrefurl=https%3A%2F%2Fslidesdocs.com%2Fes%2Ffondo%2Fescena-abstracta-con-elementos-geometricos-en-estilo-cyberpunk-azul-para-publicidad-3d-render-fondo-power-point_46da1ec4bb&docid=M4c3SepnxqMpCM&tbnid=EYxQNJCzMr_itM&vet=12ahUKEwiJnuGEovOJAxVnRjABHVclA1kQM3oECBcQAA..i&w=960&h=540&hcb=2&ved=2ahUKEwiJnuGEovOJAxVnRjABHVclA1kQM3oECBcQAA
    }
    </style>
    """,
    unsafe_allow_html=True
)
   