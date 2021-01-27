from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, filters, viewsets
from .models import Cart, CartProduct
from .serializers import (CartSerializer)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'cart': reverse('cart-list', request=request, format=format),
#     })


# class CartViewSet(viewsets.ModelViewSet):
#     """This viewset automatically provides list, 
#     create, retrieve, update and destroy actions.
#     """
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer(data={"cat_id":pk})

        

class CartCreate(generics.CreateAPIView):
    """ 
    Adds cart to db. 
    Important - it takes categories as list 
    of category names, not dictionary.
    """
    serializer_class = CartSerializer


# class CartGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     """Get, Update or Delete cart with slug given in url"""
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer



class CartDetail(APIView):
    """
    Retrieve, update or delete a Cart instance.
    """
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        print(pk)
        serializer = CartSerializer(cart, context={'cart_id': pk})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
