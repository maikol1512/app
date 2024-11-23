import streamlit as st
from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
st.set_page_config(
    page_title="Análisis de Vigas",  # Título en el navegador
    page_icon="🔧",  # Icono en el navegador
    layout="wide",  # Diseño amplio
    )

def truss_app():
    st.title("Análisis de Cerchas (Truss)")
    st.write("""
    Una viga plana es un elemento estructural que es capaz de soportar cargas a través de la resistencia al cizallamiento interno y a la flexión. 
    Las vigas se caracterizan por: su longitud, restricciones, segundo momento de área de la sección transversal y módulo elástico.
    """)

    # Ejemplo 1
    st.header("Ejemplo 1: Carga puntual y momento en viga simplemente apoyada")
    st.write("""
    Una viga de 30 metros de longitud:
    - Momento de 120 Nm en sentido contrario a las agujas del reloj en el extremo.
    - Carga puntual de 8 N al inicio.
    - Dos soportes simples: uno a 10 metros del inicio y otro al final.
    """)

    # Configurar viga
    E, I = symbols('E, I')
    R1, R2 = symbols('R1, R2')
    b = Beam(30, E, I)
    b.apply_load(8, 0, -1)  # Carga puntual
    b.apply_load(R1, 10, -1)  # Reacción en 10m
    b.apply_load(R2, 30, -1)  # Reacción en el extremo
    b.apply_load(120, 30, -2)  # Momento en el extremo
    b.bc_deflection.append((10, 0))
    b.bc_deflection.append((30, 0))

    # Resolver reacciones
    b.solve_for_reaction_loads(R1, R2)

    # Mostrar resultados
    st.write("**Reacciones de apoyo:**")
    st.write(f"- Reacción en el soporte a 10 m (R1): {str(b.reaction_loads[R1])}")
    st.write(f"- Reacción en el soporte a 30 m (R2): {str(b.reaction_loads[R2])}")

    st.write("**Cargas aplicadas:**")
    st.latex(str(b.load))

    st.write("**Fuerza cortante (Shear Force):**")
    st.latex(str(b.shear_force().rewrite("Piecewise")))

    st.write("**Momento flector (Bending Moment):**")
    st.latex(str(b.bending_moment().rewrite("Piecewise")))

    st.write("**Deflexión:**")
    st.latex(str(b.deflection().rewrite("Piecewise")))

    # Más ejemplos pueden añadirse aquí siguiendo el mismo patrón.
    
if __name__ == "__main__":
    truss_app()
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
   

  