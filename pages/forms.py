from django import forms
from django.forms import widgets
from service.models import Request, Comment

class RequestJobForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ('employee', 'user',)
        fields = ['problem']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('employee', 'user',)
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={ "class":"form-control", "name":"signature", "rows":3,}),
        }