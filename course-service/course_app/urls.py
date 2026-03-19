from django.urls import path
from . import views

urlpatterns = [
    path('', RegisterCourseView.as_view(), name='register_course'),
]
