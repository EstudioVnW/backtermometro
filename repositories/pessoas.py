from sqlalchemy import Column, Integer, String, Boolean
from repositories.base import Base
from sqlalchemy.orm import relationship

class Pessoa(Base):
	__tablename__ = 'pessoas'

	id_pessoas = Column(Integer, primary_key=True)
	nome = Column(String)
	fl_professor = Column(Boolean)

	def to_json(self):
		return {
			'id_pessoas': self.id_pessoas,
			'nome': self.nome,
			'fl_professor': self.fl_professor
		}

class AllPessoas():

	def __init__(self, session):
		self.session = session

	def create(self, nome, fl_professor):
		nova_pessoa = Pessoa()
		nova_pessoa.nome = nome
		nova_pessoa.fl_professor = fl_professor
		
		try:
			self.session.add(nova_pessoa)
			self.session.commit()
			return nova_pessoa.to_json()
		except:
			self.session.rollback()
			raise

	def readAll(self):
		pessoas = self.session.query(Pessoa).all()
		nova_lista = []
		for pessoa in pessoas:
			nova_lista.append(pessoa.to_json())
		return nova_lista

	def read(self, id):
		pessoa = self.session.query(Pessoa).filter_by(id_pessoas = id).first()
		return pessoa.to_json() if pessoa else None

	def update(self, id_pessoas, nome, fl_professor):
		try:
			pessoa = self.session.query(Pessoa).filter_by(id_pessoas = id_pessoas).first()
			if not pessoa:
				return None
			pessoa.nome = nome
			pessoa.fl_professor = fl_professor
			self.session.commit()
			return pessoa.to_json()
		except:
			self.session.rollback()
			raise

	def delete(self, id_pessoas):
		try:
			pessoa = self.session.query(Pessoa).filter_by(id_pessoas = id_pessoas).first()
			if not pessoa:
				return None
			self.session.delete(pessoa)
			self.session.commit()
			return {
				'mensagem': 'Pessoa apagada com sucesso!'
			}
		except:
			self.session.rollback()
			raise