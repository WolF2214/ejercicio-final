# Generated by Django 4.0.1 on 2022-02-02 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_task_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['expiredate']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='expiredate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expired Date '),
        ),
    ]