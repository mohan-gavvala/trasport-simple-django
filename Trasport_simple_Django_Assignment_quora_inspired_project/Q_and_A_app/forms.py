from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Question, Answer
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'required': True,
                'placeholder': 'guest@example.com'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'guest',
            })
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs = {'placeholder': 'password'}
        self.fields['password2'].widget.attrs = {'placeholder': 'confirm password'}

class LoginForm(AuthenticationForm):
    class Meta:
        fields = '__all__'

class Add_Question_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['ask_question']
        widgets = {
            'ask_question': forms.TextInput(attrs={

                'placeholder': 'Write your question ?'
            })
        }

class Add_Response_Form(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['post_answer']
