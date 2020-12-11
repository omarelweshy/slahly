from django.urls import reverse_lazy
from django.views.generic import * 
from .forms import *
from .models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

class ProfileView(SuccessMessageMixin, UpdateView):
    model = User
    form = UserChangeForm
    template_name = 'profile.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'address', 'phone']
    success_url = reverse_lazy('profile')
    success_message = 'تم تحديث معلوماتك بنجاح'

    def get_object(self):
        return self.request.user