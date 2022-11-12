from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='/'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('click_login',views.click_login,name='click_login'),
    path('click_signup',views.click_signup,name='click_signup'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('book',views.book,name='book'),
    # path('profile',views.profile,name='profile'),
]