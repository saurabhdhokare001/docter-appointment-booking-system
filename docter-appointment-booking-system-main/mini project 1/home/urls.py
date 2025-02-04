from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("home.html",views.index, name='home'),
    path("about.html",views.about, name='about'),
    path("docter.html",views.docter, name='docter'),
    path("login.html",views.login, name='login'),
    path("signup.html",views.signup, name='signup'),
    path("submit",views.login, name='log'),
    path("Login",views.appoint, name="appoint"),
    path("Book",views.book, name="book"),
]
