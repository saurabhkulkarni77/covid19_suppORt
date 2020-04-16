from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
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
        	'delivery_time':delivery_time,
        	'Dietary_Restrictions':Dietary_Restrictions,
        	'Delivery_Address':Delivery_Address
        	}
        	template = get_template('con.txt')
        	#print(contact_name)
        	subject = 'Your order is ready!!'
        	message = 'Your order is ready!!'
        	email_from = settings.EMAIL_HOST_USER
        	to = request.POST['email']
        	recipient_list = [to]
        	content = template.render(context)
        	#recipient_list = ['sskkulk@gmail.com','lucawrab@buffalo.edu']
        	send_mail( subject, content, email_from, recipient_list )
        	# email = EmailMessage(
         #        "New contact form submission",
         #        content,
         #        "Your website" +'',
         #        ['youremail@gmail.com'],
         #        headers = {'Reply-To': contact_email }
         #    )
        return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
    	
        form = NameForm()

    return render(request, 'tasks/userpagetemp.html', {'form': form})

def thanks(request):
    return render(request,'tasks/thanks.html')

def index(request):
	tasks = Task.objects.all()
	context = {'tasks': tasks}
	return render(request,'tasks/list.html',context)

def deleteTask(request,pk):
	item = Task.objects.get(id=pk)
	if request.method =='POST':
		to = item.email
		Taskone.objects.create(your_name = item.your_name,email=item.email,phone_number=item.phone_number,order_size=item.order_size,delivery_time=item.delivery_time,Dietary_Restrictions=item.Dietary_Restrictions,Delivery_Address=item.Delivery_Address)
		item.delete()
		subject = 'Thank you for'
		message = 'it  means a world to us'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [to]
		send_mail( subject, message, email_from, recipient_list )
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