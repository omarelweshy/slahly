from django.urls import reverse_lazy
from django.views.generic import * 
from .forms import *
from .models import User

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

class ProfileView(UpdateView):
    model = User
    form = UserChangeForm
    template_name = 'profile.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'address', 'city', 'phone']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user