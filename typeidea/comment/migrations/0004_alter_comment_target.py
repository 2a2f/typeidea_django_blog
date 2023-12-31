# Generated by Django 4.2.4 on 2023-08-20 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content_html'),
        ('comment', '0003_alter_comment_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.post', verbose_name='评论目标'),
        ),
    ]
