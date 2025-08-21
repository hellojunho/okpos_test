import json

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from shop.models import Product, ProductOption, Tag


@pytest.mark.django_db()
def test_patch_product() -> None:
    """
    /shop/products/1/ 엔드포인트로 PATCH 요청
    """
    product = Product.objects.create(name="TestProduct")
    tag1 = Tag.objects.create(name="ExistingTag", pk=1)
    tag2 = Tag.objects.create(name="NewTag")

    product.tag_set.add(tag1, tag2)

    ProductOption.objects.create(product=product, name="TestOption1", price=1000)
    ProductOption.objects.create(product=product, name="TestOption2", price=500)
    ProductOption.objects.create(product=product, name="TestOption3", price=0)

    client = APIClient()
    response = client.patch(
        f"/shop/products/{product.id}/",
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

    updated_product = Product.objects.get(id=product.id)
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
            for option in updated_product.option_set.all()
        ],
        "tags": [
            {"id": tag.id, "name": tag.name} for tag in updated_product.tag_set.all()
        ],
    }
    json_response = json.dumps(json_response, ensure_ascii=False, indent=4)
    print(f"Response: {json_response}")
