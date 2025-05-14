import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar docentes
saludos_dos = session.query(Saludo2).all()

# Mostrar con Streamlit
st.title("Presentación de todos los Saludos Dos")

for saludo  in saludos_dos:
    st.write(saludo) # Usa es __str__
    st.markdown("---")

st.markdown("---")
st.title("Presentación de todos los Saludos de la Tabla 2")
lista = []

for s in saludos_dos:
    diccionario = {"id": s.id, "mensaje": s.mensaje, "tipo": s.tipo}
    lista.append(diccionario)

st.dataframe(lista)
