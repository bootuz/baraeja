import random
import string

from django.test import TestCase

from app.models import Category


def generate_random_string(length: int):
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for _ in range(length))


class Test(TestCase):
    def test_category(self):
        title = generate_random_string(10)
        slug = generate_random_string(10)
        category = Category.objects.create(title=title, slug=slug)
        assert category.title == title
        assert category.slug == slug

    def test_category_str(self):
        title = generate_random_string(10)
        category = Category.objects.create(title=title, slug=title)
        assert str(category) == title
