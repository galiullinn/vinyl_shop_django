from django.shortcuts import render

def index(request):
    context = {
        'tilte': 'Home'
    }
    return render(request, 'products/index.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'products/about.html', context)
