from django.contrib import admin
from django.urls import path 
from user_auth.views import Userview,Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",Userview.as_view()),
    path('login',Login.as_view())
]