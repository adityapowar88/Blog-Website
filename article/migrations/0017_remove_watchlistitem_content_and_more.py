# Generated by Django 4.2.6 on 2024-02-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_alter_watchlistitem_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlistitem',
            name='content',
        ),
        migrations.RemoveField(
            model_name='watchlistitem',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='watchlistitem',
            name='title',
        ),
        migrations.AddField(
            model_name='watchlistitem',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='article.article'),
        ),
    ]
