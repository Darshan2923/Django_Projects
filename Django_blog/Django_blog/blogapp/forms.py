from django.forms import forms
from .models import *

class ProfileForm(forms.ModeForm):
    class Meta:
        model=Profile
        fields=('phone_no','bio','facebook','instagram','linkedin','image')