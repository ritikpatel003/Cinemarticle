# Generated by Django 3.2.8 on 2021-10-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=5000)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
