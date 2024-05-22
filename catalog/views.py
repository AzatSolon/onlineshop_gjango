import csv

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from pytils.translit import slugify

from catalog.models import Product


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'{name} ({phone}) написал: {message}')

        with open('contact_info.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, message])

        return HttpResponseRedirect(self.request.path)


class ProductListView(ListView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price', 'data_make', 'data_last_save', 'views_counter',
              'is_published']
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_delete')
