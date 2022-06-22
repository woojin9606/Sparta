from django.db import models
import datetime
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    description = models.CharField("설명", max_length=100)
    create_date = models.DateTimeField("등록일자", auto_now_add=True)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    post_start_date = models.DateField("게시 시작 일")
    post_end_date = models.DateField("게시 종료 일")

    is_active = models.BooleanField("활성화 여부", default=True)
    
    def __str__(self):
        return f"{self.user.username} 님이 올리신 제품입니다."