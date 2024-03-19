from django.test import TestCase
from .models import Product, Material, ProductMaterial, Warehouse


class ModelTests(TestCase):

    def test_product_creation(self):
        product = Product.objects.create(product_name="Chair", code="CH123")
        self.assertEqual(product.product_name, "Chair")
        self.assertEqual(product.code, "CH123")

    def test_material_creation(self):
        material = Material.objects.create(material_name="Wood")
        self.assertEqual(material.material_name, "Wood")

    def test_product_material_creation(self):
        product = Product.objects.create(product_name="Table", code="TB456")
        material = Material.objects.create(material_name="Steel")
        product_material = ProductMaterial.objects.create(
            product=product,
            material=material,
            quantity=10.5
        )
        self.assertEqual(product_material.product, product)
        self.assertEqual(product_material.material, material)
        self.assertEqual(product_material.quantity, 10.5)

    def test_warehouse_creation(self):
        material = Material.objects.create(material_name="Plastic")
        warehouse = Warehouse.objects.create(
            material=material,
            remainder=50,
            price=12.99
        )
        self.assertEqual(warehouse.material, material)
        self.assertEqual(warehouse.remainder, 50)
        self.assertEqual(warehouse.price, 12.99)

