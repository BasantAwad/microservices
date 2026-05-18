from .models import Notification

class NotificationController:
    @staticmethod
    def get_recent_notifications(limit=10):
        notifications = Notification.objects.all().order_by('-created_at')[:limit]
        return [{'id': n.id, 'user_id': n.user_id, 'message': n.message, 'created_at': n.created_at} for n in notifications]
