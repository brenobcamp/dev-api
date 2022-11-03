from flask import (Flask, request)
from flask_restful import (Resource, Api)
from http import HTTPStatus
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': 0,
    'nome': 'Breno',
    'habilidades': ['Python', 'Flask']},
    {'id': 1,
    'nome': 'Rafael',
    'habilidades': ['Java', 'Spring']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": HTTPStatus.NOT_FOUND}
        except Exception:
            response = {"status": HTTPStatus.INTERNAL_SERVER_ERROR, "mensagem": "Erro descohecido. Contate o admin"}
       
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return {"status": HTTPStatus.ACCEPTED, "requisição": dados}

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": HTTPStatus.OK, "mensagem": "Registro excluído"}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run()

