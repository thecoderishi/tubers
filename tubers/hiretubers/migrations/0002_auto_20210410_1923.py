# Generated by Django 3.2 on 2021-04-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiretuber',
            name='tuber_city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='hiretuber',
            name='tuber_price',
            field=models.IntegerField(blank=True, default=5000),
            preserve_default=False,
        ),
    ]