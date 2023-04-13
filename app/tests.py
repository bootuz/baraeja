import random
import string

from django.test import TestCase

from app.models import Category


def generate_random_string(length: int):
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for _ in range(length))


class Test(TestCase):
    def test_category(self):
        length = random.randint(10, 99)
        title = generate_random_string(length)
        slug = generate_random_string(length)
        category = Category.objects.create(title=title, slug=slug)
        assert category.title == title
        assert category.slug == slug
        assert len(category.title) == length
        assert len(category.slug) == length

    def test_category_no_slug(self):
        length = random.randint(10, 99)
        title = generate_random_string(length)
        category = Category.objects.create(title=title)
        assert category.title == title
        assert category.slug == ""
        assert len(category.title) == length
        assert len(category.slug) == 0

    def test_category_no_title(self):
        length = random.randint(10, 99)
        slug = generate_random_string(length)
        category = Category.objects.create(slug=slug)
        assert category.slug == slug
        assert category.title == ""
        assert len(category.slug) == length
        assert len(category.title) == 0

    def test_category_str(self):
        length = random.randint(10, 99)
        title = generate_random_string(length)
        category = Category.objects.create(title=title, slug=title)
        assert str(category) == title
        assert len(category.title) == length
