from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# import vào cái View
from course.views import GetAllCoursesAPIView
from course.views import GetAllMajorsAPIView 
from course.views import GetAllSubjectAPIView, GetDetailSubjectAPIView, PostSubjectAPIView, UpadateSubjectAPIView
# from course.views import GetAllDocumentAPIView, PostDocumentAPIView, GetDetailDocumentAPIView, UpadateDocumentAPIView, 
from course.views import DocumentViewSet
# , DocumentViewSet

router = routers.DefaultRouter()
router.register('document', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('courses/', GetAllCoursesAPIView.as_view()),
    path('majors/', GetAllMajorsAPIView.as_view()),
    # url of subject
    path('subjects/', GetAllSubjectAPIView.as_view()),
    path('subjects/<int:subject_id>/', GetDetailSubjectAPIView.as_view()),
    path('subject', PostSubjectAPIView.as_view()),  
    path('subject/<int:subject_id>/', UpadateSubjectAPIView.as_view()),  
    # url of document
    # path('documents/', GetAllDocumentAPIView.as_view()),
    # path('documents/<int:document_id>/', GetDetailDocumentAPIView.as_view()),
    # path('document/', PostDocumentAPIView.as_view()),
    # path('document/<int:document_id>/', UpadateDocumentAPIView.as_view()),  
    # url of minio
    # path('updocument/', UPDocumentAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)