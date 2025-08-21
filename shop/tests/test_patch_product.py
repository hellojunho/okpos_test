import json

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from test_create_product import test_create_product

from shop.models import Product, ProductOption, Tag


@pytest.mark.django_db()
def test_patch_product() -> None:
    """
    /shop/products/1/ 엔드포인트로 PATCH 요청
    """
    # 먼저 테스트를 위해 제품을 생성합니다.
    test_create_product()

    client = APIClient()
    response = client.patch(
        "/shop/products/1/",
        data={
            "name": "TestProduct",
            "option_set": [
                {"pk": 1, "name": "TestOption1", "price": 1000},
                {"pk": 2, "name": "Edit TestOption2", "price": 1500},
                {"name": "Edit New Option", "price": 0},
            ],
            "tag_set": [
                {"id": 1, "name": "ExistingTag"},
                {"pk": 2, "name": "NewTag"},
                {"name": "Edit New Tag"},
            ],
        },
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK

    updated_product = Product.objects.prefetch_related("option_set", "tag_set").get(
        id=1
    )
    tags = list(updated_product.tag_set.all())
    options = list(updated_product.option_set.all())

    assert updated_product.name == "TestProduct"
    assert updated_product.tag_set.count() == 3
    assert updated_product.tag_set.filter(name="ExistingTag").exists()
    assert updated_product.tag_set.filter(name="NewTag").exists()
    assert updated_product.tag_set.filter(name="Edit New Tag").exists()
    assert updated_product.option_set.count() == 3
    assert updated_product.option_set.filter(name="TestOption1").exists()
    assert updated_product.option_set.filter(name="Edit TestOption2").exists()
    assert updated_product.option_set.filter(name="Edit New Option").exists()

    json_response = {
        "id": updated_product.id,
        "name": updated_product.name,
        "options": [
            {"id": option.id, "name": option.name, "price": option.price}
            for option in options
        ],
        "tags": [{"id": tag.id, "name": tag.name} for tag in tags],
    }
    json_response = json.dumps(json_response, ensure_ascii=False, indent=4)
    print(f"Response: {json_response}")
