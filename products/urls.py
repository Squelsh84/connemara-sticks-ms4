from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.productPage, name='product'),
    path('products/', views.allProducts, name='products'),

]
