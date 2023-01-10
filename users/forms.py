# django_project/users/forms.py
import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm

from blog.models import Flight


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


from django.core.exceptions import ValidationError
class FlightForm(forms.ModelForm,):

    class Meta:
        model = Flight
        fields = ('flight_id', 'name', 'country', 'company', 'succes','date','upload')

    def save(self, commit=True):
        flight = super(FlightForm, self).save(commit=False)
        if commit:
            flight.save()
        return flight



    def clean_date(self):
        date = self.cleaned_data['date']

        if datetime.datetime.today().date() < date.date() :
            raise ValidationError("zła data")
        return date


