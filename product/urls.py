from django.urls import path
from .views import ProductList, MaterialList, WareHouseList, ProductMaterialList, add_products

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('warehouse/', WareHouseList.as_view(), name='warehouse'),
    path('material/', MaterialList.as_view(), name='material'),
    path('product-material/', ProductMaterialList.as_view(), name='product-material'),
    path('add/', add_products, name='add_products'),
]
