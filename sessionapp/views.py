from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del(request.session['num_visits'])

    return HttpResponse('View Count =' + str(num_visits))

