from django.db import models

# Create your models here.
class Task(models.Model):
	your_name = models.CharField(max_length=1000)
	email     = models.EmailField(default='forgot to enter email')
	phone_number = models.CharField(max_length=12,default='forgot to enter phonr number')
	order_size = models.CharField(default='forgot to enter order size',max_length=1000)
	delivery_time = models.CharField(default='take your time',max_length=1000)
	Dietary_Restrictions = models.CharField(max_length=1000,default='As per menu')
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)