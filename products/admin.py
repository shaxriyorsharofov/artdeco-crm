from django.contrib import admin
from .models import File_Doc, Products, Comment, News
# Register your models here.

class File_DocAdmin(admin.TabularInline):
    model = File_Doc

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [File_DocAdmin]

admin.site.register(Products, ProductsAdmin)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(File_Doc)



