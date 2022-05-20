# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
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

# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".

paises_C = session.query(Cosax).filter(Cosax.nombrepais=="uador").all()
print(paises_C)
