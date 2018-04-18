from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from aulas import Aula

Base = declarative_base()

class Duvida(Base):
	__tablename__ = 'duvidas'

	id_duvidas = Column(Integer, primary_key=True)
	duvida = Column(String)
	legenda = Column(String)
	aulas_id_aulas = Column(Integer, ForeignKey('aulas.id_aulas'))


class AllDuvidas():
	
	def __init__(self, session):
		self.session = session

	def create(self, duvida, legenda, aulas_id_aulas):
		nova_duvida = Duvida()
		nova_duvida.duvida = duvida
		nova_duvida.legenda = legenda
		nova_duvida.aulas_id_aulas = aulas_id_aulas
		self.session.add(nova_duvida)
		self.session.commit()

	def read(self, id):
		duvida = self.session.query(Duvida).filter_by(id_duvidas = id).first()
		return duvida
