from django.shortcuts import render
from django.core.paginator import Paginator
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
