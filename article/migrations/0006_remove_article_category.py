# Generated by Django 4.2.6 on 2024-01-26 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Category',
        ),
    ]
