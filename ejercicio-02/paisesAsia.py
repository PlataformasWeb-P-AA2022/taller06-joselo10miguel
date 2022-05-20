
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
# se importa el operador and
# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Cosax

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países de Asía, ordenados por el atributo Dial.
paises_A = session.query(Cosax).filter(Cosax.continente=="AS").order_by(Cosax.dial).all()
print(paises_A)

