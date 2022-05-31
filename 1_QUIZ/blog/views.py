from django.shortcuts import render, redirect
from .models import Category, Article
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수

def home(requst):
    return redirect('/main')

def view_main(request):
    return render(request, 'category.html')

def create_article(request):
    if request.method == 'POST':
        category = request.POST.get('category', None)
        title = request.POST.get('title',None)
        content = request.POST.get('content', None)
        my_category = Category.objects.get(category_name=category)
        my_article = Article()
        my_article.category = my_category
        my_article.title = title
        my_article.content = content
        my_article.save()
        return redirect('/main')
    elif request.method == 'GET':
        all_category = Category.objects.all()
        return render(request, 'new.html', {'category': all_category})
