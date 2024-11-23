import streamlit as st

def cable_app():
    st.title("Cables")
    st.write("""
        Los **cables** son elementos estructurales flexibles que soportan cargas principalmente en tensión. 
        Se utilizan en puentes colgantes, sistemas de transmisión de energía y otras estructuras donde la flexibilidad es clave.
    """)
    
    st.write("**Ejemplo de Cálculo de un Cable usando SymPy**")
    from sympy.physics.continuum_mechanics.beam import Beam
from sympy.physics.continuum_mechanics.cable import Cable
c=Cable(("A", 0, 40),("B", 100, 20))
c.apply_load(0, ("X", 850))
c.solve(58.58, 0)
c.tension
c.tension_at(0)
c.reaction_loads

st.write("En desarrollo: Aquí se implementará el cálculo utilizando SymPy y la documentación referida.")

if __name__ == "__main__":
    cable_app()

