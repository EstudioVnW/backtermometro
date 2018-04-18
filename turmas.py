from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Turma(Base):
	__tablename__ = 'turmas'

	id_turmas = Column(Integer, primary_key=True)
	alunos_turma = Column(String)
	modulo = Column(Integer)
	turno = Column(String)
	data_inicial = Column(Date)
	data_final = Column(Date)
	polos_id_polos = Column(Integer, ForeignKey('polos.id_polos'))


class AllTurmas():
	
	def __init__(self, session):
		self.session = session

	def create(self, alunos_turma, modulo, turno, data_inicial, data_final, polos_id_polos):
		nova_turma = Turma()
		nova_turma.alunos_turma = alunos_turma
		nova_turma.modulo = modulo
		nova_turma.turno = turno
		nova_turma.data_inicial = data_inicial
		nova_turma.data_final = data_final
		nova_turma.polos_id_polos = polos_id_polos
		self.session.add(nova_turma)
		self.session.commit()

	def read(self, id):
		turma = self.session.query(Turma).filter_by(id_turmas = id).first()
		return turma

	def update(self, id_turmas, alunos_turma, modulo, turno, data_inicial, data_final, polos_id_polos):
		turma = self.session.query(Turma).filter_by(id_turmas = id_turmas).first()
		nova_turma.alunos_turma = alunos_turma
		nova_turma.modulo = modulo
		nova_turma.turno = turno
		nova_turma.data_inicial = data_inicial
		nova_turma.data_final = data_final
		nova_turma.polos_id_polos = polos_id_polos
		self.session.commit()

	def delete(self, id_turmas):
		turma = self.session.query(Turma).filter_by(id_turmas = id_turmas).first()
		self.session.delete(turma)
		self.session.commit()
