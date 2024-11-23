import streamlit as st

def truss_app():
    st.title("Cerchas (Truss)")
    st.write("""
        Una **cercha** es una estructura reticular que se usa comúnmente en puentes y techos. 
        Está formada por barras conectadas en nodos, que transmiten fuerzas principalmente por tracción o compresión.
    """)
    
    st.write("**Ejemplo y Cálculo de una Cercha usando SymPy**")
    from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
E, I, F = symbols('E I F')
l = symbols('l', positive=True)
b = Beam(l, E, I)
R1,R2 = symbols('R1  R2')
M1, M2 = symbols('M1, M2')
b.apply_load(R1, 0, -1)
b.apply_load(M1, 0, -2)
b.apply_load(R2, l, -1)
b.apply_load(M2, l, -2)
b.apply_load(-F, l/2, -1)
b.bc_deflection = [(0, 0),(l, 0)]
b.bc_slope = [(0, 0),(l, 0)]
b.solve_for_reaction_loads(R1, R2, M1, M2)
b.reaction_loads

b.load

b.shear_force()

b.bending_moment()

b.slope()

b.deflection()
st.write("En desarrollo: Aquí se implementará el cálculo utilizando SymPy y la documentación referida.")

if __name__ == "__main__":
    truss_app()
