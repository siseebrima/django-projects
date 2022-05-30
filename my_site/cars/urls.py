from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('rental_review/', views.rental_view, name='rental_view'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
]
