from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base
from aulas import Aula

class Avaliacoes(Base):
	__tablename__ = 'avaliacoes'

	id_avaliacao = Column(Integer, primary_key=True)
	nota = Column(Integer)
	avaliacao = Column(String)
	aulas_id_aulas = Column(Integer, ForeignKey('aulas.id_aulas'))


class AllAvaliacoes():
	
	def __init__(self, session):
		self.session = session

	def create(self, nota, avaliacao, aulas_id_aulas):
		nova_avaliacao = Avaliacoes()
		nova_avaliacao.nota = nota
		nova_avaliacao.avaliacao = avaliacao
		nova_avaliacao.aulas_id_aulas = aulas_id_aulas
		self.session.add(nova_avaliacao)
		self.session.commit()

	def read(self, id):
		avaliacao = self.session.query(Avaliacoes).filter_by(id_avaliacaos = id).first()
		return avaliacao
