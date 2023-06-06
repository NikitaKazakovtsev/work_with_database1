from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        my_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        my_objects = Phone.objects.order_by('price')
    elif sort == 'max_price':
        my_objects = Phone.objects.order_by('-price')
    else:
        my_objects = Phone.objects.all()
    
    context = {'phones': my_objects}
    return render(request, template, context)


def show_product(request, slug):
    one_phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': one_phone}
    return render(request, template, context)
