# Generated by Django 4.1.3 on 2022-11-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=201)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=201, unique=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
