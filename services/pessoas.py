from flask_restplus import Resource
from app import api, session
from repositories.pessoas import AllPessoas
from flask import jsonify

all_pessoas = AllPessoas(session)

@api.route('/pessoas')
class AllPeopleResource(Resource):
    def get(self):
        pessoas = all_pessoas.readAll()
        return jsonify(pessoas)

    def post(self):
        json = request.get_json()
        try:
            new_pessoa = all_pessoas.create(json['nome'], json['fl_professor'])
            new_pessoa = jsonify(new_pessoa)
            new_pessoa.status_code=201
            return new_pessoa
        except Exception as exc:
            return exc, 500

@api.route('/pessoas/<int:id_pessoas>')
class PeopleResource(Resource):
    def get(self, id_pessoas):
        pessoa = all_pessoas.read(id_pessoas)
        if pessoa:
            return jsonify(pessoa)
        else:
            return 'Pessoa não encontrada', 404

    def put(self, id_pessoas):
        json = request.get_json()
        try:
            pessoa_updated = all_pessoas.update(id_pessoas, json['nome'], json['fl_professor'])
            if pessoa_updated:
                return jsonify(pessoa_updated)
            else:
                return 'Pessoa não encontrada', 404
        except Exception as exc:
            return exc, 500

    def delete(self, id_pessoas):
        try:
            message = all_pessoas.delete(id_pessoas)
            if message:
                return jsonify(message)
            else:
                return 'Pessoa não encontrada', 404
        except Exception as exc:
            return exc, 500