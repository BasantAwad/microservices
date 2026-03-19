from celery import shared_task
from .models import Course

@shared_task
def send_enrollment_notification(course_id, user_id):
    """
    Send notification when a course is enrolled.
    This task will be called from course view and received by notification service.
    """
    course = Course.objects.get(id=course_id)
    message = f"Congratulations! You have enrolled in the course: {course.title}"
    print(f"Sending notification to user {user_id} for course {course.title}")
    return {'status': 'sent', 'message': message}
