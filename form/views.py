from django.shortcuts import render
from form.forms import BasicForm
from django.http import HttpResponse

# Create your views here.

def example(request):
    form = BasicForm()
    return HttpResponse(form.as_table())
