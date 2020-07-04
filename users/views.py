from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import CustomUser
from .forms import CustomUserCreationForm


class IndexView(generic.ListView):
    template_name = 'users/index.html'

    def get_queryset(self):
        return CustomUser.objects.all()


class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)


class ProfileUpdateView(generic.UpdateView):
    model = CustomUser
    template_name = 'users/profile_update_form.html'
    fields = ['username', 'first_name', 'last_name']

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)


class SignupView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
