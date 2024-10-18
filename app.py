from flask import Flask, request, jsonify, abort


app = Flask(__name__)

TAXA_DEBITO = 0.03
TAXA_CREDITO = 0.05

contas = {}

@app.route('/conta', methods=['GET'])
def consultar_conta():
    pass


@app.route('/conta', methods=['POST'])
def criar_conta():
    pass


@app.route('/transacao', methods=['POST'])
def realizar_transacao():
    pass
