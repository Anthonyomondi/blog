# Generated by Django 3.1.7 on 2021-03-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tony_blogs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]