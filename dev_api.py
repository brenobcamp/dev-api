import json
from flask import (Flask, request, jsonify)
from http import HTTPStatus

app = Flask(__name__)

desenvolvedores = [
    {'id': 0,
    'nome': 'Breno',
    'habilidades': ['Python', 'Flask']},
    {'id': 1,
    'nome': 'Rafael',
    'habilidades': ['Java', 'Spring']}
]

# Devolve um desenvolvedor pelo id
@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": HTTPStatus.NOT_FOUND}
        except Exception:
            response = {"status": HTTPStatus.INTERNAL_SERVER_ERROR, "mensagem": "Erro descohecido. Contate o admin"}
       
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify({"status": HTTPStatus.ACCEPTED,
                        "requisição": dados})
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status": HTTPStatus.OK, "mensagem": "Registro excluído"})

# Devolve todos os desenvolvedores
@app.route("/dev/", methods=['GET', 'POST'])
def listar_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return jsonify({"status": HTTPStatus.OK, "mensagem": "Registro inserido", "registro": desenvolvedores[posicao]})

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)