import streamlit as st
from sympy import symbols
from sympy.physics.continuum_mechanics.beam import Beam
st.set_page_config(
    page_title="Análisis de Vigas",  # Título en el navegador
    page_icon="🔧",  # Icono en el navegador
    layout="wide",  # Diseño amplio
    )

def beam_app():
    st.title("Viga (Docstrings)")
    st.write("""
    Este módulo se puede utilizar para resolver problemas de flexión de vigas 2D con Funciones de singularidad en mecánica.
             Una viga es un elemento estructural que es capaz de soportar una carga principalmente resistiendo contra la flexión. Las vigas se caracterizan por: su perfil de sección transversal (segundo momento de área), su longitud y su material.
    """)
    st.header("Ejemplos")
    st.write("""Hay una manga de 4 metros de longitud. Una carga distribuida constante de 6 N/m se aplica desde la mitad de la viga hasta el final. Hay dos soportes simples debajo de la viga, uno en el punto de inicio y otro en el punto de llegada de la viga. La deflexión de la viga en el extremo está restringida.

Usando la convención de signos de que las fuerzas hacia abajo son positivas.""")
    
    # Definir los parámetros simbólicos
    E, I = symbols('E, I')
    R1, R2 = symbols('R1, R2')
    b = Beam(4, E, I)
    b.apply_load(R1, 0, -1)
    b.apply_load(6, 2, 0)
    b.apply_load(R2, 4, -1)
    b.bc_deflection = [(0, 0), (4, 0)]
    b.boundary_conditions
    b.load
    b.solve_for_reaction_loads(R1, R2)
    b.load
    b.shear_force()
    b.bending_moment()
    b.slope()
    b.deflection()
    b.deflection().rewrite("Piecewise")

    # Definir los parámetros simbólicos
    st.write("""Calcule las reacciones de apoyo para una viga completamente simbólica de longitud L. Hay dos soportes simples debajo de la viga, uno en el punto de partida y otro en el punto final de la viga. La deflexión de la viga al final está restringido. La viga está cargada con:

una carga puntual descendente P1 aplicada a L/4

una carga puntual ascendente P2 aplicada a L/8

un momento en sentido contrario a las agujas del reloj M1 aplicado a L/2

un momento en el sentido de las agujas del reloj M2 aplicado a 3 * L / 4

una carga constante distribuida q1, aplicada hacia abajo, a partir de L/2 hasta 3 * L / 4

una carga constante distribuida q2, aplicada hacia arriba, a partir de 3*L/4 hasta L

No se necesitan suposiciones para las cargas simbólicas. Sin embargo, la definición de un length ayudará al algoritmo a calcular la solución.""")
    
    # Definir los parámetros simbólicos
    E, I = symbols('E, I')
    L = symbols("L", positive=True)
    P1, P2, M1, M2, q1, q2 = symbols("P1, P2, M1, M2, q1, q2")
    R1, R2 = symbols('R1, R2')
    b = Beam(L, E, I)
    b.apply_load(R1, 0, -1)
    b.apply_load(R2, L, -1)
    b.apply_load(P1, L/4, -1)
    b.apply_load(-P2, L/8, -1)
    b.apply_load(M1, L/2, -2)
    b.apply_load(-M2, 3*L/4, -2)
    b.apply_load(q1, L/2, 0, 3*L/4)
    b.apply_load(-q2, 3*L/4, 0, L)
    b.bc_deflection = [(0, 0), (L, 0)]
    b.solve_for_reaction_loads(R1, R2)
    print(b.reaction_loads[R1])
    print(b.reaction_loads[R2])

    st.write("Hay una manga de 4 metros de longitud. Un momento de magnitud 3 Nm es Se aplica en el sentido de las agujas del reloj en el punto de inicio del haz. Se aplica una carga puntual de magnitud 4 N desde la parte superior del haz a A 2 metros del punto de partida. Otra carga puntual de magnitud 5 N se aplica en la misma posición.")

    # Definir los parámetros simbólicos
    E, I = symbols('E, I')
    b = Beam(4, E, I)
    b.apply_load(-3, 0, -2)
    b.apply_load(4, 2, -1)
    b.apply_load(5, 2, -1)
    b.load
    b.applied_loads

    st.write("Hay una manga de 4 metros de longitud. Un momento de magnitud 3 Nm es Se aplica en el sentido de las agujas del reloj en el punto de inicio del haz. Se aplica una carga puntual de magnitud 4 N desde la parte superior del haz a A 2 metros del punto de partida y una carga de rampa parabólica de magnitud Se aplican 2 N/m por debajo de la viga a partir de 2 metros hasta 3 metros lejos del punto de inicio del haz.")

    # Definir los parámetros simbólicos
    E, I = symbols('E, I')
    b = Beam(4, E, I)
    b.apply_load(-3, 0, -2)
    b.apply_load(4, 2, -1)
    b.apply_load(-2, 2, 2, end=3)
    b.load

    st.write("""
    Hay una viga de 20 metros de longitud:
    - Se aplica un momento de magnitud **100 Nm** en el sentido de las agujas del reloj al final de la viga.
    - Se aplica una carga puntual de magnitud **8 N** hacia abajo a una distancia de **10 metros** desde el inicio.
    - La viga tiene un soporte fijo en el inicio y un rodillo en el extremo.
    
    Usando la convención de signos:
    - Las fuerzas ascendentes y momentos en sentido de las agujas del reloj son positivos.
    """)

    # Definir los parámetros simbólicos
    E, I = symbols('E, I')
    b = Beam(20, E, I)

    # Aplicar soportes y cargas
    p0, m0 = b.apply_support(0, 'fixed')  # Soporte fijo en el inicio
    p1 = b.apply_support(20, 'roller')   # Rodillo en el extremo
    b.apply_load(-8, 10, -1)             # Carga puntual descendente
    b.apply_load(100, 20, -2)            # Momento en el extremo

    # Resolver las reacciones en los apoyos
    b.solve_for_reaction_loads(p0, m0, p1)

    # Mostrar reacciones de apoyo
    st.write("**Reacciones de apoyo:**")
    st.write(f"- Reacción en el soporte fijo (p0): {str(b.reaction_loads[p0])}")
    st.write(f"- Momento en el soporte fijo (m0): {str(b.reaction_loads[m0])}")
    st.write(f"- Reacción en el soporte rodillo (p1): {str(b.reaction_loads[p1])}")

    # Mostrar las cargas aplicadas
    st.write("**Cargas aplicadas:**")
    st.latex(str(b.load))

    # Mostrar fuerza cortante y momento flector
    st.write("**Fuerza cortante (Shear Force):**")
    st.latex(str(b.shear_force().rewrite("Piecewise")))

    st.write("**Momento flector (Bending Moment):**")
    st.latex(str(b.bending_moment().rewrite("Piecewise")))

if __name__ == "__main__":
    beam_app()
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



