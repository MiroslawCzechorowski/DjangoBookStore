from django.contrib import admin
from .models import Book
from .models import Buty
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')


class ButyAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'size', 'price')

admin.site.register(Book, BookAdmin)
admin.site.register(Buty, ButyAdmin)