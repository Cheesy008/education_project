# Generated by Django 3.0.2 on 2020-03-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ST', 'Студент'), ('TE', 'Учитель')], max_length=2),
        ),
    ]
