# Generated by Django 2.2 on 2020-03-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='quiz',
            field=models.ManyToManyField(blank=True, to='main.Quiz', verbose_name='Тест'),
        ),
    ]