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

# duvidas = AllDuvidas(session)
# duvidas.create('Não entendi como almentar o tamanho', '', 1)

aulas = AllAulas(session)
aulas.create('CSS3', 'aprendendo as cores', '2018-04-18', 1, 1, 1)
