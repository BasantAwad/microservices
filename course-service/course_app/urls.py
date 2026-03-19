from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterCourseView.as_view(), name='register_course'),
]
