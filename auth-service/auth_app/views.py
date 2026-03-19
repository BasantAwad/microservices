from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pika
import json
import os

# Create your views here.

class RegisterUserView(APIView):
    def post(self, request):
        # Logic to register user
        # Send message to notification service
        self.send_notification({'message': 'User registered'})
        return Response({'status': 'User registered'})

    def send_notification(self, message):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ.get('RABBIT_HOST', 'localhost')))
        channel = connection.channel()
        channel.queue_declare(queue='notifications')
        channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps(message))
        connection.close()