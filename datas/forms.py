from django import forms
from django.contrib.auth import authenticate
from datetime import date

from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):

    username=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user=self.cleaned_data.get("username")
        passw=self.cleaned_data.get("password")
        usern=authenticate(username=user,password=passw)
        if usern is None:
            raise forms.ValidationError("wrong credentials")


class CustomUserCreationForm(forms.Form):
    choices =  [('student', 'student'), ('cafeteria', 'cafeteria'), ('lost and found', 'lost_and_found'), ('swachh bharat', 'swachh_bharat'), ('events manager', 'events')]
    username = forms.CharField(label='Enter Username', max_length=150)
    first_name=forms.CharField(label='Enter name', max_length=150)



    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    last_name = forms.ChoiceField(choices = choices,widget=forms.RadioSelect())


    class Meta:
        model=User
        fields={'username','first_name','last_name','e-mail','password1','password2'}


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'])

        return user


class select2(forms.Form):
    choices = [('student', 'student'), ('cafeteria', 'cafeteria'), ('lost_and_found', 'lost_and_found'), ('swachh', 'swachh')]
    sele = forms.ChoiceField(label ='LOGIN AS :',choices = choices)



class query(forms.Form):
    choices = [('january', 'january'), ('febuary', 'febuary'), ('march', 'march'), ('april', 'april'),
               ('may', 'may'), ('june', 'june'), ('july', 'july'), ('august', 'august'), ('september', 'september'),
               ('octuber', 'octuber'),
               ('november', 'november'), ('december', 'december')]

    choices2 = [('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')]

    line= forms.CharField(label ='line numberr')
    month = forms.ChoiceField(label ='month',choices = choices)
    year = forms.ChoiceField(label ='year',choices = choices2)


