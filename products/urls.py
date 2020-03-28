from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:category_slug>/<slug:product_slug>',
         views.productPage, name='product_detail'),
    path('category/<slug:category_slug>',
         views.allProducts, name='products_by_category'),
    path('products/', views.allProducts, name='products'),
]
