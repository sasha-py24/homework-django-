from .admin_test.config import CUSTOM_ADMIN_MODELS



class CustomCart:
    def dispatch(self):
        product_id = self.kwargs['product_id']
        if self.request.session.get('cart') is None:
            self.request.session['cart'] = {}
        return