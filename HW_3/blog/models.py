from django.db import models
import datetime
from datetime import timedelta

# Create your models here.
class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문")
    create_date = models.DateTimeField("노출 시작", default=datetime.datetime.now())
    create_end_date = models.DateTimeField("노출 종료", default=(datetime.datetime.now()+timedelta(days=7)))

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."

class Comment(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    contents = models.TextField("본문")

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 댓글입니다."

