from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import (CartViewSet)
# from .views import (CartGetUpdateDelete, CartCreate)
from .views import (CartSave, CartDetail, CartAddProduct, CartRemoveProduct)
from rest_framework import renderers


# router = DefaultRouter()
# router.register(r'', CartViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', CartSave.as_view()),
    path('<int:pk>/', CartDetail.as_view()),
    path('add/', CartAddProduct.as_view()),
    path('remove/', CartAddProduct.as_view()),
]
