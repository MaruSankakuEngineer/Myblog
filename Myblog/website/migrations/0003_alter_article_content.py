# Generated by Django 5.1.4 on 2025-01-04 07:34

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_article_content_alter_article_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='内容'),
        ),
    ]
