from django.urls import path
from . import views

urlpatterns = [
    path('',views.services_view, name='services'),
    path('<int:id>/', views.service_view, name='service'),
    path('edit/<int:id>/',views.service_edit_view, name='service_edit'),
    path('delete/<int:id>/',views.service_delete_view, name='service_delete'),
]