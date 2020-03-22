from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>',
         views.index, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>',
         views.productPage, name='product_detail'),
    path('search/', views.search, name='search'),
]
