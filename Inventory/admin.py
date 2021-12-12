from django.contrib import admin
from Inventory.models import Item, ItemType


class Item_Admin(admin.ModelAdmin):
    list_display = ('itemType',)
admin.site.register(Item, Item_Admin)
class Itemtype(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(ItemType, Itemtype)
