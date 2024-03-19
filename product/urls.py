from django.urls import path
from .views import ProductList, MaterialList, WareHouseList, ProductMaterialList, add_products

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('warehouse/', WareHouseList.as_view()),
    path('material/', MaterialList.as_view()),
    path('product-material/', ProductMaterialList.as_view()),
    path('add/', add_products),
]
