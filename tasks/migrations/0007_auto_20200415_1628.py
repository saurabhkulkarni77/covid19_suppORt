# Generated by Django 3.0.5 on 2020-04-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20200415_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskone',
            name='order_size',
            field=models.CharField(default='forgot to enter order size', max_length=1000),
        ),
        migrations.AlterField(
            model_name='taskone',
            name='delivery_time',
            field=models.CharField(choices=[('Please Select Time Slot', 'Please Select Time Slot'), ('12:00 PM till 12:30PM', '12:00 PM till 12:30PM'), ('12:30 PM till 1:00PM', '1:00 PM till 1:30PM'), ('1:30 PM till 2:00PM', '1:30 PM till 2:00PM'), ('2:00 PM till 2:30PM', '2:00 PM till 2:30PM'), ('2:30 PM till 3:00PM', '2:30 PM till 3:00PM'), ('3:00 PM till 3:30PM', '3:00 PM till 3:30PM'), ('3:30 PM till 4:00PM', '3:30 PM till 4:00PM'), ('4:00 PM till 4:30PM', '4:00 PM till 4:30PM'), ('4:30 PM till 5:00PM', '4:30 PM till 5:00PM'), ('5:00 PM till 5:30PM', '5:00 PM till 5:30PM'), ('5:30 PM till 6:00PM', '5:30 PM till 6:00PM'), ('6:00 PM till 6:30PM', '6:00 PM till 6:30PM'), ('6:30 PM till 7:00PM', '6:30 PM till 7:00PM')], default='take your time', max_length=1000),
        ),
    ]
