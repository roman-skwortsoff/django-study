from django.core.management import BaseCommand
from shopapp.models import Product
class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **kwargs):
        self.stdout.write('Create product')
        product_names = ['Nvidia 1650 DDR6 4Gb Gigabyte', 'AMD Radeon RX 580 8Gb Gigabyte', 'AMD Radeon RX 5600 6Gb Asus']
        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Created product {product_name}")

        self.stdout.write(self.style.SUCCESS('Product created'))
