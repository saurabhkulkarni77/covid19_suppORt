from django.db import models

# Create your models here.
class Task(models.Model):
	your_name = models.CharField(max_length=1000)
	email     = models.EmailField(default='forgot to enter email')
	phone_number = models.CharField(max_length=12,default='forgot to enter phonr number')
	order_size = models.CharField(default='forgot to enter order size',max_length=1000)
	time_choice = (
    	('Please Select Time Slot','Please Select Time Slot'),
    	('12:00 PM','12:00 PM'),
    	('12:30 PM','12:30 PM'),
    	('1:00 PM','1:00 PM'),
    	('1:30 PM','1:30 PM'),
    	('2:00 PM','2:00 PM'),
    	('2:30 PM','2:30 PM'),
    	('3:00 PM','3:00 PM'),
    	('3:30 PM','3:30 PM'),
    	('4:00 PM','4:00 PM'),
    	('4:30 PM','4:30 PM'),
    	('5:00 PM','5:00 PM'),
    	('5:30 PM','5:30 PM'),
    	('6:00 PM','6:00 PM'),
    	('6:30 PM','6:30 PM'),
    	('7:00 PM','7:00 PM'),)
	delivery_time = models.CharField(default='take your time',max_length=1000,choices=time_choice)
	Dietary_Restrictions = models.CharField(max_length=1000,default='As per menu')
	Delivery_Address = models.CharField(default='Not Necessary',max_length=100000)
	created = models.DateTimeField(auto_now_add=True)
class Taskone(models.Model):
	your_name = models.CharField(max_length=1000)
	email     = models.EmailField(default='forgot to enter email')
	phone_number = models.CharField(max_length=12,default='forgot to enter phone number')
	order_size = models.CharField(default='forgot to enter order size',max_length=1000)
	time_choice = (
    	('Please Select Time Slot','Please Select Time Slot'),
    	('12:00 PM','12:00 PM'),
    	('12:30 PM','12:30 PM'),
    	('1:00 PM','1:00 PM'),
    	('1:30 PM','1:30 PM'),
    	('2:00 PM','2:00 PM'),
    	('2:30 PM','2:30 PM'),
    	('3:00 PM','3:00 PM'),
    	('3:30 PM','3:30 PM'),
    	('4:00 PM','4:00 PM'),
    	('4:30 PM','4:30 PM'),
    	('5:00 PM','5:00 PM'),
    	('5:30 PM','5:30 PM'),
    	('6:00 PM','6:00 PM'),
    	('6:30 PM','6:30 PM'),
    	('7:00 PM','7:00 PM'),
    	)
	delivery_time = models.CharField(default='take your time',max_length=1000,choices=time_choice)
	Dietary_Restrictions = models.CharField(max_length=1000,default='As per menu')
	Delivery_Address = models.CharField(default='Not Necessary', max_length=100000)
	created = models.DateTimeField(auto_now_add=True)