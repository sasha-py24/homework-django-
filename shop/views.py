from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product, Article, Categories
from .forms import ProductCreationForm, CategoriesCreationForm

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.http import JsonResponse, HttpResponseRedirect

import datetime



class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'  # == {'products': products}

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return
    #     return super().dispatch(request, *args, **kwargs)


# def index(request):
#         products = Product.objects.all()
#         return render(request, 'index.html',  {'products': products})


def page2(request):
    return render(request, 'page2.html', {'products': 'j'})



class ProductCreationView(CreateView):
    template_name = 'product.html'
    model = Product
    # fields = ['name', 'description', 'price']
    form_class = ProductCreationForm
    success_url = '/'




class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
    slug_url_kwarg = 'prod_id'
    slug_field = 'id'
    http_method_names = ['post']

    def form_valid(self, form):
        self.object.delete()
        if self.request.GET.get('redirect'):
            return HttpResponseRedirect('/')
        return JsonResponse({})


# def product(request):
#     form = ProductCreationForm()
#     if request.method == 'POST':
#         form = ProductCreationForm(request.POST)
#         if form.is_valid():
#                 # name = request.POST['name']
#                 # price = request.POST['price']
#                 # description = request.POST['description']
#                 # product = Product(name=name, price=price, description=description)
#              form.save()
#         else:
#             return render(request, 'product.html', {'form': form})
#     return render(request, 'product.html', {'form': form})
#


def article(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        date = request.POST['date']
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        article = Article(title=title, text=text, date=date)
        article.save()
    return render(request, 'article.html', {'title': 'article'})


# def product_details(request, id):
#     prod = Product.objects.get(id=id)
#     return render(request, 'product_details.html', {'prod': prod})


class ProductDetailsView(DetailView):
    template_name = 'product_details.html'
    model = Product
    slug_url_kwarg = 'pk'
    context_object_name = 'prod'


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    model = Product
    slug_url_kwarg = 'pk'
    context_object_name = 'prod'
    form_class = ProductCreationForm
    success_url = '/'

def categories(request):
    form_c = CategoriesCreationForm()
    if request.method == 'POST':
        form_c = CategoriesCreationForm(request.POST)
        if form_c.is_valid():
             form_c.save()
        else:
            return render(request, 'categories.html', {'form_c': form_c})
    return render(request, 'categories.html', {'form_c': form_c})






# if request.method == 'POST':
#     res = eval(f"{request.POST['num1']}{request.POST['action']}{request.POST['num2']}")
#     return render(request, 'user.html', {'res': res})
# <form method="post">
#         {% csrf_token %}
#         <input name="num1" type="number">
#         <input name="action" type="text">
#         <input name="num2" type="number">
#         <input type="submit">
# </form>
