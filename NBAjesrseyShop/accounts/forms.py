from django import forms
from accounts.models import User, Address


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords did not match. Try again!")
        return confirm_password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.is_active = (True)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country', 'zip_code', 'city', 'street', 'house_no', 
                  'apartment_no', 'default_shipping_address']
        widgets = {'user_id': forms.HiddenInput()}
