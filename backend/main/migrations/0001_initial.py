# Generated by Django 2.2 on 2020-03-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='Текст ответа')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('question_title', models.TextField(verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('questions_count', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Количество вопросов')),
                ('description', models.TextField(verbose_name='Описание теста')),
                ('test_completed', models.BooleanField(default=False, verbose_name='Завершено создание теста')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QuizRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Завершён')),
            ],
        ),
    ]
