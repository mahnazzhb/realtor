from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtors

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtors.objects.order_by('-hire_date')
    mvp_realtors = Realtors.objects.all().filter(is_mvp=True)
    return render(request, 'pages/about.html')
