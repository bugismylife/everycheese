from django.contrib import admin
from .models import Cheese


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'firmness', 'slug', 'created','modified',)
    list_filter = ('firmness','created',)
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('created','modified',)
