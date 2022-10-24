from email.policy import default
from operator import mod
from django.db import models

# Create your models here.

# tương tác với database
# có các function, hàm để tương tác dữ liệu

class Course(models.Model):
    # các trường
    ## tiêu đề khóa học
    title = models.CharField(max_length=255)
    ## giá tiền
    price = models.IntegerField(default=0)
    ## nội dung
    content = models.CharField(max_length=255)

    ### thêm dữ liệu bằng cách  