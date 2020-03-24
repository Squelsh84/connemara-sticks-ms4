from django.urls import path
from . import views


urlpatterns = [
    path('account/create/', views.SignUpView, name='register'),
    path('account/login/', views.SignInView, name='login'),
    path('account/logout/', views.SignOutView, name='logout'),
]
