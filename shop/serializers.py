from typing import Any, Dict  # ← 추가

from drf_writable_nested.mixins import UniqueFieldsMixin

# 중첩 검증 단계에서 unique 오류 방지
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from shop.models import Product, ProductOption, Tag


class TagSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False, source="id")

    class Meta:
        model = Tag
        fields = ("pk", "name")

    def create(self, validated_data: Dict[str, Any]) -> Tag:
        tag, _ = Tag.objects.get_or_create(
            name=validated_data["name"], defaults=validated_data
        )
        return tag


class ProductOptionSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False, source="id")

    class Meta:
        model = ProductOption
        fields = ("pk", "name", "price")


class ProductSerializer(WritableNestedModelSerializer):
    option_set = ProductOptionSerializer(many=True)
    tag_set = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ("pk", "name", "option_set", "tag_set")
