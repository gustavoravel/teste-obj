from flask import Flask, request, jsonify, abort

from database import db
from models import Conta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

TAXA_DEBITO = 0.03
TAXA_CREDITO = 0.05
TAXA_PIX = 0.0


@app.route('/conta', methods=['GET'])
def consultar_conta():
    numero_conta_str = request.args.get('numero_conta')

    if numero_conta_str is None:
        return jsonify({"message": "Número da conta não fornecido."}), 400

    try:
        numero_conta = int(numero_conta_str)
    except ValueError:
        return jsonify({"message": "Número da conta deve ser um inteiro."}), 400

    conta = Conta.query.get(numero_conta)
    
    if conta is None:
        return jsonify({"message": "Conta não encontrada."}), 404

    return jsonify({"numero_conta": conta.numero_conta, "saldo": conta.saldo}), 200


@app.route('/conta', methods=['POST'])
def criar_conta():
    data = request.get_json()
    numero_conta = data.get('numero_conta')
    saldo = data.get('saldo')

    if Conta.query.get(numero_conta):
        return jsonify({"message": "Conta já existe."}), 400

    nova_conta = Conta(numero_conta=numero_conta, saldo=saldo)
    db.session.add(nova_conta)
    db.session.commit()

    return jsonify(nova_conta.to_dict()), 201


@app.route('/transacao', methods=['POST'])
def realizar_transacao():
    data = request.get_json()
    forma_pagamento = data.get('forma_pagamento')
    numero_conta = data.get('numero_conta')
    valor = data.get('valor')

    conta = Conta.query.get(numero_conta)
    if conta is None:
        return jsonify({"message": "Conta não encontrada."}), 404

    taxa = 0
    if forma_pagamento == 'D':
        taxa = 0.03 * valor
    elif forma_pagamento == 'C':
        taxa = 0.05 * valor

    valor_total = valor + taxa

    if conta.saldo < valor_total:
        return jsonify({"message": "Saldo insuficiente."}), 404

    conta.saldo -= valor_total
    db.session.commit()

    return jsonify(conta.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)