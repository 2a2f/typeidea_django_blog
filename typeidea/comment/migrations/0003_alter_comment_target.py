# Generated by Django 4.1.5 on 2023-02-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=100, verbose_name='评论目标'),
        ),
    ]