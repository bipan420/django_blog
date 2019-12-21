#inherits from the forms object
from django import forms
#import user model
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #create the user whenever it validates
        model = User
        fields = ['username', 'email', 'password1', 'password2']
