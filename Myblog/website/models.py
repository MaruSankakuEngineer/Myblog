from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="タイトル")
    content = CKEditor5Field(verbose_name="内容")  # リッチテキストフィールド
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return self.title
