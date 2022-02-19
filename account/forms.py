from django import forms
from .models import Token, User
from django.contrib.auth import authenticate



class RegisterForm(forms.ModelForm):

    email =     forms.EmailField()
    password =  forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput , label="Confirm Password")

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

    def clean_email(self,*args , **kwargs):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email = email)
            raise forms.ValidationError("this email is already used")
        except User.DoesNotExist:
            return email

    def clean_password(self , *args , **kwargs):
        psw = self.cleaned_data['password']
        if len(psw) >= 8:
            return psw
        else:
            raise forms.ValidationError("Password should exceed 8 digits!")

    def clean_password2(self , *args , **kwargs):
        psw = self.cleaned_data['password2']
        if len(psw) >= 8:
            return psw
        else:
            raise forms.ValidationError("Password confirmation should exceed 8 digits!")

    def clean(self , *args , **kwargs):
        
        psw1 = self.cleaned_data.get("password"  ,False)
        psw2 = self.cleaned_data.get("password2" ,False)

        if psw2 == psw1:
    
            return self.cleaned_data
        else:
            raise forms.ValidationError("passwords are not the same!")

    def save(self  , *args , **kwargs):
        em = self.cleaned_data['email']
        psw = self.cleaned_data['password']
        token = Token()
        token.save()
        user = User.objects.create_user(email = em , password = psw ,  token = token)
        return user


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def save(self , commit = True ,request=None ,  *args , **kwargs ):

        user = authenticate(request=request , **self.cleaned_data)
        if user:
            return user
        else:
            return False

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username" , "about" , "status"]

class VerififcationForm(forms.Form):

    token = forms.CharField(widget=forms.PasswordInput , label="Enter the code sent in your email")
