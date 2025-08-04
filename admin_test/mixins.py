from .config import CUSTOM_ADMIN_MODELS


class CustomAdminURLModelMixin:
    def get_queryset(self):
        model_name = self.kwargs['model_name']
        for model in CUSTOM_ADMIN_MODELS:
            if model.__name__ == model_name:
                return model.objects.all()
        raise ValueError('Unknown model')




