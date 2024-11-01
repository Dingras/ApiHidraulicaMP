from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Sales.models import Sale
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/')
def sales_view(request):
    data_users = User.objects.order_by('id')
    data_sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': data_sales,'users':data_users})

@login_required(login_url='/')
def sale_delete_view(request, id):
    sale = get_object_or_404(Sale, pk=id)
    sale.delete()
    return sales_view(request)