from flask import Flask, request, jsonify, abort


app = Flask(__name__)

TAXA_DEBITO = 0.03
TAXA_CREDITO = 0.05
TAXA_PIX = 0.0

contas = {}

@app.route('/conta', methods=['GET'])
def consultar_conta():
    numero_conta = request.args.get('numero_conta')

    # Verificar se a conta existe
    if numero_conta not in contas:
        return jsonify({"message": "Conta não encontrada."}), 404

    saldo = contas[numero_conta]["saldo"]
    return jsonify({"numero_conta": numero_conta, "saldo": saldo}), 200


@app.route('/conta', methods=['POST'])
def criar_conta():
    data = request.get_json()
    numero_conta = data.get('numero_conta')
    saldo = data.get('saldo')

    # Verificar se a conta já existe
    if numero_conta in contas:
        return jsonify({"message": "Conta já existe."}), 400

    # Criar nova conta
    contas[numero_conta] = {
        "saldo": saldo
    }

    return jsonify({"numero_conta": numero_conta, "saldo": saldo}), 201


@app.route('/transacao', methods=['POST'])
def realizar_transacao():
    data = request.get_json()
    forma_pagamento = data.get('forma_pagamento')
    numero_conta = data.get('numero_conta')
    valor = data.get('valor')

    # Verificar se a conta existe
    if numero_conta not in contas:
        return jsonify({"message": "Conta não encontrada."}), 404

    # Obter saldo atual
    saldo_atual = contas[numero_conta]["saldo"]

    # Calcular a taxa
    if forma_pagamento == "D":
        taxa = valor * TAXA_DEBITO
    elif forma_pagamento == "C":
        taxa = valor * TAXA_CREDITO
    elif forma_pagamento == "P":
        taxa = TAXA_PIX
    else:
        return jsonify({"message": "Forma de pagamento inválida."}), 400

    total_a_pagar = valor + taxa

    # Verificar se o saldo é suficiente
    if saldo_atual < total_a_pagar:
        return jsonify({"message": "Saldo insuficiente."}), 404

    # Realizar a transação
    contas[numero_conta]["saldo"] -= total_a_pagar

    return jsonify({"numero_conta": numero_conta, "saldo": contas[numero_conta]["saldo"]}), 201

