from flask_restplus import Resource
from app import api, session
from repositories.turmas import AllTurmas
from flask import jsonify

all_turmas = AllTurmas(session)

@api.route('/turmas')
class AllClassResource(Resource):
	def get(self):
		turmas = all_turmas.readAll()
		return jsonify(turmas)

	def post(self):
		json = request.get_json()
		try:
			new_class = all_turmas.create(json['alunos_turma'], json['modulo'], json['turno'], json['data_inicial'], json['data_final'], json['id_polos'])
			new_class = jsonify(new_class)
			new_class.status_code = 201
			return new_class
		except Exception as exc:
			return exc, 500

@api.route('/turmas/<int:id_turmas>')
class ClassResource(Resource):
	def get(self, id_turmas):
		turma = all_turmas.read(id_turmas)
		if turma:
			return jsonify(turma)
		else:
			return 'Turma não encontrada', 404

	def put(self, id_turmas):
		json = request.get_json()
		try:
			class_updated = all_turmas.update(id_turmas, json['alunos_turma'], json['modulo'], json['turno'], json['data_inicial'], json['data_final'], json['id_polos'])
			if class_updated:
				return jsonify(class_updated)
			else:
				return 'Turma não encontrada', 404
		except Exception as exc:
			return exc, 500