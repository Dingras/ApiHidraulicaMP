from django.urls import path
from . import views

urlpatterns = [
    path('',views.sales_view, name='sales'),
    path('delete/<int:id>/',views.sale_delete_view, name='sale_delete'),

]