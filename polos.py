from sqlalchemy import Column, Integer, String
from base import Base

class Polo(Base):
	__tablename__ = 'polos'

	id_polos = Column(Integer, primary_key=True)
	nome = Column(String)


class AllPolos():

	def __init__(self, session):
		self.session = session

	def create(self, nome):
		nova_polo = Polo()
		nova_polo.nome = nome
		self.session.add(nova_polo)
		self.session.commit()

	def read(self, id):
		polo = self.session.query(Polo).filter_by(id_polos = id).first()
		return polo

	def update(self, id_polos, nome):
		polo = self.session.query(Polo).filter_by(id_polos = id_polos).first()
		polo.nome = nome
		self.session.commit()

	def delete(self, id_polos):
		polo = self.session.query(Polo).filter_by(id_polos = id_polos).first()
		self.session.delete(polo)
		self.session.commit()