from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Avaliacoes(Base):
	__tablename__ = 'avaliacoes'

	id_avaliacao = Column(Integer, primary_key=True)
	nota = Column(Integer)
	avaliacao = Column(String)
	aulas_id_aulas = Column(Integer, ForeignKey('aulas.id_aulas'))


class AllAvaliacoes():
	
	def __init__(self, session):
		self.session = session

	def create(self, nome, nota, avaliacao, aulas_id_aulas):
		nova_avaliacao = Avaliacao()
		nova_avaliacao.nota = nota
		nova_avaliacao.avaliacao = avaliacao
		nova_avaliacao.aulas_id_aulas = aulas_id_aulas
		self.session.add(nova_avaliacao)
		self.session.commit()

	def read(self, id):
		avaliacao = self.session.query(Avaliacao).filter_by(id_avaliacaos = id).first()
		return avaliacao
