from rest_framework import serializers
from .models import Course

class GetAllCourses(serializers.ModelSerializer):

    class Meta:
        model = Course
        # định nghĩa thông tin trong phần Field
        fields = ('id', 'title')
