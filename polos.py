from sqlalchemy import Column, Integer, String
from base import Base

class Polo(Base):
	__tablename__ = 'polos'

	id_polos = Column(Integer, primary_key=True)
	nome = Column(String)

	def to_json(self):
		return {
			'id_polos': self.id_polos,
			'nome': self.nome
		}

class AllPolos():

	def __init__(self, session):
		self.session = session

	def create(self, nome):
		new_polo = Polo()
		new_polo.nome = nome


		try:
			self.session.add(new_polo)
			self.session.commit()
			return new_polo.to_json()
		except:
			self.session.rollback()
			raise

	def readAll(self):
		polos = self.session.query(Polo).all()
		new_list = []
		for polo in polos:
			new_list.append(polo.to_json())
		return new_list

	def read(self, id):
		polo = self.session.query(Polo).filter_by(id_polos = id).first()
		return polo.to_json() if polo else None

	def update(self, id_polos, nome):
		try:
			polo = self.session.query(Polo).filter_by(id_polos = id_polos).first()
			if not polo:
				return None
			polo.nome = nome
			self.session.commit()
			return polo.to_json()
		except:
			self.session.rollback()
			raise

	def delete(self, id_polos):
		try:
			polo = self.session.query(Polo).filter_by(id_polos = id_polos).first()
			if not polo:
				return None
			self.session.delete(polo)
			self.session.commit()
			return{
				'message': 'Polo apagado com sucesso'
			}
		except:
			self.session.rollback()
			raise