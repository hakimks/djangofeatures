from django.urls import path

from .views import DumpPython

urlpatterns = [
    path('', DumpPython.as_view()),
]