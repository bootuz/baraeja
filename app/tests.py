from django.test import TestCase

from app.models import Category


class Test(TestCase):
    def test_test(self):
        category = Category.objects.create(title="Литературэ", slug="literatura")
        assert category.title == "Литературэ"
        assert category.slug == "literatura"
