from celery import shared_task
from .models import Notification

@shared_task
def process_enrollment_notification(user_id, course_title):
    """
    Process notification for course enrollment.
    This task is triggered via celery beat or queue.
    """
    message = f"Course '{course_title}' enrollment confirmed for user {user_id}"
    notification = Notification.objects.create(
        user_id=user_id,
        message=message,
        course_id='N/A'  # Can be passed if available
    )
    print(f"Notification created: {notification.id} for user {user_id}")
    return {'status': 'processed', 'notification_id': notification.id}
