# Generated by Django 4.2.7 on 2023-11-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.CharField(choices=[('Not Completed', 'Not Completed'), ('Completed', 'Completed')], default='Not Completed', max_length=20),
        ),
    ]
