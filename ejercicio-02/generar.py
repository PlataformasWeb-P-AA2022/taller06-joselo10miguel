
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Cosax
import requests
import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

cadena = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")


doc = cadena.json()


for d in doc:
    print(d)
    print(len(d.keys()))
    p = Cosax(nombrepais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geoname=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], dependiente=d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()
