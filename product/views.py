from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import defaultdict

from .models import Product, ProductMaterial, Material, Warehouse
from .serializers import ProductSerializer, MaterialSerializer, WarehouseSerializer, ProductMaterialSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialList(ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class WareHouseList(ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductMaterialList(ListCreateAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer


@api_view(['POST'])
def add_products(request):
    if request.method == 'POST':
        data = request.data
        products = data.get('products', [])

        response_data = []

        reserved_quantities = defaultdict(int)

        for product_data in products:
            product_name = product_data.get('product_name')
            product_qty = product_data.get('product_qty')

            product_materials = ProductMaterial.objects.filter(product__product_name=product_name)
            material_reservations = defaultdict(int)

            for product_material in product_materials:
                material = product_material.material
                material_reservations[material] += product_material.quantity * product_qty

            product_materials_data = []

            for material, requested_qty in material_reservations.items():
                remaining_qty = requested_qty

                material_batches = material.warehouse_set.order_by('id')

                for batch in material_batches:
                    if remaining_qty <= 0:
                        break

                    available_qty = batch.remainder - reserved_quantities[batch.id]

                    batch_qty = min(remaining_qty, available_qty)
                    remaining_qty -= batch_qty

                    reserved_quantities[batch.id] += batch_qty
                    if batch_qty > 0:
                        product_materials_data.append({
                            'material_name': material.material_name,
                            'qty': batch_qty,
                            'warehouse_id': batch.id,
                            'price': batch.price,
                        })

                if remaining_qty > 0:
                    product_materials_data.append({
                        'material_name': material.material_name,
                        'qty': remaining_qty,
                        'warehouse_id': None,
                        'price': None,
                    })

            response_data.append({
                'product_name': product_name,
                'product_qty': product_qty,
                'product_materials': product_materials_data,
            })

        return Response({"result": response_data})
