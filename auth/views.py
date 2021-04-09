from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View

# Create your views here.

class DumpPython(View):
    def get(self, req):
        resp = "<prev>\n User Data in python:\n\n"
        resp += "Login Url: " + reverse('login') + "\n"
        resp += "Logout Url: " + reverse('logout') + "\n"

        return HttpResponse(resp)