from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import JsonResponse, HttpResponseRedirect


from .config import CUSTOM_ADMIN_MODELS, ADMIN_MODELS_FORMS



class IndexView(TemplateView):
    template_name = 'index_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = [model.__name__ for model in CUSTOM_ADMIN_MODELS]
        return context



class ModelListView(ListView ):
    paginate_by = 10
    template_name = 'model_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        for model in CUSTOM_ADMIN_MODELS:
            if model.__name__ == model_name:
                return model.objects.all()
        raise ValueError('Unknown model')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs['model_name']
        context['model'] = model_name
        for model in CUSTOM_ADMIN_MODELS:
            if model.__name__ == model_name:
                context['form'] = ADMIN_MODELS_FORMS[model]
        return context




class ItemCreateView(CreateView):
    def get_form_class(self):
        model_name = self.kwargs['model_name']
        for model in CUSTOM_ADMIN_MODELS:
            if model.__name__ == model_name:
                return ADMIN_MODELS_FORMS[model]
        raise ValueError('Unknown model')

    def form_valid(self, form):
        form.save()
        return JsonResponse({})


class ModelDeleteView(DeleteView):
        success_url = '/'
        slug_url_kwarg = 'mod_id'
        slug_field = 'id'
        http_method_names = ['post']

        def get_queryset(self):
            model_name = self.kwargs['model_name']
            for model in CUSTOM_ADMIN_MODELS:
                if model.__name__ == model_name:
                    return model.objects.all()
            raise ValueError('Unknown model')
        def form_valid(self, form):
            self.object.delete()
            if self.request.GET.get('redirect'):
                return HttpResponseRedirect('/')
            return JsonResponse({})