from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pessoas import AllPessoas
from aulas import AllAulas
from avaliacoes import AllAvaliacoes
from duvidas import AllDuvidas
from polos import AllPolos
from turmas import AllTurmas

engine = create_engine('mysql+pymysql://root:estudiovainaweb@localhost:3306/termometro')


Session = sessionmaker(bind=engine)

session = Session()

# pessoas = AllPessoas(session)
# pessoas.create('Juliana', True) 

# pessoa = AllPessoas(session)
# pessoa.update(24, 'Gisele', True)

# pessoa = AllPessoas(session)
# pessoa.delete(24)


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





