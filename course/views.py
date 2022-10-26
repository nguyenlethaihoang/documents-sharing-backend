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
# -----------------------------------------------------------
# Major
class GetAllMajorsAPIView(APIView):
    def get(self, request):
        list_major =  Major.objects.all()
        mydata = GetAllMajor(list_major, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)
# -----------------------------------------------------------
# Subject
class GetAllSubjectAPIView(APIView):
    def get(self, request):
        list_subject =  Subject.objects.all()
        mydata = GetAllSubject(list_subject, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)

class GetDetailSubjectAPIView(APIView):
    def get_object(self, subject_id,):
        try:
            return Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            return None
    # Retrieve
    def get(self, request, subject_id, *args, **kwargs):
        subject_instance = self.get_object(subject_id)
        if not subject_instance:
            return Response(
                {"res": "Object with subject id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = GetAllSubject(subject_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
class PostSubjectAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'), 
            'majorID': request.data.get('majorID'), 
            'imgUrl': request.data.get('imgUrl')
        }
        serializer = GetAllSubject(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UpadateSubjectAPIView(APIView):
    def get_object(self, subject_id,):
        try:
            return Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            return None
    def put(self, request, subject_id, *args, **kwargs):
        subject_instance = self.get_object(subject_id)
        if not subject_instance:
            return Response(
                {"res": "Object with subject id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'), 
            'majorID': request.data.get('majorID'), 
        }
        serializer = GetAllSubject(instance = subject_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# -----------------------------------------------------------
# Document
class GetAllDocumentAPIView(APIView):
    def get(self, request):
        list_document =  Document.objects.all()
        mydata = GetAllDocument(list_document, many=True)
        return Response( data=mydata.data, status=status.HTTP_200_OK)