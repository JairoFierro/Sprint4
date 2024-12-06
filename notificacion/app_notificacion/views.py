import pika
import json
from django.core.mail import send_mail
from django.conf import settings

def consumir_mensajes():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ['HOST'])
    )
    channel = connection.channel()
    channel.queue_declare(queue=settings.RABBITMQ['QUEUE'])
    def procesar_mensaje(ch, method, properties, body):
        mensaje = json.loads(body)
        enviar_correo(
            mensaje['email'],
            mensaje['tipo'],
            mensaje['contenido']
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_consume(
        queue=settings.RABBITMQ['QUEUE'], on_message_callback=procesar_mensaje
    )
    print("Esperando mensajes...")
    channel.start_consuming()

def enviar_correo(destinatario, asunto, contenido):
    try:
        send_mail(
            asunto,
            contenido,
            'noreply@ofipensiones.com',
            [destinatario],
        )
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar correo a {destinatario}: {e}")

