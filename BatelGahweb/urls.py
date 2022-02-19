from django.urls.conf import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/" , include("account.urls")),
    path("" , include("chat.urls")),
]
