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
		new_doubt = Duvida()
		new_doubt.duvida = duvida
		new_doubt.legenda = legenda
		new_doubt.aulas_id_aulas = aulas_id_aulas

		try:
			self.session.add(new_doubt)
			self.session.commit()
			return new_doubt.to_json()
		except:
			self.session.rollback()
			raise

	def readAll(self):
		duvidas = self.session.query(Duvida).all()
		new_legend= []
		for duvida in duvidas:
			new_legend.append(duvida.to_json())
		return new_legend	

	def read(self, id):
		duvida = self.session.query(Duvida).filter_by(id_duvidas = id).first()
		return duvida.to_json() if duvida else None

	def update(self, id_duvidas, duvida, legenda, aulas_id_aulas):
		try:
			update = self.session.query(Duvida).filter_by(id_duvidas = id_duvidas).first()
			if not update:
				return None
			update.duvida = duvida	
			update.legenda = legenda
			update.aulas_id_aulas = aulas_id_aulas
			self.session.commit()
			return update.to_json()
		except:
			self.session.rollback()
			raise
	
	def delete(self, id_duvidas):
		try:
			duvida = self.session.query(Duvida).filter_by(id_duvidas = id_duvidas).first()
			if not duvida:
				return None
			self.session.delete(duvida)
			self.session.commit()
			return {
				'message': 'Duvida apagada com sucesso!'
			}
		except:
			self.session.rollback()
			raise










