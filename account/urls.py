from django.urls import path
from . import views

urlpatterns = [

    path("register/" , views.RegisterView.as_view() , name="register"),
    path("login" , views.LoginView.as_view() , name="login"),
    path("myprofile/" , views.profile_view , name = 'profile' ),
    path("profilesummary/<slug:slug>" , views.profile_summary_view , name="profilesummary" ),
    path("verification/<int:pk>" , views.verification_view , name ='verification')

]

