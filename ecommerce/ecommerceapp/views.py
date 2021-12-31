from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'allHTMLFiles/index.html')

def allproducts(request):
    return render(request, 'allHTMLFiles/latest.html')

def featured(request):
    return render(request, 'allHTMLFiles/featured.html')

def review(request):
    return render(request, 'allHTMLFiles/review.html')

def viewproduct(request,id):
    return render(request, 'allHTMLFiles/viewproduct.html')

def cart(request,):
    return render(request, 'allHTMLFiles/cart.html')