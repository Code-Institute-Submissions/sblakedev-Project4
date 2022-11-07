from django import forms
from django.forms import ModelForm
from .models import CreateAccount, Booking


class DateInput(forms.DateInput):

    input_type = 'date'


class BookingForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )

    email_address = forms.EmailField(
        label='Email Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    phone = forms.CharField(
        label='Phone Number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'date': DateInput()
        }
