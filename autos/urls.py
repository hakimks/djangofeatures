from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='autos'
urlpatterns = [
    path('', TemplateView.as_view(template_name='autos/main.html'), name='main'),
    
]