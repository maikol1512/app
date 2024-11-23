import streamlit as st
st.set_page_config(
    page_title="Análisis de Vigas",  # Título en el navegador
    page_icon="🔧",  # Icono en el navegador
    layout="wide",  # Diseño amplio
    )


def main():
    st.title("Aplicación Multipágina: Mecánica de Medios Continuos")
    st.header("Introducción a la Mecánica de Medios Continuos")
    st.write("""
        La mecánica de medios continuos es una rama de la física que estudia el comportamiento de los materiales sólidos y fluidos 
        bajo la acción de fuerzas externas e internas. A continuación, se exploran tres estructuras fundamentales: 
        **Vigas (Beam)**, **Cerchas (Truss)** y **Cables**.
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
        background-image: url("https://media.istockphoto.com/id/1453207093/es/vector/fondo-navide%C3%B1o-polvo-azul-brillante.jpg?s=612x612&w=0&k=20&c=S5YCFOnEFu8ZWjNBCwmnB4QRHeBCvQCvpWtbv0yAQPw=");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
   