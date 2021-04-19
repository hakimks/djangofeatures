from django.forms import ModelForm
from .models import Make

# create the form class

class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = "__all__"