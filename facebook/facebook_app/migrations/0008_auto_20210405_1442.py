# Generated by Django 3.1.5 on 2021-04-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook_app', '0007_auto_20210405_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
    ]
