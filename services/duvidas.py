from flask_restplus import Resource
from app import api, session
from repositories.duvidas import AllDuvidas
from flask import jsonify

all_duvidas = AllDuvidas(session)

@api.route('/duvidas')
class AllAskResource(Resource):
	def get(self):
		duvidas = all_duvidas.readAll()
		return jsonify(duvidas)

	def post(self):
		json = request.get_json()
		try:
			new_ask = all_duvidas.create(json['duvida'], json['legenda'], json['aulas_id_aulas'])
			new_ask = jsonify(new_ask)
			new_ask.status_code = 201
			return new_ask
		except Exception as exc:
			return exc, 500

@api.route('/duvidas/<int:id_duvidas>')
class AskResource(Resource):
	def get(self, id_duvidas):
		duvida = all_duvidas.read(id_duvidas)
		if duvida:
			return jsonify(duvida)
		else:
			return 'Duvida não encontrada', 404

	def put(self, id_duvidas):
		json = request.get_json()
		try:
			ask_updated = all_duvidas.update(id_duvidas, json['duvida'], json['legenda'], json['aulas_id_aulas'])
			if ask_updated:
				return jsonify(ask_updated)
			else:
				return 'Duvida não encontrada', 404
		except Exception as exc:
			return exc, 500

	def delete(self, id_duvidas):
		try: 
			message = all_duvidas.delete(id_duvidas)
			if message:
				return jsonify(message)
			else:
				return 'Dúvida não encontrada', 404
		except Exception as exc:
			return exc, 500