from django.urls import path
from . import views
from django_ckeditor_5 import views as ckeditor_views  # ckeditor_5のビューをインポート
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about', views.about, name='about'),
    path('archives/', views.archive, name='archive'),
    path('archives/<int:year>/<int:month>/', views.archive_month, name='archive_month'),

    # CKEditor5の画像アップロードURLを追加
    path('ckeditor/upload/', ckeditor_views.upload_file, name='ck_editor_5_upload_file'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # メディアファイルへのURL設定