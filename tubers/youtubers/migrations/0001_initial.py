# Generated by Django 3.1.7 on 2021-04-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='medial/ytubers/%Y/%m/')),
                ('video_url', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(max_length=255)),
                ('camera_type', models.CharField(max_length=255)),
                ('subs_count', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('is_features', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
