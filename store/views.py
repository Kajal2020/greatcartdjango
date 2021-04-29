from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from category.models import Category
from django.contrib import messages


# Create your views here.
def store(request, category_slug = None):
    categories = None
    products = None

    # print(category_slug)
    # Agar t shirt aaya toh mujhe t shirt hai kya dekhna hai database mei
    if category_slug != None:
        # print('inside if block')
        categories = get_object_or_404(Category, slug = category_slug) # Category trable ke  slug field mei t-shirt kar ke koi item hai kya?
        # print(categories)
        products = Product.objects.filter(category = categories, is_available = True)
        product_count = products.count()
    else:
        # print('inside else block')
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()



    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    # category_slug = ''
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        # select * from product_table where category.slug = 'jeans' and slug='atx-jeans'
    except Product.DoesNotExist:
        messages.error(request, 'Invalid request!')
        return redirect('store')
    print(single_product)
    context = {'single_product' : single_product,}
    return render(request, 'store/product_detail.html', context)
