from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base
from aulas import Aula

class Duvida(Base):
	__tablename__ = 'duvidas'

	id_duvidas = Column(Integer, primary_key=True)
	duvida = Column(String)
	legenda = Column(String)
	aulas_id_aulas = Column(Integer, ForeignKey('aulas.id_aulas'))
	
	def to_json(self):
			return {
				'id_duvidas': self.id_duvidas,
				'duvida': self.duvida,
				'legenda': self.legenda,
				'aulas_id_aulas': self.aulas_id_aulas
			}

class AllDuvidas():
	
	def __init__(self, session):
		self.session = session

	def create(self, duvida, legenda, aulas_id_aulas):
		nova_duvida = Duvida()
		nova_duvida.duvida = duvida
		nova_duvida.legenda = legenda
		nova_duvida.aulas_id_aulas = aulas_id_aulas

		try:
			self.session.add(nova_duvida)
			self.session.commit()
			return nova_duvida.to_json()
		except:
			self.session.rollback()
			raise

	def readAll(self):
		duvidas = self.session.query(Duvida).all()
		nova_legenda = []
		for duvida in duvidas:
			nova_legenda.append(duvida.to_json())
		return nova_legenda	

	def read(self, id):
		duvida = self.session.query(Duvida).filter_by(id_duvidas = id).first()
		return duvida.to_json() if duvida else None

	def update(self, id_duvidas, duvida, legenda, aulas_id_aulas):
		try:
			duvida = self.session.query(Duvida).filter_by(id_duvidas = id_duvidas).first()
			if not duvida:
				return None
			duvida.duvida = duvida	
			duvida.legenda = legenda
			duvida.aulas_id_aulas = aulas_id_aulas
			self.session.commit()
			return duvida.to_json()
		except:
			self.session.rollback()
			raise











