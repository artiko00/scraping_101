from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Galleta(Base):
    __tablename__ = 'galletas'
    identificador = Column(Integer(), primary_key=True)
    nombre = Column(String(), index=True)