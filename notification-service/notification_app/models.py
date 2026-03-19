from django.db import models

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    course_id = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
