from django.shortcuts import render, redirect
from collection.forms import ServiceForm
from collection.models import Service

#Index - list of all services
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
def edit_service(request, slug):
    #Get the object
    service = Service.objects.get(slug=slug)
    
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