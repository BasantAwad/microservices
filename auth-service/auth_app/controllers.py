from .models import User
from celery import current_app

class AuthController:
    @staticmethod
    def register_user(username, email, password):
        if not username or not email or not password:
            return None, 'username, email, and password are required'
        if User.objects.filter(username=username).exists():
            return None, 'Username already exists'
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Send notification via RabbitMQ
        current_app.send_task(
            'notification_app.tasks.process_enrollment_notification',
            args=[str(user.id), f'User {username} registered successfully'],
            queue='notifications'
        )
        return user, None
