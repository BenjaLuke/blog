from django.contrib import admin
from categories.models import Category

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = ['title','published']