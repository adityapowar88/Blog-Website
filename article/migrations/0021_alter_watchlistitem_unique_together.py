# Generated by Django 4.2.6 on 2024-02-12 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_watchlistitem_pub_date_alter_watchlistitem_article_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='watchlistitem',
            unique_together=set(),
        ),
    ]
