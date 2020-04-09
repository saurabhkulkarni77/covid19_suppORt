from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm
from .models import Post

def user_order_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	form.save()
        return HttpResponse('<h1>Thanks!!</h1>')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'userpagetemp.html', {'form': form})