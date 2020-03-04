# Generated by Django 3.0.2 on 2020-03-04 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('questions_count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество вопросов')),
                ('description', models.TextField(verbose_name='Описание теста')),
                ('score', models.PositiveSmallIntegerField(default=0, verbose_name='Количество баллов')),
                ('completed', models.BooleanField(default=False, verbose_name='Завершен')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.TextField(verbose_name='Текст вопроса')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Quiz', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='Текст вопроса')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question', verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
