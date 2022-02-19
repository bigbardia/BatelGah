from django.urls import path
from . import views



urlpatterns = [
    path("" , views.ChatMain.as_view() , name = "main"),
]
