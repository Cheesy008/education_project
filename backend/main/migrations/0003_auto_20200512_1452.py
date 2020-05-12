# Generated by Django 3.0.4 on 2020-05-12 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0002_auto_20200317_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizresponse',
            options={'verbose_name': 'Ответ пользователя', 'verbose_name_plural': 'Ответы пользователя'},
        ),
        migrations.AlterModelOptions(
            name='quizroom',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='test_completed',
            new_name='test_created',
        ),
        migrations.RemoveField(
            model_name='quizresponse',
            name='user',
        ),
        migrations.RemoveField(
            model_name='quizroom',
            name='quiz_response',
        ),
        migrations.AddField(
            model_name='quizresponse',
            name='quiz_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_responses', to='main.QuizRoom', verbose_name='Комната'),
        ),
        migrations.AddField(
            model_name='quizroom',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='main.Quiz', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='quizroom',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='users.Profile', verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='quizroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.Profile', verbose_name='Пользователь'),
        ),
    ]
