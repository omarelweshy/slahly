from django import forms
from service.models import Request

class RequestJobForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ('employee', 'user',)
        fields = ['problem']
