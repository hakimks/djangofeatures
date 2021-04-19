from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Make, Auto
from .forms import MakeForm


# Create your views here.

class MainView(View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}

        return render(request, 'autos/auto-list.html', ctx)

class MakeView(View):
    pass
class MakeCreate(View):
    pass

class MakeUpdate(View):
    pass
class MakeDelete(View):
    pass

class AutoCreate(View):
    pass
class AutoUpdate(view):
    pass
class AutoDelete(View):
    pass
