from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import (CartViewSet)
# from .views import (CartGetUpdateDelete, CartCreate)
from .views import (CartCreate, CartDetail)
from rest_framework import renderers


# router = DefaultRouter()
# router.register(r'', CartViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('<int:pk>/', CartDetail.as_view()),
    path('', CartCreate.as_view()),
]
