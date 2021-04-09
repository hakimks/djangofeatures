from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.conf import settings

# Create your views here.

class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        isLocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >=0
        context = {
            'installed' : settings.INSTALLED_APPS,
            'isLocal' : isLocal
        }

        return render(request, 'home/main.html', context)
