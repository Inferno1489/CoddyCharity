from django.forms import ModelForm
from django import forms
from coddy.models import *


class DonateForm(ModelForm):
    class Meta:
        model = Donate
        fields = ['name', 'surname', 'email', 'tel', 'comp', 'sms']
        labels = {
            'name' : 'Имя',
            'surname' : 'Фамилия',
            'email' : 'E-mail',
            'tel' : 'Телефон',
            'comp': 'Компьютер',
            'sms': 'Деньги',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Иван'}),
            'surname': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Иванович'}),
            'email': forms.EmailInput(attrs={'class': 'field', 'placeholder': 'example@mail.ru'}),
            'tel': forms.TextInput(attrs={'class': 'field', 'placeholder': '+7 900 123 45 67', 'type': 'tel'}),
            'comp': forms.CheckboxInput(attrs={'class': 'checkbox', 'id': 'comp'}),
            'sms': forms.CheckboxInput(attrs={'class': 'checkbox', 'id': 'sms'}),
        }


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'surname', 'email', 'tel']
        labels = {
            'name' : 'Имя',
            'surname' : 'Фамилия',
            'email' : 'E-mail',
            'tel' : 'Телефон',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Иван'}),
            'surname': forms.TextInput(attrs={'class': 'field', 'placeholder': 'Иванович'}),
            'email': forms.EmailInput(attrs={'class': 'field', 'placeholder': 'example@mail.ru'}),
            'tel': forms.TextInput(attrs={'class': 'field', 'placeholder': '+7 900 123 45 67', 'type': 'tel'}),
        }