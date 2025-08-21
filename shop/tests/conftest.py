import pytest

from shop.models import Product, ProductOption, Tag


@pytest.fixture()
def product_seed() -> int:
    p = Product.objects.create(name="TestProduct")
    t1 = Tag.objects.create(name="ExistingTag")
    t2 = Tag.objects.create(name="NewTag")
    p.tag_set.set([t1, t2])
    ProductOption.objects.create(product=p, name="TestOption1", price=1000)
    ProductOption.objects.create(product=p, name="TestOption2", price=500)
    ProductOption.objects.create(product=p, name="TestOption3", price=0)
    return p.id
