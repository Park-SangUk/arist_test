# Generated by Django 3.1.1 on 2020-11-12 05:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201112_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='writer',
            field=models.CharField(max_length=30, verbose_name='WRITER'),
        ),
    ]