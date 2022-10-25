from rest_framework import serializers
from .models import Course, Major, Subject, User, Document

class GetAllCourses(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title')

class GetAllMajor(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('id', 'name')

class GetAllSubject(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name' , 'majorID')

class GetAllUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'studentID' , 'name', 'permisson')

class GetAllDocument(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name' , 'description', 'link', 'date', 'size', 'subjectID', 'userID')
