# Generated by Django 3.0.2 on 2020-03-06 08:36


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ST', 'Student'), ('TE', 'Teacher')], default='ST', max_length=2),
        ),
    ]
