from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models.functions import TruncMonth
from django.db.models import Count
from .models import Article  # Post を Article に変更


def post_list(request):
    articles = Article.objects.all().order_by('-created_at')  # 最新順に取得
    paginator = Paginator(articles, 5)  # ページネーションを適用
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'website/post_list.html', {'page_obj': page_obj})


def post_detail(request, pk):
    # ArticleをID（pk）で取得
    post = Article.objects.get(pk=pk)  # Post → Articleに修正
    return render(request, 'website/post_detail.html', {'post': post})


def about(request):
    # Aboutページを残す場合はこちらを保持
    return render(request, 'website/about.html')


def archive(request):
    archives = (
        Article.objects.annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('-month')
    )
    return render(request, 'website/archive.html', {'archives': archives})

def archive_month(request, year, month):
    articles = Article.objects.filter(created_at__year=year, created_at__month=month)
    return render(request, 'website/archive_month.html', {'articles': articles, 'year': year, 'month': month})