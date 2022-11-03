from flask_restful import Resource
from flask import request
from json import loads
from http import HTTPStatus

habilidades = ['Python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return habilidades
    def post(self):
        dados = request.data
        habilidades.append(dados)
        return {'status': HTTPStatus.OK}
    def put(self, id):
        dados = request.data
        habilidades[id] = dados
        return {'status': HTTPStatus.OK}
    def delete(self, id):
        habilidades[id].pop()
        return {'status': HTTPStatus.OK}