# Generated by Django 2.2.1 on 2019-10-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NibblesBookApp', '0016_auto_20191009_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
