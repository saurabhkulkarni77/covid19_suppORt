from django import forms
from .models import *
class NameForm(forms.ModelForm):
    your_name =forms.CharField(label='Your Name', max_length=1000)
    email     = forms.EmailField(label="Enter Email")
    phone_number = forms.CharField(max_length=12)
    order_size = forms.CharField(label='Number of People (Order Size)', max_length=1000)
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
    delivery_time = forms.ChoiceField(widget = forms.Select(),label = 'Pickup Time',initial='Please Select Timeslot',choices=time_choice)
    Dietary_Restrictions = forms.CharField(label='Dietary Restrictions', max_length=1000)
    class Meta:
    	model = Task
    	fields = ('your_name','email','phone_number','order_size','delivery_time','Dietary_Restrictions')
