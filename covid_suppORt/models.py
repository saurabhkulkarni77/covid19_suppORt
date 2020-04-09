from django.db import models

class Post(models.Model):
	your_name = models.CharField(max_length=1000)
	email     = models.EmailField(default='forgot to enter email')
	phone_number = models.CharField(max_length=12,default='forgot to enter phonr number')
	order_size = models.CharField(default='forgot to enter order size',max_length=1000)
	delivery_time = models.CharField(default='take your time',max_length=1000)
	Dietary_Restrictions = models.CharField(max_length=1000,default='As per menu')
