from django.shortcuts import render
from rest_framework import generics, filters
from .models import Product, Category
from .serializers import (CategorySerializer, ShowProductSerializer, ProductSerializer)


class ProductsList(generics.ListAPIView):
    """Listing all products with optional
    filtering based on query parameters.
    Filtering by: 
    category: name,
    availability: IN/OUT/SOON,
    promotion(promotion_going): Bool
    """
    queryset = Product.objects.all()
    serializer_class = ShowProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get("category", None)
        availability = self.request.query_params.get("availability", None)
        promotion = self.request.query_params.get("promotion_going", None)
        if category is not None:
            queryset = queryset.filter(category__category_name=category)
        if availability is not None:
            queryset = queryset.filter(availability=availability)
        if promotion is not None:
            queryset = queryset.filter(promotion_going=promotion)
        return queryset


class AddProduct(generics.CreateAPIView):
    """ Adds product to db. 
    Important - it takes categories as list 
    of category names, not dictionary.
    """
    serializer_class = ProductSerializer


class GetUpdateDeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    """Get, Update or Delete product with slug given in url"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    # permission_classes = [permissions.IsWorkerOrReadOnly]


class CategoriesList(generics.ListCreateAPIView):
    """List or create categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GetUpdateDeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    """Get, Update or Delete category with slug given in url"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    # permission_classes = [permissions.IsWorkerOrReadOnly]


