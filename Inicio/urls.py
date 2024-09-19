from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/',views.register, name='register'),
    path('logout/',views.salir),
    path('users/',views.users_view, name='users'),
]