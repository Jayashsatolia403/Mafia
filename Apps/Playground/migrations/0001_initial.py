# Generated by Django 3.1.7 on 2021-06-28 10:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.CharField(max_length=20)),
                ('isFilled', models.BooleanField(default=False)),
                ('isStarted', models.BooleanField(default=False)),
                ('winner', models.CharField(max_length=10)),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
