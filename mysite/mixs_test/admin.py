from django.contrib import admin

from .models import Customer, Operator, Item, Lot, Detail


class DetailAdmin(admin.ModelAdmin):
    list_display = ('batch', 'mv')
    list_filter = ['item', 'lot']
    search_fields = ['item']


admin.site.register(Customer)
admin.site.register(Operator)
admin.site.register(Item)
admin.site.register(Lot)
admin.site.register(Detail, DetailAdmin)
