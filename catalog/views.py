from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"\nИмя - {name}\nТелефон - {phone}\nСообщение - {message}")

    return render(request, 'contacts.html')


def index(request):
    return render(request, 'base.html')


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_info.html', context)
