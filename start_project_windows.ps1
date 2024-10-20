# Verificar se o ambiente virtual já existe
if (-Not (Test-Path "venv")) {
    Write-Host "Criando ambiente virtual..."
    python -m venv venv
    Write-Host "Ambiente virtual criado."
}

# Ativar o ambiente virtual
Write-Host "Ativando o ambiente virtual..."
venv\Scripts\Activate

# Instalar as dependências
Write-Host "Instalando dependências..."
pip install -r requirements.txt

# Configurar as variáveis de ambiente do Flask
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# Iniciar o servidor Flask
Write-Host "Iniciando o servidor Flask..."
flask run

# Desativar o ambiente virtual após a execução
deactivate
