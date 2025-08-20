from django.db import transaction
from rest_framework import viewsets

from shop.models import Product
from shop.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self) -> Product:
        return Product.objects.prefetch_related("tag_set", "option_set").all()
