from django.shortcuts import render, get_object_or_404
from products.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def index(request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)

    paginator = Paginator(products, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'category': category_page, 'products': products})


def search(request):
    products = Product.objects.filter(name__contains=request.GET['title'])
    return render(request, 'products.html', {'products': products})
