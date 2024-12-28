from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-created_at')  # 最新順に取得
    return render(request, 'website/home.html', {'articles': articles})

