from django.db import models


# Create your models here.
class Teacher(models.Model):
    teacher_id = models.IntegerField()
    subject_id = models.IntegerField()
    dept_id = models.IntegerField()
