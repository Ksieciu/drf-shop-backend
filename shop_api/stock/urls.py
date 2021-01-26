from django.contrib import admin
from django.urls import path
from .views import (ProductsList, CategoriesList, 
                    AddProduct, GetUpdateDeleteProduct, 
                    GetUpdateDeleteCategory)

urlpatterns = [
    path('products/', ProductsList.as_view()),
    path('products/add', AddProduct.as_view()),
    path('products/<slug:slug>', GetUpdateDeleteProduct.as_view()),
    path('categories/', CategoriesList.as_view()),
    path('categories/<slug:slug>', GetUpdateDeleteCategory.as_view()),
]