from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask_restplus import Api

engine = create_engine('mysql+pymysql://root:estudiovainaweb@localhost:3306/termometro')

Session = sessionmaker(bind=engine)

session = Session()

app = Flask(__name__)
api = Api(app)


# , apidoc
# @api.documentation
# def custom_ui():
#     return apidoc.ui_for(api)