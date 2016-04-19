#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq-5672'))
channel = connection.channel()

channel.queue_declare(queue='cadastrar-clientes')

teste = 0
while (teste < 10):
	channel.basic_publish(exchange='',
	                      routing_key='cadastrar-clientes',
	                      body='{"name":"monica", "lastname": "ribeiro"}')
	print(" [x] Sent!")
	teste = teste + 1
connection.close()
 