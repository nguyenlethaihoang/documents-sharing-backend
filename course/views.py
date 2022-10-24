from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course 
from .serializer import GetAllCourses
# Create your views here.

class GetAllCoursesAPIView(APIView):
    def get(self, request):
        list_course =  Course.objects.all()
        mydata = GetAllCourses(list_course, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)

