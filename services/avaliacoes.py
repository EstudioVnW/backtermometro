from flask_restplus import Resource
from app import api, session
from repositories.avaliacoes import AllAvaliacoes
from flask import jsonify

all_avaliacoes = AllAvaliacoes(session)

@api.route('/avaliacoes')
class AllEvaluationResource(Resource):
	def get(self):
		avaliacoes = all_avaliacoes.readAll()
		return jsonify(avaliacoes)

	def post(self):
		json = request.get_json()
		try:
			new_evaluation = all_avaliacoes.create(json['nota'], json['avaliacao'], json['aulas_id_aulas'])
			new_evaluation = jsonify(new_evaluation)
			new_evaluation.status_code=201
			return new_avaliacao
		except Exception as exc:
			return exc, 500

@api.route('/avaliacoes/<int:id_aulas>')
class EvaluationResource(Resource):
	def get(self, id_avaliacoes):
		avaliacao = all_avaliacoes.read(id_avaliacoes)
		if avaliacao:
			return jsonify(avaliacao)
		else:
			return 'Avaliacao não encontrada', 404

	def put(self, id_avaliacoes):
		json = request.get_json()
		try:
			evaluation_updated = all_avaliacoes.update(id_avaliacoes, json['nota'], json['avaliacao'], json['aulas_id_aulas'])
			if evaluation_updated:
				return jsonify(evaluation_updated)
			else:
				return 'Avaliação não encontrada', 404
		except Exception as exc:
			return exc, 500

	def delete(self, id_avaliacoes):
		try:
			message = all_avaliacoes.delete(id_avaliacoes)
			if message:
				return jsonify(message)
			else:
				return 'Avaliação não encontrada', 404
		except Exception as exc:
			return exc, 500