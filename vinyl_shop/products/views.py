from django.shortcuts import render

from products.models import Album, Genre, Artist


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'products/index.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'products/about.html', context)

def products(request):
    context = {
        'title': 'Vinyl',
        'albums': Album.objects.all(),
        'genres': Genre.objects.all(),
        'artists': Artist.objects.all()
    }
    return render(request, 'products/products.html', context)