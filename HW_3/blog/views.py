from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from django.utils import timezone
from ai.permissions import IsAdminOrIsAuthenticatedReadOnly

class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]
    #permission_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.user
        time = timezone.now()
        articles = ArticleModel.objects.filter(user=user, create_end_date__gt=time).order_by('-create_date')
        titles = [article.title for article in articles] # list 축약 문법

        titles = []

        for article in articles:
            if article.create_end_date>time:
                titles.append(article.title)

        return Response({"article_list": titles})

    def post(self, request):
        user = request.user
        title = request.data.get('title', '')
        category = request.data.get('category')
        contents = request.data.get('contents', '')
        if len(title)<=5:
            return Response({"제목이 5자 이하입니다."})
        if len(contents)<=20:
            return Response({"내용이 20자 이하입니다."})
        if category is None:
            return Response({"카테고리를 선택하세요."})

        article = ArticleModel.objects.create(user_id=user.id, title=title, contents=contents)

        article.category.add(category)

        return  Response({"create article"})

    
