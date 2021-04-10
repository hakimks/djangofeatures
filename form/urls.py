from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='form'
urlpatterns = [
    path('', TemplateView.as_view(template_name='form/main.html'), name='main'),
    path('example', views.example),
    path('create', views.SimpleCreate.as_view()),
]