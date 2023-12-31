import pika
import psycopg2
import json

print("inicio")

# Configuração da conexão RabbitMQ
rabbitmq_credentials = pika.PlainCredentials('guest', 'guest')
rabbitmq_params = pika.ConnectionParameters('rabbitmq-service', 5672, '/', rabbitmq_credentials)
connection = pika.BlockingConnection(rabbitmq_params)
channel = connection.channel()
print("conexão rabbitmq")
# Defina a fila que você deseja consumir
queue = 'fila_api'
channel.queue_declare(queue=queue)

db_conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

def callback(ch, method, properties, body):
    try:
        # db_conn = connect_db()
        cursor = db_conn.cursor()
        metodo, query, data = get_data(body)
        # Executa query
        if metodo == "GET":
            try:
                cursor.execute(query)
                # Pega o retorno da query
                dados = cursor.fetchall()
                print("RESPOSTA: " + str(dados) + '\n\n')
            except Exception as e:
                print(f"ERRO no método GET \n Descrição erro: {e}")
                cursor.close()
                return
        else:
            try:
                cursor.execute(query)
                dados = cursor.rowcount
                if dados == -1:
                    print("RESPOSTA: Dados de input inválidos")
                else:
                    print("RESPOSTA: linhas alteradas: " + str(dados) + '\n')
            except Exception as e:
                print(f"ERRO no método {metodo} \n Descrição erro: {e}")
                cursor.close()
                return
        db_conn.commit()
        cursor.close()
        print(
            f" [x] Mensagem recebida e executada no banco de dados: {data}" + "\n\n ------------------------------ \n\n" )
    except Exception as e:
        print(f"ERRO AO PROCESSAR MENSAGEM: {e}")


channel.basic_consume(
    queue='fila_api', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C \n')
channel.start_consuming()



def get_data(body):
    # pegar dados da mensagem
    data = body.decode('utf-8')
    data = json.loads(data)
    query = data.get("query")
    metodo = data.get('metodo')
    return metodo, query, data
