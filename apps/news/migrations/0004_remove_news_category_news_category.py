# Generated by Django 5.1.2 on 2024-11-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='news.category'),
        ),
    ]
