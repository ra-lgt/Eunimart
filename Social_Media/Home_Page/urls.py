from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('login_signup',views.login_signup),
    path('register',views.register),
]