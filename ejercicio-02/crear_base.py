from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Paises(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombrePais = Column(String)
    Capital = Column(String)
    Continente = Column(String)
    Dial = Column(String)
    GeonameID = Column(String)
    Itu = Column(String)
    Lenguajes = Column(String)
    Dependecia = Column(String)



Base.metadata.create_all(engine)