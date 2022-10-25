from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Major, Subject, User, Document
from .serializer import GetAllCourses, GetAllMajor, GetAllSubject, GetAllUser, GetAllDocument
# Create your views here.

class GetAllCoursesAPIView(APIView):
    def get(self, request):
        list_course =  Course.objects.all()
        mydata = GetAllCourses(list_course, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)

class GetAllMajorsAPIView(APIView):
    def get(self, request):
        list_major =  Major.objects.all()
        mydata = GetAllMajor(list_major, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)

class GetAllSubjectAPIView(APIView):
    def get(self, request):
        list_subject =  Subject.objects.all()
        mydata = GetAllSubject(list_subject, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)

