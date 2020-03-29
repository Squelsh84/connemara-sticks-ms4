from django.urls import path
from . import views

urlpatterns = [
    path('thankyou/<int:order_id>', views.thanks, name='thanks'),
]
