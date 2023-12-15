from django.contrib.auth import login
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrationForm, AddressForm
from django.shortcuts import redirect


class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('shop:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_form'] = AddressForm()
        return context 
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        address_form = AddressForm(self.request.POST)
        if address_form.is_valid():
            address = address_form.save(commit=False)
            address.user_id = user
            address.default_shipping_address = True
            address.save()
        else:
            user.delete()
            return self.form_invalid(form)

        login(self.request, user)
        return redirect(self.success_url)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy('shop:home'))

    
class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.POST.get('next', None)
        if next_url:
            return redirect(reverse_lazy(next_url))
        else:
            return redirect(reverse_lazy('shop:home'))