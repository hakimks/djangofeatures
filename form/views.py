from django.shortcuts import render, redirect, get_object_or_404
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

class SimpleUpdate(View):
    def get(self, request):
        old_data = {
            'title': "Suzukicar",
            'mileage' : 24,
            'purchase_date': '2018-08-24'
        }
        form = BasicForm(old_data)
        ctx = {'form': form}
        return render(request, 'form/form.html', ctx)

class Validate(View):
    def get(self, request):
        old_data = {
            'title': "Vitz",
            'mileage' : 240,
            'purchase_date': '2020-07-23'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form': form}
        return render(request, 'form/form.html', ctx)
    
    def post(self, request):
        form = BasicForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, 'form/form.html', ctx)
        # save data
        return redirect('/form/success')
    
    
def success(request):
        return HttpResponse('thank You')

        