from django.test import TestCase
from django.db.utils import IntegrityError

from user.models import User, TemporaryUser

from .models import Order


class TestModel(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test_user', email='test@gmail.com')
        user.set_password('password')
        user.save()
        temp_user = TemporaryUser.objects.create(email='test@gmail.com', first_name='test', last_name='test')
        temp_user.save()

    def test_order_with_user_and_temp_user(self):
        user = User.objects.get(username='test_user')
        temp_user = TemporaryUser.objects.get(email='test@gmail.com')
        order = Order(user=user, temp_user=temp_user, price=10)
        self.assertRaises(IntegrityError, order.save)

    def test_order_without_user_and_temp_user(self):
        order = Order(price=10)
        self.assertRaises(IntegrityError, order.save)

    def test_order_with_temp_user(self):
        self.assertEqual(Order.objects.count(), 0)
        temp_user = TemporaryUser.objects.get(email='test@gmail.com')
        order = Order(temp_user=temp_user, price=10)
        order.save()
        self.assertEqual(Order.objects.count(), 1)


class TestModel2(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test_user', email='test@gmail.com')
        user.set_password('password')
        user.save()

    def test_order_create(self):
        user = User.objects.get(username='test_user')
        order = Order.objects.create(price=10, user=user)
        order.save()
        self.assertEqual(user.amount_of_orders, 1)

    def test_order_delete(self):
        user = User.objects.get(username='test_user')
        order = Order.objects.get(id=1)
        order.delete()
        self.assertEqual(user.amount_of_orders, 0)