from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base
from aulas import Aula

class Avaliacao(Base):
	__tablename__ = 'avaliacoes'

	id_avaliacoes = Column(Integer, primary_key=True)
	nota = Column(Integer)
	avaliacao = Column(String)
	aulas_id_aulas = Column(Integer, ForeignKey('aulas.id_aulas'))

	def to_json(self):
		return {
			'id_avaliacoes': self.id_avaliacoes,
			'nota': self.nota,
			'avaliacao': self.avaliacao,
			'aulas_id_aulas': self.aulas_id_aulas
		}


class AllAvaliacoes():
	
	def __init__(self, session):
		self.session = session

	def create(self, nota, avaliacao, aulas_id_aulas):
		new_evaluation= Avaliacao()
		new_evaluation.nota = nota
		new_evaluation.avaliacao = avaliacao
		new_evaluation.aulas_id_aulas = aulas_id_aulas

		try:
			self.session.add(new_evaluation)
			self.session.commit()
			return new_evaluation.to_json()
		except:
			self.session.rollback()
			raise

	def readAll(self):
		avaliacoes = self.session.query(Avaliacao).all()
		new_evaluation = []
		for avaliacao in avaliacoes:
			new_evaluation.append(avaliacao.to_json())
		return new_evaluation


	def read(self, id):
		avaliacao = self.session.query(Avaliacao).filter_by(id_avaliacaos = id).first()
		return avaliacao.to_json() if avaliacao else None

	def update(self, id_avaliacoes, nota, avaliacao, aulas_id_aulas):
		try:
			updated = self.session.query(Avaliacao).filter_by(id_avaliacoes = id_avaliacoes).first()
			if not updated:
				return None
			updated.nota = nota
			updated.avaliacao = avaliacao
			updated.aulas_id_aulas = aulas_id_aulas
			self.session.commit()
			return updated.to_json()
		except:
			self.session.rollback()
			raise

	def delete(self, id_avaliacoes):
		try:
			avaliacao = self.session.query(Avaliacao).filter_by(id_avaliacoes = id_avaliacoes).first()
			if not avaliacao:
				return None
			self.session.delete(avaliacao)
			self.session.commit()
			return {
				'message': 'Avaliacao apagada com sucesso!'
			}
		except:
			self.session.rollback()
			raise


