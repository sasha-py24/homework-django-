from django.shortcuts import render, redirect

from .models import Product, Article, Categories, Contactor, SubCategories, Order, ReviewModal
from .forms import ProductCreationForm, CategoriesCreationForm, OrderForm
from .choices import ColorChoices, MaterialChoices
from .filters import ProductFilter


from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.http import JsonResponse, HttpResponseRedirect

import datetime
from django.views.decorators.cache import cache_page
from django_filters.views import FilterView

from render_block import render_block_to_string, render_block


class IndexView(ListView):
    template_name = 'index.html'
    model = Categories
    context_object_name = 'categories'  # == {'products': products}

    def get_queryset(self):
        return self.model.objects.prefetch_related('sub_categories').all()

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
    form_class = ProductCreationForm
    success_url = '/'


class OrderView(CreateView):
    form_class = OrderForm

    def get_form_class(self):
        product = Product.objects.get(pk=self.kwargs['product_id'])
        kwargs = {
            'product': product
        }
        if self.request.user.is_authenticated:
            kwargs['user'] = self.request.user
        else:
            pass
        return kwargs


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


class CatalogView(DetailView):
    template_name = 'product_catalog.html'
    model = SubCategories
    context_object_name = 'sub_category'



class ProductListView(FilterView, ListView):
    paginate_by = 10
    template_name = "product_list.html"
    model = Product
    context_object_name = 'products'
    filterset_class = ProductFilter

    def get_queryset(self):
        search = self.request.GET.get('search')
        sub_category_id = self.kwargs['subcategory_id']
        if search:
            return Product.objects.filter(sub_category__id=sub_category_id, name__contains=search)
        return Product.objects.filter(sub_category__id=sub_category_id)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_category'] = SubCategories.objects.get(id=self.kwargs['subcategory_id'])
        return context

    def get(self, request, *args, **kwargs):
        filterset_class = self.get_filterset_class()
        self.filterset = self.get_filterset(filterset_class)

        if (
            not self.filterset.is_bound
            or self.filterset.is_valid()
            or not self.get_strict()
        ):
            self.object_list = self.filterset.qs
        else:
            self.object_list = self.filterset.queryset.none()

        context = self.get_context_data(
            filter=self.filterset, object_list=self.object_list
        )
        if self.request.GET.get('is_filter') is not None:
            return render_block(request, self.template_name, 'products', context)
        return self.render_to_response(context)



class HTMXTestView(TemplateView):
    template_name = "text.html"



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