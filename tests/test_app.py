import unittest
import json

from app import app

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_criar_conta(self):
        # criação conta
        response = self.app.post('/conta', json={
            "numero_conta": 2345,
            "saldo": 180.37
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"numero_conta": 2345, "saldo": 180.37})

    def test_consultar_conta_existente(self):
        # consulta conta existente
        response = self.app.get('/conta?numero_conta=234')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"numero_conta": 2345, "saldo": 180.37})

    def test_consultar_conta_inexistente(self):
        # consulta conta não existente
        response = self.app.get('/conta?numero_conta=476532')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Conta não encontrada."})

    def test_transacao_debito(self):
        # transação de débito
        response = self.app.post('/transacao', json={
            "forma_pagamento": "D",
            "numero_conta": 2345,
            "valor": 10
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"numero_conta": 2345, "saldo": 170.07})

    def test_transacao_credito(self):
        # transação de crédito
        response = self.app.post('/transacao', json={
            "forma_pagamento": "C",
            "numero_conta": 2345,
            "valor": 10
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"numero_conta": 2345, "saldo": 165.07})

    def test_transacao_pix(self):
        # transação por Pix
        response = self.app.post('/transacao', json={
            "forma_pagamento": "P",
            "numero_conta": 2345,
            "valor": 10
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"numero_conta": 2345, "saldo": 155.07})

    def test_transacao_sem_saldo(self):
        # transação sem saldo
        response = self.app.post('/transacao', json={
            "forma_pagamento": "D",
            "numero_conta": 2345,
            "valor": 2
        })
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"message": "Saldo insuficiente."})

if __name__ == '__main__':
    unittest.main()
