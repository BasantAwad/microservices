from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from rest_framework import status

class NotificationView(APIView):
    def get(self, request):
        notifications = Notification.objects.all().order_by('-created_at')[:10]
        data = [{'id': n.id, 'user_id': n.user_id, 'message': n.message, 'created_at': n.created_at} for n in notifications]
        return Response({'notifications': data})
