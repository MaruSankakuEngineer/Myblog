from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()  # 記事データを取得
    return render(request, 'website/home.html', {'articles': articles})
