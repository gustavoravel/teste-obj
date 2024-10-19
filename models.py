from database import db

class Conta(db.Model):
    __tablename__ = 'contas'

    numero_conta = db.Column(db.Integer, primary_key=True)
    saldo = db.Column(db.Float, nullable=False)

    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def to_dict(self):
        return {
            "numero_conta": self.numero_conta,
            "saldo": self.saldo
        }
