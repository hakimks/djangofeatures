from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode

# Create your views here.

class DumpPython(View):
    def get(self, req):
        resp = "<pre>\nUser Data in python:\n\n"
        resp += "Login Url: " + reverse('login') + "\n"
        resp += "Logout Url: " + reverse('logout') + "\n"
        if req.user.is_authenticated:
            resp += "User : " + req.user.username + "\n"
            resp += "Email : " + req.user.email + "\n"
        else:
            resp += "User is not logged in \n"

        resp += "\n"
        resp += "</pre>"
        resp += """ <a href="/authz"> Go Back </a>"""

        return HttpResponse(resp)

class ManualProtect(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'authz/main.html')
        loginurl = reverse('login') + '?' + urlencode({'next' : request.path})

        return redirect(loginurl)

class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'authz/main.html')

class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')
