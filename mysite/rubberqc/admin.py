from django.contrib import admin

from .models import MixSItemSpecs, MixSCheckResult, MixSCheckDetail


class MixSCheckDetailInline(admin.TabularInline):
    model = MixSCheckDetail
    extra = 100


class MixSCheckResultAdmin(admin.ModelAdmin):
    inlines = [MixSCheckDetailInline]
    # fieldsets = [
    #     (None, {'fields': ['item', 'lot']}),
    #     ('检查详情', {'fields': ['id', 'batch', 'mv']}),
    # ]


admin.site.register(MixSItemSpecs)
admin.site.register(MixSCheckDetail)
admin.site.register(MixSCheckResult, MixSCheckResultAdmin)
