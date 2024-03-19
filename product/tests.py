from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Product, Material, ProductMaterial, Warehouse


# class ModelTest(TestCase):
#     def setUp(self):
#         product = Product.objects.create(
#             product_name="Bryuki",
#             code="123456789123"
#         )
#         material = Material.objects.create(
#             material_name='Koja'
#         )
#         ProductMaterial.objects.create(
#             product=product,
#             material=material,
#             quantity=10.5
#         )
#         Warehouse.objects.create(
#             material=material,
#             remainder=50,
#             price=12.99
#         )
#
#     def test_product(self):
#         obj = Product.objects.get(code='123456789123')
#         self.assertEqual(obj.product_name, 'Bryuki')
#
#     def test_material(self):
#         obj = Material.objects.get(material_name='Koja')
#         self.assertEqual(obj.material_name, 'Koja')
#
#     def test_product_material(self):
#         obj = ProductMaterial.objects.get(product='Bryuki')
#
#         self.assertEqual(obj.material, 'Koja')
#         self.assertEqual(obj.quantity, 10.5)
#
#     def test_warehouse(self):
#         obj = Warehouse.objects.get(price=12.99)
#
#         self.assertEqual(obj.remainder, 50)
#         self.assertEqual(obj.price, '12.99')
#         self.assertEqual(obj.material, "Koja")
#
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

