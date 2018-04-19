from sqlalchemy import Column, Integer, String, Date, ForeignKey
from base import Base
from turmas import Turma
from polos import Polo
from pessoas import Pessoa

class Aula(Base):
	__tablename__ = 'aulas'

	id_aulas = Column(Integer, primary_key=True)
	tema = Column(String)
	descricao = Column(String)
	data = Column(Date)
	turmas_id_turmas = Column(Integer, ForeignKey('turmas.id_turmas'))
	polos_id_polos =  Column(Integer, ForeignKey('polos.id_polos'))
	id_professor = Column(Integer, ForeignKey('pessoas.id_pessoas'))



class AllAulas():
	
	def __init__(self, session):
		self.session = session

	def create(self, tema, descricao, data, turmas_id_turmas, polos_id_polos, pessoas_id_pessoas):
		nova_aula = Aula()
		nova_aula.tema = tema
		nova_aula.descricao = descricao
		nova_aula.data = data
		nova_aula.turmas_id_turmas = turmas_id_turmas
		nova_aula.polos_id_polos= polos_id_polos
		nova_aula.id_professor = pessoas_id_pessoas
		self.session.add(nova_aula)
		self.session.commit()

	def read(self, id_aulas):
		aula = self.session.query(Aula).filter_by(id_aulas = id_aulas).first()
		return aula

	def update(self, id_aulas, tema, descricao, data, turmas_id_turmas, polos_id_polos, pessoas_id_pessoas):
		aula = self.session.query(Aula).filter_by(id_aulas = id_aulas).first()
		aula.tema = tema
		aula.descricao = descricao
		aula.data = data
		aula.turmas_id_turmas = turmas_id_turmas
		aula.polos_id_polos = polos_id_polos
		aula.id_professor = pessoas_id_pessoas
		self.session.commit()
