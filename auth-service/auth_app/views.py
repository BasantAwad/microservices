from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery import current_app
from .models import User

# Create your views here.

class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not username or not email or not password:
            return Response({'error': 'username, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, email=email, password=password)
        # Send notification via RabbitMQ
        current_app.send_task(
            'notification_app.tasks.process_enrollment_notification',
            args=[str(user.id), f'User {username} registered successfully'],
            queue='notifications'
        )
        return Response({'status': 'User registered', 'user_id': user.id}, status=status.HTTP_201_CREATED)