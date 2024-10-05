from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Sales.models import Sale

# Create your views here.
@login_required(login_url='/')
def sales_view(request):
    data_sales = Sale.objects.all()
    return render(request, 'sales.html', {'sales': data_sales})