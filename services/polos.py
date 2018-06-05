from flask_restplus import Resource
from app import api, session
from repositories.polos import AllPolos
from flask import jsonify

all_polos = AllPolos(session)

@api.route('/polos')
class AllPoloResource(Resource):
	def get(self):
		polos = all_polos.readAll()
		return jsonify(polos)


	def post(self):
		json = request.get_json()
		try: 
			new_polo = all_polos.create(json['nome'])
			new_polo = jsonify(new_polo)
			new_polo.status_code = 201
			return new_polo
		except Exception as exc:
			return exc, 500

@api.route('/polos/<int:id_polos>')
class PoloResource(Resource):
	def get(self, id_polos):
		polo = all_polos.read(id_polos)
		if polo:
			return jsonify(polo)
		else:
			return 'Polo não encontrado', 404

	def put(self, id_polos):
		json = request.get_json()
		try:
			polo_updated = all_polos.update(id_polos, json['nome'])
			if polo_updated:
				return jsonify(polo_updated)
			else:
				return 'Polo não encontrado', 404
		except Exception as exc:
			return exc, 500

	def delete(self, id_polos):
		try:
			message = all_polos.delete(id_polos)
			if message:
				return jsonify(message)
			else:
				return 'Polo não encontrado', 404
		except Exception as exc:
			return exc, 500