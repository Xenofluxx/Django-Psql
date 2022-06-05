from django.shortcuts import render
from django.http import HttpResponse

# uses htmls from pages inside templates thanks to adding templates's path to settings TEMPLATES
def index(request):
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')