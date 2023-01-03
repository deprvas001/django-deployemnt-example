from django import forms
from django.core import validators
from first_app.models import UserSignUp
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

def check_for_z(value):
    if value[0].lower() !='z':
        raise forms.ValidationError("Name Needs to Start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label ='Enter your email again:')
    text = forms.CharField()

    def clean(self):
        all_clean_data = super().clean()
        email  = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure email match!')


class NewUserForm(forms.ModelForm):
    class Meta():
        model = UserSignUp
        fields = '__all__'



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')






    