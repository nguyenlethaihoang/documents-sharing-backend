from rest_framework import serializers
from .models import Course, Major, Subject, User, Document

class GetAllCourses(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title')
# -----------------------------------------------------------
# Major
class GetAllMajor(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('id', 'name')
# -----------------------------------------------------------
# Subject
class GetAllSubject(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name' , 'majorID', 'imgUrl')
# -----------------------------------------------------------
# User
class GetAllUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'studentID' , 'name', 'permisson')
# -----------------------------------------------------------
# Document
# class GetAllDocument(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = ('id', 'name' , 'link', 'date', 'size', 'subjectID', 'userID', 'type', 'status', 'imgUrl', 'file')

# 

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['name','status', 'type', 'link', 'date','size' ,'subjectID'  ,'userID' ,'imgUrl','file']
