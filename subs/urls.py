from django.urls import path

from . import views

urlpatterns = [
    path('', views.register_guest, name='register_guest'),
    path('thanks', views.thank_you, name='thank_you'),
]
