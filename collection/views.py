from django.shortcuts import render
from collection.models import Service

def index(request):
    services = Service.objects.all()
    
    return render(request, 'index.html', {
            'services' : services,
        })
        
def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    
    return render(request, 'services/service_detail.html', {
        'service': service,
        })