# Generated by Django 4.2.4 on 2023-08-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_alter_comment_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=100, verbose_name='评论目标'),
        ),
    ]
