from django.contrib import admin
# import model vào
from .models import Course

# Register your models here.

# đăng ký models

admin.site.register(Course)