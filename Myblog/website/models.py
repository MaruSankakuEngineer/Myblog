from django.db import models
from ckeditor.fields import RichTextField  # リッチテキスト用フィールド


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="タイトル")
    content = RichTextField(verbose_name="内容")  # リッチテキストフィールド
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    def __str__(self):
        return self.title
