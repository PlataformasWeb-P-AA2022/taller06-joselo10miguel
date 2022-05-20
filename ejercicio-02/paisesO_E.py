
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
# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
paises_Ca = session.query(Cosax).filter(Cosax.continente=="EU").order_by(Cosax.capital).all()
print(paises_Ca)
