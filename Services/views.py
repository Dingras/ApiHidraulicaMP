from django.shortcuts import render ,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Services.models import Service
from Services.forms import FormService


# Create your views here.
@login_required(login_url='/')
def services_view(request):
    if request.method == 'POST':
        form_service = FormService(request.POST)
        if form_service.is_valid():
            form_service.save()
            return redirect('services')
    else:
        form_service = FormService()
    data_services = Service.objects.order_by('name')
    return render(request, 'services.html',{'services':data_services, 'form_service':form_service})

@login_required(login_url='/')
def service_view(request, id):
    data_service = get_object_or_404(Service, pk=id)
    return render(request, 'service.html', {'service' : data_service})

@login_required(login_url='/')
def service_edit_view(request, id):
    if request.method == 'POST':
        form_service = FormService(request.POST)
        if form_service.is_valid():
            form_service.save()
            return redirect('services')
    else:
        data_service = get_object_or_404(Service, pk = id )
        form_service = FormService(instance = data_service)
    data_services = Service.objects.order_by('name')
    return render(request, 'services.html',{'services' : data_services,'form_service':form_service})

@login_required(login_url='/')
def service_delete_view(request, id):
    service = get_object_or_404(Service, pk=id)
    service.delete()
    return services_view(request)