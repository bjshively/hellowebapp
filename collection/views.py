from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from collection.forms import ServiceForm
from collection.models import Service

#index - list of all services
def index(request):
    services = Service.objects.all()

    return render(request, 'index.html', {
            'services' : services,
        })

#Show service details        
def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    
    return render(request, 'services/service_detail.html', {
        'service': service,
    })
        
#Edit service details
@login_required
def edit_service(request, slug):
    #Get the object
    service = Service.objects.get(slug=slug)
    
    if service.user != request.user:
        raise Http404
    
    #Set the form we're using
    form_class = ServiceForm
    
    #If we're coming to this view via a submitted form,
    if request.method == 'POST':
        #grab the data from the submitted form
        form = form_class(data=request.POST, instance=service)
        if form.is_valid():
            #save the new data
            form.save()
            return redirect('service_detail', slug=service.slug)
            
    #otherwise just create the form
    else:
        form = form_class(instance=service)
        
    #render the template
    return render(request, 'services/edit_service.html', {
        'service': service,
        'form': form,
    })

def create_service(request):
    form_class = ServiceForm
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.slug = slugify(service.name)
            service.save()
            return redirect('service_detail', slug=service.slug)
            
    else:
        form = form_class()
        
    return render(request, 'services/create_service.html', {
        'form': form,
    })
    
#Browse views
def browse_by_name(request, initial=None):
    if initial:
        services = Service.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        services = Service.objects.all().order_by('name')
        
    return render(request, 'search/search.html', {
        'services': services,
        'initial': initial,
        })