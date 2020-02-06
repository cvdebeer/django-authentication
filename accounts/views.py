from django.shortcuts import render

# Create your views here.
def index(request):
    '''Retunr index.html file'''
    return render(request, 'index.html')