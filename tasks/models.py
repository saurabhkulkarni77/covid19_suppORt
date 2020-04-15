from django.db import models

# Create your models here.
class Task(models.Model):
	your_name = models.CharField(max_length=1000)
	email     = models.EmailField(default='forgot to enter email')
	phone_number = models.CharField(max_length=12,default='forgot to enter phonr number')
	order_size = models.CharField(default='forgot to enter order size',max_length=1000)
	time_choice = (
    	('Please Select Time Slot','Please Select Time Slot'),
    	('12:00 PM till 12:30PM','12:00 PM till 12:30PM'),
    	('12:30 PM till 1:00PM','1:00 PM till 1:30PM'),
    	('1:30 PM till 2:00PM','1:30 PM till 2:00PM'),
    	('2:00 PM till 2:30PM','2:00 PM till 2:30PM'),
    	('2:30 PM till 3:00PM','2:30 PM till 3:00PM'),
    	('3:00 PM till 3:30PM','3:00 PM till 3:30PM'),
    	('3:30 PM till 4:00PM','3:30 PM till 4:00PM'),
    	('4:00 PM till 4:30PM','4:00 PM till 4:30PM'),
    	('4:30 PM till 5:00PM','4:30 PM till 5:00PM'),
    	('5:00 PM till 5:30PM','5:00 PM till 5:30PM'),
    	('5:30 PM till 6:00PM','5:30 PM till 6:00PM'),
    	('6:00 PM till 6:30PM','6:00 PM till 6:30PM'),
    	('6:30 PM till 7:00PM','6:30 PM till 7:00PM'),
    	)
	delivery_time = models.CharField(default='take your time',max_length=1000,choices=time_choice)
	Dietary_Restrictions = models.CharField(max_length=1000,default='As per menu')
	created = models.DateTimeField(auto_now_add=True)
class Taskone(models.Model):
	your_name = models.CharField(max_length=1000)
	email     = models.EmailField(default='forgot to enter email')
	phone_number = models.CharField(max_length=12,default='forgot to enter phonr number')
	order_size = models.CharField(default='forgot to enter order size',max_length=1000)
	time_choice = (
    	('Please Select Time Slot','Please Select Time Slot'),
    	('12:00 PM till 12:30PM','12:00 PM till 12:30PM'),
    	('12:30 PM till 1:00PM','1:00 PM till 1:30PM'),
    	('1:30 PM till 2:00PM','1:30 PM till 2:00PM'),
    	('2:00 PM till 2:30PM','2:00 PM till 2:30PM'),
    	('2:30 PM till 3:00PM','2:30 PM till 3:00PM'),
    	('3:00 PM till 3:30PM','3:00 PM till 3:30PM'),
    	('3:30 PM till 4:00PM','3:30 PM till 4:00PM'),
    	('4:00 PM till 4:30PM','4:00 PM till 4:30PM'),
    	('4:30 PM till 5:00PM','4:30 PM till 5:00PM'),
    	('5:00 PM till 5:30PM','5:00 PM till 5:30PM'),
    	('5:30 PM till 6:00PM','5:30 PM till 6:00PM'),
    	('6:00 PM till 6:30PM','6:00 PM till 6:30PM'),
    	('6:30 PM till 7:00PM','6:30 PM till 7:00PM'),
    	)
	delivery_time = models.CharField(default='take your time',max_length=1000,choices=time_choice)
	Dietary_Restrictions = models.CharField(max_length=1000,default='As per menu')
	created = models.DateTimeField(auto_now_add=True)