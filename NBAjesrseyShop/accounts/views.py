from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrationForm
from django.shortcuts import render
from django.views import View


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('address') 

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        return valid
     

class AddressAdd(View):
    def get(self,request):
        return render(request, 'registration/address.html')