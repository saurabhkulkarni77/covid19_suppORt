from django import forms
from .models import *
class NameForm(forms.ModelForm):
    your_name =forms.CharField(label='Your name', max_length=1000)
    email     = forms.EmailField(label="Enter Email")
    phone_number = forms.CharField(max_length=12)
    order_size = forms.CharField(label='order size', max_length=1000)
    delivery_time = forms.CharField(label = 'delivery time', max_length=1000)
    Dietary_Restrictions = forms.CharField(label='Dietary Restrictions', max_length=1000)
    class Meta:
    	model = Task
    	fields = ('your_name','email','phone_number','order_size','delivery_time','Dietary_Restrictions')


class KitchenForm(forms.ModelForm):
	complete = models.BooleanField(default=False)
	class Meta:
		model = Task
		fields = ('complete',)