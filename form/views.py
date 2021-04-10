from django.shortcuts import render
from form.forms import BasicForm
from django.http import HttpResponse
from django.views import View

# Create your views here.

def example(request):
    form = BasicForm()
    return HttpResponse(form.as_table())

class SimpleCreate(View): 
    def get(self, request) :
        form = BasicForm()
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)