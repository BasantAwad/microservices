from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    user_id = models.CharField(max_length=50)  # Reference to auth user_id
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'courses'
