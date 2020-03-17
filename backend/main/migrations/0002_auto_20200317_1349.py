# Generated by Django 2.2 on 2020-03-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_quiz'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizroom',
            name='owner',
            field=models.ForeignKey(default='Noname', on_delete=django.db.models.deletion.CASCADE, related_name='quizrooms', to='users.Profile', verbose_name='Создатель'),
        ),
        migrations.AddField(
            model_name='quizroom',
            name='user',
            field=models.ForeignKey(default='Noname', on_delete=django.db.models.deletion.CASCADE, to='users.Profile', verbose_name='Пользователь'),
        ),
    ]
