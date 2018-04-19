from sqlalchemy import Column, Integer, String, Boolean
from base import Base
from sqlalchemy.orm import relationship


class Pessoa(Base):
	__tablename__ = 'pessoas'

	id_pessoas = Column(Integer, primary_key=True)
	nome = Column(String)
	fl_professor = Column(Boolean)

class AllPessoas():

	def __init__(self, session):
		self.session = session

	def create(self, nome, fl_professor):
		nova_pessoa = Pessoa()
		nova_pessoa.nome = nome
		nova_pessoa.fl_professor = fl_professor
		self.session.add(nova_pessoa)
		self.session.commit()

	def read(self, id):
		pessoa = self.session.query(Pessoa).filter_by(id_pessoas = id).first()
		return pessoa

	def update(self, id_pessoas, nome, fl_professor):
		pessoa = self.session.query(Pessoa).filter_by(id_pessoas = id_pessoas).first()
		pessoa.nome = nome
		pessoa.fl_professor = fl_professor
		self.session.commit()

	def delete(self, id_pessoas):
		pessoa = self.session.query(Pessoa).filter_by(id_pessoas = id_pessoas).first()
		self.session.delete(pessoa)
		self.session.commit()