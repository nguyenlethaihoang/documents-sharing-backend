from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Major, Subject, User, Document
from django.http import JsonResponse
from django.core import serializers  
from .serializer import GetAllCourses, GetAllMajor, GetAllSubject, GetAllUser, DocumentSerializer
# GetAllDocument, 
from rest_framework import viewsets

from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

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
        mydata = GetAllMajor(list_major, context={'request': request}, many=True)
        return JsonResponse(data=mydata.data, safe=False)
# -----------------------------------------------------------
# Subject
class GetAllSubjectAPIView(APIView):
    def get(self, request):
        list_subject =  Subject.objects.all()
        mydata = GetAllSubject(list_subject,context={'request': request}, many=True)
        return JsonResponse(data=mydata.data, safe=False)

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
        mydata = DocumentSerializer(list_document,context={'request': request}, many=True)
        return JsonResponse(data=mydata.data, safe=False)
# # Detail
# class GetDetailDocumentAPIView(APIView):
#     def get_object(self, document_id,):
#         try:
#             return Document.objects.get(id=document_id)
#         except Document.DoesNotExist:
#             return None
#     # Retrieve
#     def get(self, request, document_id, *args, **kwargs):
#         document_instance = self.get_object(document_id)
#         if not document_instance:
#             return Response(
#                 {"res": "Object with document id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = GetAllDocument(document_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
# class PostDocumentAPIView(APIView):
#     def post(self, request, *args, **kwargs,):
#         data = {
#             'name': request.data.get('name'), 
#             'description': request.data.get('description'), 
#             'link': request.data.get('link'),
#             'date': request.data.get('date'),
#             'size': request.data.get('size'),
#             'subjectID': request.data.get('subjectID'),
#             'userID': request.data.get('userID'),
#             'status': request.data.get('status'),
#             'type': request.data.get('type'),
#             'imgUrl': request.data.get('imgUrl'),
#         }
#         serializer = GetAllDocument(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class UpadateDocumentAPIView(APIView):
#     def get_object(self, document_id,):
#         try:
#             return Document.objects.get(id=document_id)
#         except Document.DoesNotExist:
#             return None
#     def put(self, request, document_id, *args, **kwargs):
#         document_instance = self.get_object(document_id)
#         if not document_instance:
#             return Response(
#                 {"res": "Object with document id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'name': request.data.get('name'), 
#             'majorID': request.data.get('majorID'), 
#         }
#         serializer = GetAllDocument(instance = document_instance, data=data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DocumentViewSet(APIView):
#     def post(self, request, *args, **kwargs,):
#         queryset = Document.objects.all()
#         serializer_class = GetAllDocument

#         def post(self, request, *args, **kwargs):
#             name = request.data['name']
#             file = request.data['file']
#             Document.objects.create(name=name, file=file)
#             return HttpResponse({'message': 'Book created'}, status=200)

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        # name = request.data['name']
        name = 'ten tai lieu'
        Document.objects.create(name=name, file=file)
        return HttpResponse({'message': 'Document created'}, status=200)
    def post(self, request, *args, **kwargs,):
        data = {
            'name': request.data.get('name'), 
            # 'name': 'ten tai lieu',
            'link': request.data.get('link'),
            'date': request.data.get('date'),
            'size': request.data.get('size'),
            'subjectID': request.data.get('subjectID'),
            'userID': request.data.get('userID'),
            'status': request.data.get('status'),
            'type': request.data.get('type'),
            'imgUrl': request.data.get('imgUrl'), 
        }
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)