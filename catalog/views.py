from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"\nИмя - {name}\nТелефон - {phone}\nСообщение - {message}")

    return render(request, 'contacts.html')


def index(request):
    return render(request, 'base.html')
