from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import pandas as pd

Session = sessionmaker(bind=engine)
session = Session()

# leer csv
df = pd.read_csv("./data/saludos_mundo.csv")

# se crea un objeto de tipo
# Saludo

miSaludo = Saludo()
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
