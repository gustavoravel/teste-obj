# Desafio Técnico - Sistema de Gestão Bancária

Este repositório contém a implementação de um sistema de gestão bancária para um desafio técnico de uma vaga de programador. A aplicação foi desenvolvida utilizando Flask e SQLAlchemy, e permite a criação de contas bancárias e a realização de transações com controle de saldo.

## Descrição do Projeto

A aplicação consiste em uma API RESTful com os seguintes endpoints:

- **POST /conta**: Cria uma nova conta bancária com saldo inicial.
- **GET /conta?numero_conta=**: Consulta o saldo de uma conta bancária pelo número da conta.
- **POST /transacao**: Realiza uma transação de débito, crédito ou Pix, descontando a taxa correspondente e garantindo que não haja saldo negativo.

### Taxas de Transação
- **Débito (D)**: 3% sobre o valor da transação.
- **Crédito (C)**: 5% sobre o valor da transação.
- **Pix (P)**: Sem custo adicional.

### Requisitos

- Python 3.8 ou superior.
- Flask.
- SQLAlchemy.

## Estrutura do Projeto

```bash
.
├── app.py              # Arquivo principal da aplicação Flask.
├── database.py         # Configuração da conexão com o banco de dados.
├── models.py           # Definição dos modelos de dados (SQLAlchemy).
├── db.sqlite3          # Banco de dados SQLite (adicionado ao .gitignore).
├── start_project_linux.sh  # Script para iniciar a aplicação no Linux.
├── start_project_windows.ps1 # Script para iniciar a aplicação no Windows.
├── README.md           # Documentação da aplicação.
└── .gitignore          # Arquivos e pastas ignorados pelo Git.
```

## Instruções para Execução

### Clonando o Repositório

Primeiro, clone o repositório em sua máquina:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

### Configuração do Ambiente Virtual

Crie um ambiente virtual e ative-o:

```bash
# No Linux ou MacOS
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

### Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

> **Nota**: O arquivo `requirements.txt` deve conter as bibliotecas necessárias como `Flask` e `SQLAlchemy`.

### Configuração do Banco de Dados

Antes de rodar a aplicação, certifique-se de criar o banco de dados SQLite:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Executando a Aplicação

Para iniciar a aplicação Flask, execute:

```bash
# No Linux ou MacOS
sh start_project_linux.sh

# No Windows
start_project_windows.ps1
```

> Esses scripts executarão o comando `python app.py` para iniciar o servidor.

### Acessando a API

A aplicação estará disponível em `http://localhost:5000`. Você pode usar uma ferramenta como o Postman para testar os endpoints.

### Exemplos de Requisições

- **Criar Conta**
    - **POST** `http://localhost:5000/conta`
    - Corpo (JSON):
        ```json
        {
            "numero_conta": 123,
            "saldo": 1000.0
        }
        ```
- **Consultar Conta**
    - **GET** `http://localhost:5000/conta?numero_conta=123`
- **Realizar Transação**
    - **POST** `http://localhost:5000/transacao`
    - Corpo (JSON):
        ```json
        {
            "forma_pagamento": "D",
            "numero_conta": 123,
            "valor": 100.0
        }
        ```


### Notas Finais

Este projeto foi desenvolvido como parte de um desafio técnico para uma vaga de programador. O foco foi implementar uma solução que prioriza código limpo, boas práticas de desenvolvimento e uma estrutura que permita fácil manutenção e extensibilidade da API.

---

**Autor**: Gustavo Soares
