# API com FastAPI e MySQL

Este projeto é uma API em Python que utiliza o framework FastAPI para criar uma interface que permite aos usuários realizar operações básicas de CRUD (Create, Read, Update, Delete) em um banco de dados MySQL.

## Funcionalidades

- **C**reate: Você pode adicionar novos registros ao banco de dados por meio da API.
- **R**ead: É possível recuperar informações do banco de dados por meio da API.
- **U**pdate: Os registros existentes podem ser atualizados por meio da API.
- **D**elete: Você pode excluir registros do banco de dados usando a API.

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Um moderno framework web para construir APIs com Python.
- [MySQL](https://www.mysql.com/): Um sistema de gerenciamento de banco de dados relacional.
- [Python](https://www.python.org/): A linguagem de programação utilizada para desenvolver a API.

## Pré-requisitos

- Certifique-se de ter Python instalado na sua máquina. Você pode fazer o download em [python.org](https://www.python.org/downloads/).
- Você precisará de um servidor MySQL ou um serviço MySQL online para hospedar seu banco de dados.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/CaetanoxMTZ/crud_python.git
cd fastpython

2. Instale os requisitos: 
```bash
pip install -r requirements.txt

3. Inicie o servidor: 
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

