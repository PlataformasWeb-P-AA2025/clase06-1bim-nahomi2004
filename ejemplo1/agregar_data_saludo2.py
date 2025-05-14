from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import pandas as pd

Session = sessionmaker(bind=engine)
session = Session()

# leer csv
df = pd.read_csv("./data/saludos_mundo.csv", sep='|')

# recorrer las filas del DataFrame y crear objetos Saludo2
for _, row in df.iterrows():
    saludo = Saludo2(
        mensaje=row['saludo'],
        tipo=row['tipo'],
        origen=row['origen']
    )
    session.add(saludo)

# confirmar transacciones
session.commit()