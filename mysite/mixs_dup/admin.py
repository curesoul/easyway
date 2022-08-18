from django.contrib import admin

from .models import Customer, Operator, Item, Lot, ProductionPlan, Detail


admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Lot)
admin.site.register(ProductionPlan)
admin.site.register(Detail)


