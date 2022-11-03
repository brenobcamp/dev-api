from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    return jsonify({'nome': 'breno',
                    'profissao': 'desenvolvedor'})

# @app.route("/soma/<int:valor1>/<int:valor2>")
# def soma(valor1, valor2):
#     return jsonify({"Soma": valor1 + valor2})

@app.route("/soma", methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'Soma': total})

if __name__ == '__main__':
    app.run(debug=True)