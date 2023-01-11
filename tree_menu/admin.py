from django.contrib import admin

from tree_menu.forms import ItemForm
from tree_menu.models import Item, Menu


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    form = ItemForm


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
