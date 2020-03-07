# Generated by Django 3.0.2 on 2020-03-07 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Answer', verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Question', verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Profile', verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quizzes', to='users.Profile', verbose_name='Создатель'),
        ),
        migrations.CreateModel(
            name='QuizRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Завершён')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizrooms', to='users.Profile', verbose_name='Создатель')),
                ('quiz_response', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.QuizResponse')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile', verbose_name='Пользователь')),
            ],
        ),
    ]
