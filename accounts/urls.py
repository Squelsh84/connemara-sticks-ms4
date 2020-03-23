from django.urls import path
from . import views


urlpatterns = [
    path('account/create/', views.SignUpView, name='register'),
]
