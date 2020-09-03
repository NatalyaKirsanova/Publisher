from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass