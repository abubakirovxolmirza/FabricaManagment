from rest_framework import serializers
from .models import Product, ProductMaterial, Material, Warehouse


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['material_name']


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = ['id', 'material', 'remainder', 'price']

    def get_warehouse_id(self, obj):
        return obj.pk


class ProductMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductMaterial
        fields = ("product", "material", "quantity")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'product_name']

