from django.contrib import admin
# import model vào
from .models import Course, Major, Subject, User, Document

# Register your models here.

# đăng ký models

admin.site.register(Course)
admin.site.register(Major)
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Document)