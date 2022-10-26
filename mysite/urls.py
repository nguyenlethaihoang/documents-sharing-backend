from django.contrib import admin
from django.urls import path

# import vào cái View
from course.views import GetAllCoursesAPIView
from course.views import GetAllMajorsAPIView 
from course.views import GetAllSubjectAPIView, GetDetailSubjectAPIView, PostSubjectAPIView, UpadateSubjectAPIView
from course.views import GetAllDocumentAPIView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', GetAllCoursesAPIView.as_view()),
    path('majors/', GetAllMajorsAPIView.as_view()),
    # url of subject
    path('subjects/', GetAllSubjectAPIView.as_view()),
    path('subjects/<int:subject_id>/', GetDetailSubjectAPIView.as_view()),
    path('subject', PostSubjectAPIView.as_view()),  
    path('subject/<int:subject_id>/', UpadateSubjectAPIView.as_view()),  
    # url of document
    path('documents/', GetAllDocumentAPIView.as_view()),
]
