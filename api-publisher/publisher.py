import pika
from fastapi import FastAPI
from tables_db import Operadora, Procedimento, Prestador, Beneficiario
from config import log_config
import logging
from logging.config import dictConfig
import json
dictConfig(log_config)

# Configurar conexão com o RabbitMQ
# connection = pika.BlockingConnection(pika.ConnectionParameters('crud-rabbitmq-kubernetes_rabbitmq_1'))
rabbitmq_credentials = pika.PlainCredentials('guest', 'guest')
rabbitmq_params = pika.ConnectionParameters('rabbitmq-service', 5672, '/', rabbitmq_credentials)
connection = pika.BlockingConnection(rabbitmq_params)
channel = connection.channel()

# Definir a fila para enviar mensagens
queue_name = 'fila_api'
channel.queue_declare(queue=queue_name)

# Configuração API
app = FastAPI(debug=True)
logger = logging.getLogger('foo-logger')


@app.get("/")
def get_geral():
    return "Hello!!"

# CRUD OPERADORA
@app.get("/operadora")
def get_operadora_all():
    mensagem = '{"metodo": "GET", "query": "SELECT * FROM operadora;"}'
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.get("/operadora/{id}")
def get_operadora(nome: int):
    query = f"SELECT * FROM operadora where id = '{id}';"
    mensagem = {'metodo': 'GET', 'query': query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.post("/operadora")
def criar_operadora(request: Operadora):
    query = f"INSERT INTO public.operadora (nome, cnpj) VALUES ('{request.nome}', '{request.cnpj}');"
    body = {"nome": request.nome, "cnpj": request.cnpj}
    mensagem = {"metodo": "POST", "query": query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.put("/operadora/{id}")
def atualizar_operadora(id: int, request: Operadora):
    query = f"UPDATE public.operadora SET nome='{request.nome}', cnpj='{request.cnpj}' WHERE id={id};"
    body = {"nome": request.nome, "cnpj": request.cnpj}
    mensagem = {"metodo": "PUT", "query": query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.delete("/operadora/{id}")
def deletar_operadora(id: int):
    query = f"DELETE FROM public.operadora WHERE id={id};"
    mensagem = {"metodo": "DELETE", "query": query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"

# CRUD PRESTADOR
@app.get("/prestador")
def get_prestadors_all():
    mensagem = '{"metodo": "GET", "query": "SELECT * FROM prestador;"}'
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.get("/prestador/{id}")
def get_prestador(id: int):
    query = f"SELECT * FROM prestador where id = {id};"
    mensagem = {'metodo': 'GET', 'query': query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.post("/prestador")
def criar_prestador(request: Prestador):
    query = f"INSERT INTO public.prestador (nome, cnpj, cidade, estado) VALUES ('{request.nome}', '{request.cnpj}', '{request.cidade}', '{request.estado}');"
    body = {"nome": request.nome, "cnpj": request.cnpj, "cidade": request.cidade,
            "estado": request.estado}
    mensagem = {"metodo": "POST", "query": query, "body": body}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.put("/prestador/{id}")
def atualizar_aluno(id: int, request: Prestador):
    query = f"UPDATE public.prestador SET nome='{request.nome}', cnpj='{request.cnpj}', cidade='{request.cidade}', estado='{request.estado}' WHERE id={id};"
    body = {"nome": request.nome, "cnpj": request.cnpj, "cidade": request.cidade,
            "estado": request.estado}
    mensagem = {"metodo": "PUT", "query": query, "body": body}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.delete("/prestador/{id}")
def deletar_aluno(id: int):
    query = f"DELETE FROM public.prestador WHERE id={id};"
    mensagem = {"metodo": "DELETE", "query": query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"

# CRUD PROCEDIMENTO
@app.get("/procedimento")
def get_aluno_all():
    mensagem = '{"metodo": "GET", "query": "SELECT * FROM procedimento;"}'
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.get("/procedimento/{id}")
def get_aluno(id: int):
    query = f"SELECT * FROM procedimento where id = {id};"
    mensagem = {'metodo': 'GET', 'query': query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.post("/procedimento")
def criar_aluno(request: Procedimento):
    # descricao, valor, operadora_id, prestador_id
    query = f"INSERT INTO public.procedimento (descricao, valor, operadora_id) VALUES ('{request.descricao}', '{request.valor}', '{request.operadora_id}');"
    body = {"descricao": request.descricao, "valor": request.valor,
            "operadora_id": request.operadora_id}
    mensagem = {"metodo": "POST", "query": query, "body": body}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.put("/procedimento/{id}")
def atualizar_aluno(id: int, request: Procedimento):
    query = f"UPDATE public.procedimento SET descricao='{request.descricao}', valor='{request.valor}', operadora_id='{request.operadora_id}' WHERE id={id};"
    body = {"descricao": request.descricao, "valor": request.valor,
            "operadora_id": request.operadora_id}
    mensagem = {"metodo": "PUT", "query": query, "body": body}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.delete("/procedimento/{id}")
def deletar_aluno(id: int):
    query = f"DELETE FROM public.procedimento WHERE id={id};"
    mensagem = {"metodo": "DELETE", "query": query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"

# CRUD beneficiário

@app.get("/beneficiario")
def get_cursos_all():
    mensagem = '{"metodo": "GET", "query": "SELECT * FROM beneficiario;"}'
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.get("/beneficiario/{id}")
def get_curso(id: int):
    query = f"SELECT * FROM beneficiario where id = {id};"
    mensagem = {'metodo': 'GET', 'query': query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"Erro ao publicar mensagem: {e}"


@app.post("/beneficiario")
def criar_curso(request: Beneficiario):
    query = f"INSERT INTO public.beneficiario (nome, num_carteira, cidade, estado, procedimento_id, prestador_id) VALUES ('{request.nome}', '{request.num_carteira}', '{request.cidade}', '{request.estado}', '{request.procedimento_id}', '{request.prestador_id}');"
    body = {"nome": request.nome, "num_carteira": request.num_carteira, "cidade": request.cidade,
            "estado": request.estado, "procedimento_id": request.procedimento_id, "prestador_id": request.prestador_id}
    mensagem = {"metodo": "POST", "query": query, "body": body}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.put("/beneficiario/{id}")
def atualizar_aluno(id: int, request: Beneficiario):
    query = f"UPDATE public.beneficiario SET nome='{request.nome}', num_carteira='{request.num_carteira}', cidade='{request.cidade}', estado='{request.estado}', procedimento_id='{request.procedimento_id}', prestador_id='{request.prestador_id}' WHERE id={id};"
    body = {"nome": request.nome, "num_carteira": request.num_carteira, "cidade": request.cidade,
            "estado": request.estado, "procedimento_id": request.procedimento_id, "prestador_id": request.prestador_id}
    mensagem = {"metodo": "PUT", "query": query, "body": body}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


@app.delete("/beneficiario/{id}")
def deletar_aluno(id: int):
    query = f"DELETE FROM public.beneficiario WHERE id={id};"
    mensagem = {"metodo": "DELETE", "query": query}
    mensagem = json.dumps(mensagem)
    try:
        channel.basic_publish(
            exchange='', routing_key=queue_name, body=mensagem)
        return "MENSAGEM ENVIADA"
    except Exception as e:
        return f"ERRO NO ENVIO DA MENSAGEM \n Erro: {e}"


# {
#     "nome": "São Marcos",
#     "cnpj": "852369741",
#     "cidade": "Teresina",
#     "estado": "Piauí",
#     "operadora_id": 6
# }