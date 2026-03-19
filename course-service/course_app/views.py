from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pika
import json
import os

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .tasks import send_enrollment_notification
from rest_framework.decorators import api_view

class RegisterCourseView(APIView):
    def post(self, request):
        title = request.data.get('title')
        user_id = request.data.get('user_id')
        if not title or not user_id:
            return Response({'error': 'Title and user_id required'}, status=status.HTTP_400_BAD_REQUEST)
        course = Course.objects.create(title=title, user_id=user_id)
        # Trigger celery task for notification
        send_enrollment_notification.delay(course.id, user_id)
        return Response({'status': 'Course registered', 'course_id': course.id}, status=status.HTTP_201_CREATED)
