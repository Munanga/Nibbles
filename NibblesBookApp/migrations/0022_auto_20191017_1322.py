# Generated by Django 2.2.1 on 2019-10-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NibblesBookApp', '0021_auto_20191016_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(default='None', max_length=1000),
        ),
    ]
