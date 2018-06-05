from flask_restplus import Resource
from app import api, session
from repositories.aulas import AllAulas
from flask import jsonify

all_aulas = AllAulas(session)

@api.route('/aulas')
class AllLessonResource(Resource):
	def get(self):
		aulas = all_aulas.readAll()
		return jsonify(aulas)

	def post(self):
		json = request.get_json()
		try:
			new_lesson = all_aulas.create(json['tema'], json['descricao'], json['data'], json['turmas_id_turmas'], json['polos_id_polos'], json['id_professor'])
			new_lesson = jsonify(new_lesson)
			new_lesson.status_code=201
			return new_lesson
		except Exception as exc:
			return exc, 500

@api.route('/aulas/<int:id_aulas>')
class LessonResource(Resource):
	def get(self, id_aulas):
		aula = all_aulas.read(id_aulas)
		if aula:
			return jsonify(aula)
		else:
			return 'Aula não encontrada', 404

	def put(self, id_aulas):
		json = request.get_json()
		try:
			aula_atualizada = all_aulas.update(id_aulas, json['tema'], json['descricao'], json['data'], json['turmas_id_turmas'], json['polos_id_polos'], json['id_professor'])
			if aula_atualizada:
				return jsonify(aula_atualizada)
			else:
				return 'Aula não encontrada', 404 
		except Exception as exc:
			return exc, 500