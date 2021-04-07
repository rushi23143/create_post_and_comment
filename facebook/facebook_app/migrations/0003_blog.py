# Generated by Django 3.1.5 on 2021-04-03 19:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_app', '0002_auto_20210404_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('title', models.CharField(max_length=100, verbose_name='Post title')),
                ('description', models.TextField(verbose_name='Post Description')),
                ('posted_date', models.DateField(default=datetime.date.today)),
                ('good_name', models.CharField(max_length=100, verbose_name='Good name')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook_app.user')),
            ],
        ),
    ]
