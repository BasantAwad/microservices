from rest_framework.views import APIView
from rest_framework.response import Response
from .controllers import NotificationController

class NotificationView(APIView):
    def get(self, request):
        data = NotificationController.get_recent_notifications()
        return Response({'notifications': data})

