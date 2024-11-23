import streamlit as st
from sympy import symbols, Eq, Function
from sympy.physics.continuum_mechanics.beam import Beam

def beam_app():
    st.title("Vigas (Beam)")
    st.write("""
        En ingeniería, una **viga** es un elemento estructural diseñado para soportar cargas aplicadas lateralmente 
        respecto a su eje longitudinal. Las vigas son esenciales para soportar cargas en edificios, puentes y otras estructuras.
    """)

    # Ejemplo simple usando sympy
    E, I, L = symbols('E I L')
    x = symbols('x')
    M = Function('M')(x)

    # Crear viga
    viga = Beam(10, E, I)
    viga.apply_load(-10, 5, -1)  # Carga puntual en x=5
    viga.bc_deflection.append((0, 0))  # Restricción en x=0
    viga.bc_deflection.append((10, 0))  # Restricción en x=10

    # Solución
    viga.solve_for_reaction_loads()
    momento_flector = viga.bending_moment()
    
    st.write("Momento flector de la viga:")
    st.latex(momento_flector)

if __name__ == "__main__":
    beam_app()

