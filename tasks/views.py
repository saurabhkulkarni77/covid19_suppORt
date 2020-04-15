from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.

def user_order_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	form.save()
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
		item.delete()
		return redirect('kitchen')
	context={'item':item}
	return render(request,'tasks/delete.html',context)

def confirmTask(request,pk):
	item = Task.objects.get(id=pk)
	if request.method =='POST':
		#item.save(using='analyticsdb')
		Taskone.objects.create(your_name = item.your_name,email=item.email,phone_number=item.phone_number,order_size=item.order_size,delivery_time=item.delivery_time,Dietary_Restrictions=item.Dietary_Restrictions)
		return redirect('kitchen')
	context={'item':item}
	return render(request,'tasks/confirm.html',context)