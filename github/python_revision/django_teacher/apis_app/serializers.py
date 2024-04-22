from rest_framework import serializers
from .models import Teacher


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_id', 'subject_id','dept_id']
