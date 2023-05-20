from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order
class Command(BaseCommand):
    """
    Creates order
    """
    def handle(self, *args, **kwargs):
        self.stdout.write("Create order")
        user = User.objects.get(username = admin)
        order = Order.objects.get_or_create(
            delivery_address = 'ul.Kungurtseva d.10, kv.1',
            promocode = 'SALE_09.04',
            user = user
        )