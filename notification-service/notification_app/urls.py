from django.urls import path
from . import views

urlpatterns = [
    path('', NotificationView.as_view(), name='notifications'),
]
