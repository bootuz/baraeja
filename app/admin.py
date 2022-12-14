from django.contrib import admin

from app.models import Book, Author, Category, Publisher


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["category", "publisher"]
    filter_horizontal = ["authors"]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["title"]


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ["title"]


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
