from django.shortcuts import render

def index(request):
    
    #Passing a number into the view
    number = 6
    
    return render(request, 'index.html', {
            'number': number,
        })