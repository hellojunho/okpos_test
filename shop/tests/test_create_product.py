import json

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from shop.models import Product, ProductOption, Tag


@pytest.mark.django_db()
def test_create_product() -> None:
    """
    /shop/products/ 엔드포인트로 POST 요청
    """
    client = APIClient()
    data = {
        "name": "TestProduct",
        "option_set": [
            {"pk": 1, "name": "TestOption1", "price": 1000},
            {"pk": 2, "name": "TestOption2", "price": 500},
            {"pk": 3, "name": "TestOption3", "price": 0},
        ],
        "tag_set": [{"pk": 1, "name": "ExistingTag"}, {"name": "NewTag"}],
    }

    response = client.post(
        "/shop/products/",
        data=data,
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    print(f"Request: {json.dumps(data, ensure_ascii=False, indent=4)}")

    product = Product.objects.prefetch_related("option_set", "tag_set").get(
        name="TestProduct"
    )
    options = list(product.option_set.all())
    tags = list(product.tag_set.all())

    assert product.name == "TestProduct"
    assert product.tag_set.count() == 2
    assert product.tag_set.filter(name="ExistingTag").exists()
    assert product.tag_set.filter(name="NewTag").exists()

    assert (
        product.option_set.count() == 3
    )  # TestOption1, TestOption2, TestOption3 세 개의 옵션
    assert product.option_set.filter(
        name="TestOption1"
    ).exists()  # 옵션이 존재하는지 확인
    assert product.option_set.filter(
        name="TestOption2"
    ).exists()  # 옵션이 존재하는지 확인
    assert product.option_set.filter(
        name="TestOption3"
    ).exists()  # 옵션이 존재하는지 확인
    assert (
        product.option_set.filter(name="TestOption1").first().price == 1000
    )  # 옵션 가격이 1000인지 확인
    assert (
        product.option_set.filter(name="TestOption2").first().price == 500
    )  # 옵션 가격이 500인지 확인
    assert (
        product.option_set.filter(name="TestOption3").first().price == 0
    )  # 옵션 가격이 0인지 확인

    json_response = {
        "id": product.id,
        "name": product.name,
        "options": [
            {"id": option.id, "name": option.name, "price": option.price}
            for option in options
        ],
        "tags": [{"id": tag.id, "name": tag.name} for tag in tags],
    }
    json_response = json.dumps(json_response, ensure_ascii=False, indent=4)
    print(f"Response: {json_response}")
