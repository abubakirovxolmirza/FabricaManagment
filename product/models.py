from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name


class Material(models.Model):
    material_name = models.CharField(max_length=255)

    def __str__(self):
        return self.material_name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=2000, decimal_places=2)

    def __str__(self):
        return f"{self.product} {self.material} {self.quantity}"


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.material} soni {self.remainder} narxi {self.price} so'm"
