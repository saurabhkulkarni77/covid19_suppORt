from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
# Create your views here.

def user_order_page(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = NameForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			form.save()
			#print(type(form))
			contact_name = request.POST.get(
				'your_name'
				, '')
			contact_email = request.POST.get(
				'email'
				, '')
			contact_phone = request.POST.get(
				'phone_number'
				, '')
			contact_order_type = request.POST.get(
				'order_choice'
				, '')
			contact_order_size = request.POST.get(
				'order_size'
				, '')
			delivery_time = request.POST.get(
				'delivery_time'
				, '')
			Dietary_Restrictions = request.POST.get(
				'Dietary_Restrictions'
				, '')
			Delivery_Address = request.POST.get(
				'Delivery_Address'
				, '')
			context = {
			'contact_name': contact_name,
			'contact_email':contact_email,
			'contact_phone':contact_phone,
			'contact_order_size':contact_order_size,
			'contact_order_type':contact_order_type,
			'delivery_time':delivery_time,
			'Dietary_Restrictions':Dietary_Restrictions,
			'Delivery_Address':Delivery_Address
			}
			template = get_template('con.txt')
			#print(contact_name)
			subject = '<DO NOT REPLY>: Thank you for you Kabab & Curry Order'
			email_from = settings.EMAIL_HOST_USER
			to = request.POST['email']
			recipient_list = [to]
			content = template.render(context)
			email = EmailMessage(subject, content, email_from, recipient_list)
			email.send()
		return HttpResponseRedirect('thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		
		form = NameForm()

	return render(request, 'tasks/userpagetemp.html', {'form': form})

def thanks(request):
	return render(request,'tasks/thanks.html')

def index(request):
	tasks = Task.objects.all().order_by('delivery_time')
	context = {'tasks': tasks}
	return render(request,'tasks/list.html',context)

def deleteTask(request,pk):
	item = Task.objects.get(id=pk)
	if request.method =='POST':
		to = item.email
		customer_name = item.your_name 
		Taskone.objects.create(your_name = item.your_name,email=item.email,phone_number=item.phone_number,order_size=item.order_size,delivery_time=item.delivery_time,Dietary_Restrictions=item.Dietary_Restrictions,Delivery_Address=item.Delivery_Address,order_choice=item.order_choice,created=item.created)
		item.delete()
		subject = '<DO NOT REPLY>: Kabab & Curry Order Ready'
		context = {
			'contact_name': customer_name}
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [to]
		template = get_template('kitchen.txt')
		content = template.render(context)
		email = EmailMessage(subject, content, email_from, recipient_list)
		email.send()
		return redirect('kitchen')
	context={'item':item}
	return render(request,'tasks/delete.html',context)

def confirmTask(request,pk):
	item = Task.objects.get(id=pk)
	if request.method =='POST':
		item.delete()
		return redirect('kitchen')
	context={'item':item}
	return render(request,'tasks/confirm.html',context)