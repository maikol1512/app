import streamlit as st

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
