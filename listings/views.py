from django.shortcuts import render
from django.http import HttpResponse

# uses htmls from listings folder inside templates thanks to adding templates's path to settings TEMPLATES
def index(request):
    return render(request, 'listings/listings.html')

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
    