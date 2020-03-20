from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogs, name='blogs'),
    path('', views.blog, name='blog'),
]
