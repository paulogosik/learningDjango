from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # For example:
        # Pull data from database
        # Transform
        # Send email
        
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html')
