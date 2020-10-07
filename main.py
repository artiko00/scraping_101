import requests
from bs4 import BeautifulSoup
import re

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from galletas import Galleta, Base

engine = create_engine('sqlite:///galletas.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

pagina = requests.get('https://es.wikipedia.org/wiki/Galleta')

if pagina.status_code == 200:
    soup = BeautifulSoup(pagina.text, 'html.parser')
    for link in soup.find_all('a'):
        txt = link.get_text()
        x = re.search("[Gg]alleta", txt)
        if x:
            una_galleta = Galleta()
            una_galleta.nombre = txt
            session.add(una_galleta)
    session.commit()
