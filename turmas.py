from sqlalchemy import Column, Integer, String, Date, ForeignKey
from base import Base
from polos import Polo

class Turma(Base):
	__tablename__ = 'turmas'

	id_turmas = Column(Integer, primary_key=True)
	alunos_turma = Column(String)
	modulo = Column(Integer)
	turno = Column(String)
	data_inicial = Column(Date)
	data_final = Column(Date)
	id_polos = Column(Integer, ForeignKey('polos.id_polos'))

	def to_json(self):
		return {
			'id_turmas': self.id_turmas,
			'alunos_turma': self.alunos_turma,
			'modulo': self.modulo,
			'turno': self.turno,
			'data_inicial': self.data_inicial,
			'data_final': self.data_final,
			'id_polos': self.id_polos
		}


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
		nova_turma.id_polos = polos_id_polos

		try:			
			self.session.add(nova_turma)
			self.session.commit()
			return nova_turma.to_jason()
		except:
			self.session.rollback()
			raise

	def readAll(self):
		turmas = self.session.query(Turma).all()
		nova_lista = []
		for turma in turmas:
			nova_lista.append(turma.to_json())
		return nova_lista

	def read(self, id):
		turma = self.session.query(Turma).filter_by(id_turmas = id).first()
		return turma.to_json() if turma else None

	def update(self, id_turmas, alunos_turma, modulo, turno, data_inicial, data_final, polos_id_polos):
		try:
			turma = self.session.query(Turma).filter_by(id_turmas = id_turmas).first()
			if not turma:
				return None
			turma.nome = nome
			turma.alunos_turma = alunos_turma
			turma.modulo = modulo
			turma.turno = turno
			turma.data_inicial = data_inicial
			turma.data_final = data_final
			turma.id_polos = polos_id_polos
			self.session.commit()
			return turma.to_json()
		except:
			self.session.rollback()
			raise

	def delete(self, id_turmas):
		try:
			turma = self.session.query(Turma).filter_by(id_turmas = id_turmas).first()
			if not turma:
				return None
			self.session.delete(turma)
			self.session.commit()
			return {
				'mensagem': 'Turma apagada com sucesso!'
			}
		except:
			self.session.rollback()
			raise
