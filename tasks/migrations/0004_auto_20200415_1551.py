# Generated by Django 3.0.5 on 2020-04-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_taskone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='delivery_time',
            field=models.CharField(choices=[('12:00 PM till 12:30PM', '12:00 PM till 12:30PM')], default='take your time', max_length=1000),
        ),
    ]