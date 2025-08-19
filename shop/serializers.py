# serializers.py
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin # 중첩 검증 단계에서 unique 오류 방지

from shop.models import Tag, Product, ProductOption


class TagSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    pass


class ProductOptionSerializer(serializers.ModelSerializer):
    pass


class ProductSerializer(WritableNestedModelSerializer):
    pass