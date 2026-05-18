from .models import Course
from .tasks import send_enrollment_notification

class CourseController:
    @staticmethod
    def register_course(title, user_id):
        if not title or not user_id:
            return None, 'Title and user_id required'
        course = Course.objects.create(title=title, user_id=user_id)
        send_enrollment_notification.delay(course.id, user_id)
        return course, None
