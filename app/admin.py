from django.contrib import admin

from app.models import Book, Author, Category, Publisher


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['category', 'publisher']
    filter_horizontal = ['authors']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


class PublisherAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
