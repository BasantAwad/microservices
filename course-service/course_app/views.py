from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .controllers import CourseController

class RegisterCourseView(APIView):
    def post(self, request):
        course, error = CourseController.register_course(
            request.data.get('title'),
            request.data.get('user_id')
        )
        if error:
            return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Course registered', 'course_id': course.id}, status=status.HTTP_201_CREATED)
