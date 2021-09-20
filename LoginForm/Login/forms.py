from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticate
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Account


class RegistrationForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2', 'captcha')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid password or email')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError(f'Email is already use')




