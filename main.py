from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import mysql.connector


app = FastAPI()

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "160499",
    "database": "aula_13_10"
}

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def get_db_connection():
    connection = mysql.connector.connect(**DB_CONFIG)
    if not connection.is_connected():
        raise HTTPException(status_code=500, detail="Houve uma falha na conexão")
    return connection

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cad_func")
def cadastrar_func(request: Request):
    return templates.TemplateResponse("cad_func.html", {"request": request})
    
@app.get("/att_func")
def cadastrar_func(request: Request):
    return templates.TemplateResponse("att_func.html", {"request": request})

@app.get("/del_func")
def del_func(request: Request):
    return templates.TemplateResponse("del_func.html", {"request": request})

@app.get("/cad_setor")
def cadastrar_setor(request: Request):
    return templates.TemplateResponse("cad_setor.html", {"request": request})


@app.get("/att_setor")
def atualizar_setor(request: Request):
    return templates.TemplateResponse("att_setor.html", {"request": request})

@app.get("/del_setor")
def del_setor(request: Request):
    return templates.TemplateResponse("del_setor.html", {"request": request})

@app.get("/cad_cargo")
def cadastrar_cargo(request: Request):
    return templates.TemplateResponse("cad_cargo.html", {"request": request})


@app.get("/att_cargo")
def atualizar_cargo(request: Request):
    return templates.TemplateResponse("att_cargo.html", {"request": request})

@app.get("/del_cargo")
def del_cargo(request: Request):
    return templates.TemplateResponse("del_cargo.html", {"request": request})

"""Início bloco de funções -> FUNCIONARIOS"""
@app.post("/insert/")
async def insert_data(
    request: Request,
    nome: str = Form(...),
    sobrenome: str = Form(...),
    data_admissao: str = Form(...),
    status_funcionario: str = Form(...),
    id_cargo: int = Form(...),
    id_setor: int = Form(...),
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        query = "INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_cargo, id_setor) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nome, sobrenome, data_admissao, status_funcionario, id_cargo, id_setor))
        connection.commit()

        cursor.close()
        connection.close()

        
        response_data = {"message": "Funcionário cadastrado com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/att_func")
async def insert_data(
    request: Request,
    nome: str = Form(...),
    sobrenome: str = Form(...),
    data_admissao: str = Form(...),
    status_funcionario: str = Form(...),
    id_cargo: int = Form(...),
    id_setor: int = Form(...),
    id_funcionario: int = Form(...)
    
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "UPDATE funcionarios set primeiro_nome = %s, sobrenome = %s,  data_admissao = %s, status_funcionario = %s, id_cargo = %s, id_setor = %s where id = %s"
        cursor.execute(query, (nome,sobrenome, data_admissao, status_funcionario, id_cargo, id_setor, id_funcionario))  
        
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Funcionário atualizado com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/del_func")
async def remove_data(
    request: Request,
    nome: str = Form(...),
    id_cargo: int = Form(...),
    id_setor: int = Form(...),
    id_funcionario: int = Form(...)
    
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM funcionarios where primeiro_nome LIKE %s and id_cargo = %s and id_setor = %s and id = %s"
        cursor.execute(query, (f'%{nome}%', id_cargo, id_setor, id_funcionario))  
        
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Funcionário removido com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""FIM BLOCO DE FUNÇÕES"""
"""INICIO BLOCO DE FUNÇÕES -> SETOR"""
@app.post("/insert_setor/")
async def insert_data(
    request: Request,
    nome: str = Form(...),
 
    
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "INSERT INTO setor(nome) VALUES (%s)"
        cursor.execute(query, (nome,))  
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Setor cadastrado com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/att_setor")
async def insert_data(
    request: Request,
    nome: str = Form(...),
    id_setor: str = Form(...),
  
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "UPDATE setor set nome = %s where id = %s "
        cursor.execute(query, (nome, id_setor))  
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Setor atualizado com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/del_setor")
async def remove_data(
    request: Request,
    nome: str = Form(...),
    id_setor: str = Form(...),
  
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM setor WHERE id = %s AND nome LIKE %s"
        cursor.execute(query, (id_setor, f'%{nome}%',))  
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Setor removido com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
"""FIM BLOCO DE FUNÇÕES"""
"""ABRE BLOCO CARGOS"""
@app.post("/insert_cargo/")
async def insert_data(
    request: Request,
    nome: str = Form(...),
    id_setor: int = Form(...),
 
    
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "INSERT INTO cargos(nome, id_setor) VALUES (%s, %s)"
        cursor.execute(query, (nome, id_setor))  
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Cargo cadastrado com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/att_cargo")
async def insert_data(
    request: Request,
    nome: str = Form(...),
    id_cargo: int = Form(...),
    id_setor: int = Form(...),
  
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "UPDATE cargos SET id_setor =%s, nome = %s where id = %s"
        cursor.execute(query, (id_setor, nome, id_cargo,))  
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Cargo atualizado com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/del_cargo")
async def remove_data(
    request: Request,
    id_cargo: int = Form(...),
    nome: str = Form(...),
  
):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = "DELETE FROM cargos WHERE id = %s AND nome LIKE %s"
        cursor.execute(query, (id_cargo, f'%{nome}%'))  
        connection.commit()

        cursor.close()
        connection.close()

        response_data = {"message": "Cargo removido com sucesso!!"}
        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
"""FIM DO BLOCO CARGOS"""
if __name__ == "__main__":
    import uvicorn as uv
    uv.run(app, host="0.0.0.0", port=8000)
