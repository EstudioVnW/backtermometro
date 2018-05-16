from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pessoas import AllPessoas
from aulas import AllAulas
from avaliacoes import AllAvaliacoes
from duvidas import AllDuvidas
from polos import AllPolos
from turmas import AllTurmas
from flask import Flask, jsonify, request

engine = create_engine('mysql+pymysql://root:estudiovainaweb@localhost:3306/termometro')

Session = sessionmaker(bind=engine)

session = Session()

app = Flask(__name__)

all_pessoas = AllPessoas(session)
all_polos = AllPolos(session)

@app.route("/pessoas", methods=['GET'])
def get_all_pessoas():
    pessoas = all_pessoas.readAll()
    return jsonify(pessoas)

@app.route("/pessoas", methods=['POST'])
def criar_pessoa():
    json = request.get_json()
    try:
        nova_pessoa = all_pessoas.create(json['nome'], json['fl_professor'])
        return jsonify(nova_pessoa), 201
    except Exception as exc:
        return exc, 500

@app.route("/pessoas/<int:id>", methods=['GET'])
def get_pessoa(id):
    pessoa = all_pessoas.read(id)
    if pessoa:
        return jsonify(pessoa), 200
    else:
        return 'Pessoa não encontrada', 404

@app.route("/pessoas/<int:id>", methods=['PUT'])
def update_pessoa(id):
    json = request.get_json()
    try:
        pessoa_atualizada = all_pessoas.update(id, json['nome'], json['fl_professor'])
        if pessoa_atualizada:
            return jsonify(pessoa_atualizada), 200
        else:
            return 'Pessoa não encontrada', 404
    except Exception as exc:
        return exc, 500

@app.route("/pessoas/<int:id>", methods=['DELETE'])
def delete_pessoa(id):
    try:
        mensagem = all_pessoas.delete(id)
        if mensagem:
            return jsonify(mensagem), 200
        else:
            return 'Pessoa não encontrada', 404
    except Exception as exc:
        return exc, 500







@app.route("/polos", methods=['GET'])
def get_all_polos():
    polos = all_polos.readAll()
    return jsonify(polos)

@app.route("/polos", methods=['POST'])
def criar_polo():
    json = request.get_json()
    try:
        nova_polo = all_polos.create(json['nome'])
        return jsonify(nova_polo), 201
    except Exception as exc:
        return exc, 500

@app.route("/polos/<int:id>", methods=['GET'])
def get_polo(id):
    polo = all_polos.read(id)
    if polo:
        return jsonify(polo), 200
    else:
        return 'Polo não encontrada', 404

@app.route("/polos/<int:id>", methods=['PUT'])
def update_polo(id):
    json = request.get_json()
    try:
        polo_atualizada = all_polos.update(id, json['nome'])
        if polo_atualizada:
            return jsonify(polo_atualizada), 200
        else:
            return 'Polo não encontrada', 404
    except Exception as exc:
        return exc, 500

@app.route("/polos/<int:id>", methods=['DELETE'])
def delete_polo(id):
    try:
        mensagem = all_polos.delete(id)
        if mensagem:
            return jsonify(mensagem), 200
        else:
            return 'Polo não encontrada', 404
    except Exception as exc:
        return exc, 500

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# pessoas = AllPessoas(session)
# pessoas.create('Evy', True) 

# pessoa = AllPessoas(session)
# pessoa.update(26, 'Evelyn', True)

# pessoa = AllPessoas(session)
# pessoa.delete(27)


# duvidas = AllDuvidas(session)
# duvidas.create('Não entendi como almentar o tamanho', '', 1)

# duvida = AllDuvidas(session)
# duvida.create('', '2', 1)


# aulas = AllAulas(session)
# aulas.create('HTML10', 'Add a imagem e Alterando os tamanho da imagem', '2018-04-18', 1, 1, 1)

# aulas = AllAulas(session)
# aulas.update(7, 'Html5 e Css3', 'Começando Html5 semantica, Css3 tamanho, fonte e cores', '2018-01-25', 6, 3, 2)


# polos = AllPolos(session)
# polos.create('Escondidinho')

# polos = AllPolos(session)
# polos.update(6, 'Prazeres')

# polos = AllPolos(session)
# polos.delete(6)



# avaliacao = AllAvaliacoes(session)
# avaliacao.create(4, 'Não entrou na minha cabeça a parte do css', 1)



# turma = AllTurmas(session)
# turma.create('Maria', 1, 'Manhã', '2018-05-13','2018-10-13',  1)

# turma = AllTurmas(session)
# turma.update(11, 'Marcio', 1, 'Manhã', '2018-05-13','2018-10-13',  1)





