from django.contrib import messages
from django.views import View
from django.shortcuts import render , redirect
from .forms import RegisterForm , LoginForm , ProfileForm , VerififcationForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from .models import Token, User
from django.core.mail import send_mail


class RegisterView(View):

    def get(self,request):
        form = RegisterForm()
        return render(request , "register.html" , {"form":form})
    
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                subject="Verification Code for BatelGhah",
                message = f"this is your code {user.token.token}\n this is the link : 127.0.0.1/{user.token.get_absoloute_url()}",
                from_email="sussyemailer@gmail.com",
                recipient_list=[f"{user.email}"] ,
                fail_silently=True
            )
            messages.info(request , "Code has been sent to your email")
            return redirect(user.token.get_absoloute_url())
        else:            
            return render(request , "register.html" , {"form": form})

class LoginView(View):
    
    def get(self,request):

        form = LoginForm()
        return render(request , "login.html" , {"form" : form})

    def post(self, request):
        
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(request = request)
            if user:
                login(request , user)
                messages.info(request , "Welcome Back!")
                return redirect("profile")
        messages.error(request , "somethings wrong i can feel it!")
        return redirect("login")

@login_required(login_url= "login")
def profile_view(request):

    if request.method == "POST":
        if request.POST.get("logout" , False):
            logout(request)
            return redirect("login")
        else:
            form = ProfileForm(request.POST , instance=request.user)
            if form.is_valid():
                form.save()
                messages.info(request,"profile updated!")
                return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
        return render(request , "profile.html" , {"form" : form})

def profile_summary_view(request , slug):
    user = User.objects.get(slug = slug)
    return render(request , "profilesummary.html" , {"user":user})


def verification_view(request , pk):
    if request.method == "POST":
        token = Token.objects.get(pk = pk)
        user = User.objects.get(token = token)
        if str(request.POST['token']) == str(user.token.token):
            user.active = True
            user.save()
            login(request , user)
            messages.info(request,"Welcome to BatelGah!")
            return redirect("profile")
        else:
            print(request.POST["token"] , user.token.token)
            messages.error(request,"wrong code")
            return redirect(f"{token.get_absoloute_url()}")
    else:
        form = VerififcationForm()
        return render(request , "verification.html" , {"form" : form})

    

