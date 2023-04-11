import uuid

from django.db import models
from django.urls import reverse


def _directory(root, slug, filename):
    return f"{root}/{slug}/{filename}"


def book_directory(instance, filename):
    return _directory("books", instance.slug, filename)


def author_directory(instance, filename):
    return _directory("authors", instance.slug, filename)


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Name")
    slug = models.SlugField(max_length=100, verbose_name="URL", unique=True)
    photo = models.FileField(
        upload_to=author_directory, null=True, blank=True, verbose_name="Photo"
    )
    bio = models.TextField(default="", blank=True, verbose_name="BIO")
    born_year = models.IntegerField(verbose_name="Born year")
    death_year = models.IntegerField(null=True, blank=True, verbose_name="Death year")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:author", args=[self.slug])


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name="Title")
    slug = models.SlugField(max_length=100, verbose_name="URL", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "publisher"
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Book(models.Model):
    WESTERN = "KӀАХЭ"
    EASTERN = "ЩХЬАГЪ"
    LANGUAGES = [
        (WESTERN, "Адыгабзэ"),
        (EASTERN, "Адыгэбзэ"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, verbose_name="Title")
    slug = models.SlugField(unique=True, max_length=100, verbose_name="URL")
    cover = models.FileField(
        upload_to=book_directory, null=True, blank=True, verbose_name="Cover"
    )
    epub = models.FileField(
        upload_to=book_directory, null=True, blank=True, verbose_name="EPUB"
    )
    pdf = models.FileField(
        upload_to=book_directory, null=True, blank=True, verbose_name="PDF"
    )
    language = models.CharField(
        choices=LANGUAGES,
        max_length=20,
        blank=True,
        default="",
        verbose_name="Language",
    )
    isbn = models.CharField(max_length=100, blank=True, default="", verbose_name="ISBN")
    annotation = models.TextField(null=True, blank=True, verbose_name="Annotation")
    published_at = models.DateField(verbose_name="Published at")
    publisher = models.ForeignKey(
        Publisher,
        null=True,
        blank=True,
        related_name="books",
        default=None,
        on_delete=models.SET_DEFAULT,
        verbose_name="Publisher",
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name="books",
        default=None,
        on_delete=models.SET_DEFAULT,
        verbose_name="Category",
    )
    authors = models.ManyToManyField(
        Author, related_name="books", verbose_name="Author"
    )
    views_count = models.IntegerField(default=0, verbose_name="Views count")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book", args=[self.slug])

    def increment_view_count(self):
        self.views_count += 1
        self.save()


class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    icon_name = models.CharField(max_length=100, verbose_name="Icon name")
    url = models.URLField(max_length=100, unique=True, verbose_name="URL")

    def __str__(self):
        return self.icon_name
