import random
import string

from django.db import DataError
from django.test import TestCase

from app.models import Category, Publisher


def generate_random_string(length: int):
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for _ in range(length))


class TestCategory(TestCase):

    def test_category_with_title_and_slug(self):
        title = generate_random_string(length=10)
        slug = generate_random_string(length=10)
        category = Category.objects.create(title=title, slug=slug)
        assert category.title == title
        assert category.slug == slug
        assert isinstance(category, Category)

    def test_category_with_title_and_no_slug(self):
        title = generate_random_string(length=10)
        category = Category.objects.create(title=title)
        assert category.title == title
        assert category.slug == ""

    def test_category_with_no_title_and_with_slug(self):
        slug = generate_random_string(length=10)
        category = Category.objects.create(slug=slug)
        assert category.title == ""
        assert category.slug == slug

    def test_category_string_representation(self):
        title = generate_random_string(length=10)
        category = Category.objects.create(title=title)
        assert str(category) == title
