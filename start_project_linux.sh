#!/bin/bash

# Verificar se o ambiente virtual já existe
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
    echo "Ambiente virtual criado."
fi

# Ativar o ambiente virtual
echo "Ativando o ambiente virtual..."
source venv/bin/activate

# Instalar as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Configurar as variáveis de ambiente do Flask
export FLASK_APP=app.py
export FLASK_ENV=development

# Iniciar o servidor Flask
echo "Iniciando o servidor Flask..."
flask run

# Desativar o ambiente virtual após a execução
deactivate
