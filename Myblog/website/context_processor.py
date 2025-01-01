from django.db.models import Count
from .models import Article
from django.db.models.functions import TruncMonth


def add_archives(request):
    archives = (
        Article.objects.annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("-month")
    )
    return {"archives": archives}